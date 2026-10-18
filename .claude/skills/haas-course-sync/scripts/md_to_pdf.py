import sys, re, html, subprocess, markdown, pathlib

CSS = """
<style>
body { font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Helvetica, Arial, sans-serif;
       max-width: 900px; margin: 40px auto; padding: 0 20px; color: #1a1a1a; line-height: 1.5; font-size: 15px; }
h1 { font-size: 24px; border-bottom: 2px solid #333; padding-bottom: 8px; }
h2 { font-size: 19px; margin-top: 32px; border-bottom: 1px solid #ddd; padding-bottom: 4px; }
h3 { font-size: 16px; margin-top: 24px; }
table { border-collapse: collapse; width: 100%; margin: 16px 0; font-size: 13.5px; }
th, td { border: 1px solid #ccc; padding: 8px 10px; text-align: left; vertical-align: top; }
th { background: #2d2d2d; color: white; }
tr:nth-child(even) { background: #f7f7f7; }
code { background: #eee; padding: 1px 5px; border-radius: 3px; font-size: 0.9em; }
pre code { display: block; padding: 10px; overflow-x: auto; }
hr { border: none; border-top: 1px solid #ddd; margin: 28px 0; }
strong { color: #000; }
ul, ol { padding-left: 22px; }
@media print {
  body { margin: 15px auto; }
  h2 { page-break-after: avoid; }
  table { page-break-inside: avoid; }
}
</style>
"""

MERMAID_JS = """
<script src="https://cdn.jsdelivr.net/npm/mermaid@10/dist/mermaid.min.js"></script>
<script>mermaid.initialize({startOnLoad: true, theme: 'neutral'});</script>
"""

MATHJAX_JS = """
<script>
MathJax = { tex: { inlineMath: [['\\\\(', '\\\\)']] }, svg: { fontCache: 'global' } };
</script>
<script src="https://cdn.jsdelivr.net/npm/mathjax@3/es5/tex-svg.js"></script>
"""

# These notes use $...$ for LaTeX math AND plain dollar amounts ("$15", "$2.33"),
# inconsistently and sometimes in the same file -- occasionally even the same line.
# Naively enabling $-delimited math would swallow whole prose sentences between two
# unrelated dollar amounts into a garbled "equation". Markdown's own bold/italic
# parser (** and _) also doesn't know $...$ is special, so it happily eats asterisks
# *inside* real math (e.g. turns "$q^{**}$" into "$q^{}$") independent of all this.
#
# Fix: find $...$ spans (an unescaped \$ is never a delimiter), pull each one out
# into a placeholder *before* running python-markdown so nothing inside it can be
# mangled, then after markdown runs, decide per-span whether it looks like real math
# (short, symbol-dense, no prose) -- if so, render it with MathJax; if not (or if
# unsure), paste the original text back verbatim. A false negative just means one
# formula displays as plain text instead of a pretty equation -- no harm done. A
# false positive would corrupt real prose, so the heuristic is deliberately
# conservative and biased toward "not math" when in doubt.
MATH_SPAN_RE = re.compile(r'(?<!\\)\$((?:[^$\\\n]|\\.)+?)(?<!\\)\$')
_HAS_MARKER_RE = re.compile(r'[\\^_{}]')      # backslash command, sub/superscript, braces -- strong LaTeX signal
_LOWERCASE_WORD_RE = re.compile(r'[a-z]{4,}')  # a 4+ letter lowercase run is virtually always an English word,
                                                # never a math variable/abbreviation (those run MC, AR, cs, etc.)

def looks_like_math(span: str) -> bool:
    # A LaTeX marker is a strong, reliable signal on its own -- trust it even if the span has spaces
    # (e.g. "C(\beta x) < \beta C(x)"), and only bail out on the one thing that still risks swallowing
    # prose: a sentence boundary inside the span.
    if _HAS_MARKER_RE.search(span):
        return len(span) <= 80 and '. ' not in span
    # No LaTeX marker at all: this is either a bare short algebraic expression ("N", "CS/N", "T(q)=pq+F")
    # or -- far more likely in these notes -- two unrelated dollar amounts that happened to land on the
    # same line and got paired by the regex (e.g. "500,000 (a 50/50 shot at ... $400,000"). Real math
    # never contains a 4+ letter lowercase word; ordinary prose almost always does. That one check is
    # a more reliable discriminator here than length or word-count, which both let real false positives
    # through during testing.
    if _LOWERCASE_WORD_RE.search(span):
        return False
    if ' ' not in span.strip():
        return len(span) <= 20
    return len(span) <= 40

def protect_math(text):
    spans = {}
    def stash(m):
        key = f"MATH{len(spans)}"
        spans[key] = m.group(1)
        return key
    return MATH_SPAN_RE.sub(stash, text), spans

def restore_math(html_body, spans):
    for key, original in spans.items():
        if looks_like_math(original):
            replacement = '\\(' + html.escape(original) + '\\)'
        else:
            # Not math -- almost always two unrelated dollar amounts on the same line that
            # got paired by mistake (an odd number of $ on one line pairs 1-2, 3-4, ... and
            # can straddle real prose in between). Run it through markdown's own inline
            # formatter rather than just escaping it, so any **bold**/*italic* that got
            # swallowed inside the accidental span still renders instead of showing as
            # literal asterisks -- this was extracted before the main markdown.markdown()
            # call ran, so without this it would never get formatted at all.
            inline_html = markdown.markdown(original.replace('\\$', '$'))
            if inline_html.startswith('<p>') and inline_html.endswith('</p>'):
                inline_html = inline_html[3:-4]
            replacement = inline_html
        html_body = html_body.replace(key, replacement)
    return html_body

def convert(md_path, pdf_path):
    text = pathlib.Path(md_path).read_text()
    text, math_spans = protect_math(text)
    html_body = markdown.markdown(text, extensions=['tables', 'fenced_code'])
    html_body = restore_math(html_body, math_spans)
    has_math = any(looks_like_math(s) for s in math_spans.values())
    # python-markdown renders ```mermaid as <pre><code class="language-mermaid">; mermaid.js
    # needs <div class="mermaid"> instead, so rewrite those blocks before printing.
    has_mermaid = 'language-mermaid' in html_body
    if has_mermaid:
        html_body = re.sub(
            r'<pre><code class="language-mermaid">(.*?)</code></pre>',
            lambda m: '<div class="mermaid">' + html.unescape(m.group(1)) + '</div>',
            html_body, flags=re.S)
    head = CSS + (MERMAID_JS if has_mermaid else "") + (MATHJAX_JS if has_math else "")
    doc = f"<!DOCTYPE html><html><head><meta charset='utf-8'>{head}</head><body>{html_body}</body></html>"
    html_path = str(pdf_path) + ".tmp.html"
    pathlib.Path(html_path).write_text(doc)
    try:
        cmd = [
            "/Applications/Google Chrome.app/Contents/MacOS/Google Chrome",
            "--headless", "--disable-gpu", "--no-pdf-header-footer",
            f"--print-to-pdf={pdf_path}", "--no-sandbox",
        ]
        if has_mermaid or has_math:
            # give the CDN script (mermaid.js and/or MathJax) time to load and render before printing
            cmd.append("--virtual-time-budget=10000")
        cmd.append(f"file://{html_path}")
        subprocess.run(cmd, check=True, capture_output=True)
    finally:
        pathlib.Path(html_path).unlink(missing_ok=True)
    print(f"Wrote {pdf_path}")

if __name__ == "__main__":
    convert(sys.argv[1], sys.argv[2])
