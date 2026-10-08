import sys, subprocess, markdown, pathlib

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

def convert(md_path, pdf_path):
    text = pathlib.Path(md_path).read_text()
    html_body = markdown.markdown(text, extensions=['tables', 'fenced_code'])
    html = f"<!DOCTYPE html><html><head><meta charset='utf-8'>{CSS}</head><body>{html_body}</body></html>"
    html_path = str(pdf_path) + ".tmp.html"
    pathlib.Path(html_path).write_text(html)
    try:
        subprocess.run([
            "/Applications/Google Chrome.app/Contents/MacOS/Google Chrome",
            "--headless", "--disable-gpu", "--no-pdf-header-footer",
            f"--print-to-pdf={pdf_path}", "--no-sandbox",
            f"file://{html_path}"
        ], check=True, capture_output=True)
    finally:
        pathlib.Path(html_path).unlink(missing_ok=True)
    print(f"Wrote {pdf_path}")

if __name__ == "__main__":
    convert(sys.argv[1], sys.argv[2])
