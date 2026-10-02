---
name: haas-course-sync
description: Use this skill whenever the user is working in the Haas EMBA course-notes repo and asks to (a) check Canvas/bCourses for newly posted class materials, (b) write or catch up "Theory Notes" and "Case Studies - In-Depth Notes" for classes that are missing them, (c) push the repo to git, or (d) sync the repo to Google Drive. Trigger on phrases like "check canvas", "anything new on bcourses", "did new stuff get posted", "write notes for class X", "catch up the notes", "push to git", "sync to drive", or "push to git and drive" — even if the user doesn't name all four steps explicitly, since these are usually run together or in sequence. Also use this skill to figure out course IDs, the Canvas API token location, or which classes still need notes.
---

# Haas course-notes sync

This repo (`/Users/gulsher/Documents/Projects/Haas`) is the user's personal archive of EMBA course materials, organized `Term 1/<Course>/Block N/Class N/`. This skill captures a four-part workflow that's been run repeatedly against it: pull new files down from Canvas, write study notes for classes that don't have them yet, commit/push to GitHub, and mirror the folder into Google Drive. Each part is independent — run whichever one(s) the user actually asked for, not all four by default.

## 0. Shared context

**Canvas credentials** live in `context/.env` (gitignored) — `CANVAS_TOKEN` and `CANVAS_BASE_URL` (`https://bcourses.berkeley.edu/`). Source it with `set -a && source context/.env && set +a` before any `curl`.

**Course IDs** (fetch fresh via `GET api/v1/courses?enrollment_state=active&per_page=100` if these ever stop resolving — course IDs can change term to term):
| Course | Canvas course ID |
|---|---|
| Data Analysis for Management | 1555300 |
| Managerial Economics | 1555302 |
| Financial Accounting | 1554935 |

**Why these specific IDs and not a generic "find my courses" step each time**: resolving them once and hardcoding saves an API round-trip every run; just re-verify with the endpoint above if a 404 suggests the term rolled over.

---

## 1. Check Canvas for new materials

Each course's content lives on one Canvas "page" per block (slug `block-1`, `block-2`, ...), linked from a module called "Block Materials". The reliable way to find everything a student can actually see is to scan these page bodies for `/files/<id>` references — Canvas's own file-listing API (`/courses/{id}/files`) is usually blocked for students, so don't rely on it.

**Steps:**
1. For each course, list its pages via the module items (`GET /courses/{cid}/modules?include[]=items`), then fetch each block page body (`GET /courses/{cid}/pages/{slug}`).
2. Regex out every `/files/(\d+)` reference across all block pages for that course. Also check `GET /courses/{cid}/assignments` and read each assignment's `description` field the same way — problem sets and other graded work often link files there instead of on the block page, and are easy to miss if you only scan pages.
3. Resolve each file ID to a name via `GET /courses/{cid}/files/{id}` (gives `display_name` and `updated_at`). **Do this with a single Python script using `urllib.request` in a loop, not a bash loop that shells out to `curl | python3` per file** — the per-process spawn overhead compounds badly once you're past ~20 files and the command will stall past a tool timeout. A plain Python loop over ~100 IDs finishes in a couple of seconds.
4. Compare resolved names against what's on disk under `Term 1/<Course>/`. **Normalize both sides before comparing** — lowercase, strip smart quotes/apostrophes/question-marks, strip all non-alphanumeric characters — because filenames that crossed through different downloads often differ only in how a curly quote or em-dash got encoded (e.g. a title's `'` becomes `?` in one copy and `'` in another). A naive exact-match comparison produces a wall of false "missing" positives. Example normalizer:
   ```python
   import re, unicodedata
   def norm(s):
       s = unicodedata.normalize('NFKD', s).lower()
       s = re.sub(r"[‘’“”'\"?]", '', s)
       return re.sub(r'[^a-z0-9]+', '', s)
   ```
5. For anything genuinely new (no normalized match locally), figure out which Class folder it belongs to by reading the surrounding text on the block page (the class heading it falls under) or the corresponding `class.md`, then download it there:
   ```bash
   curl -s -L -H "Authorization: Bearer $CANVAS_TOKEN" \
     "${CANVAS_BASE_URL}courses/<cid>/files/<id>/download?download_frd=1" \
     -o "Term 1/<Course>/Block N/Class N/<display_name>"
   ```
6. If a "new" file is a `.zip`, download and `unzip -l` it before committing to it — it's often just a convenience bundle of files already downloaded individually under the same names. Skip it if so; no need to keep a duplicate zip around.
7. Report back what's genuinely new vs. what turned out to be a repackaged duplicate, and which class folder each new file was dropped into. Don't silently skip reporting items you decided were duplicates — say so, since that's the judgment call most likely to be wrong.

**Known false-positive traps**: smart-quote/em-dash mangling (handled by the normalizer above), and zipped re-bundles of already-downloaded content (handled by step 6).

---

## 2. Write Theory Notes and Case Studies notes

The target format is two files per class:
- **`Theory Notes.md`** — a deep summary of that class's lecture slides, cross-referenced with any assigned textbook/lecture-note pages, working every formula through with actual numbers rather than describing it abstractly.
- **`Case Studies - In-Depth Notes.md`** — deep analysis of the case PDFs/articles assigned for that class, explicitly answering every discussion question the course's `class.md` lists for each one, and tying the analysis back to the Theory Notes' concepts.

**The canonical style template** — read these before writing anything, and match their density, structure, and voice:
- `Term 1/Data Analysis for Management/Block 1/Class 3/Chapter 15 - Theory Notes.md`
- `Term 1/Data Analysis for Management/Block 1/Class 3/Case Studies - In-Depth Notes.md`

Both are dense and numbers-driven (work examples through to a final value, don't just name the formula), close with a "Cross-cutting themes" or "Punchline" section, and the Theory Notes file ends with an empty placeholder:
```markdown
## Gulsher questions (along with clarification)

*(none yet — add here when you have follow-up questions on this chapter)*
```
Keep that placeholder — it's where the user logs their own follow-up questions later, and it's a convention worth preserving across every new file rather than reinventing a different closing section each time.

**Before writing, check whether notes are actually missing** — don't regenerate files that already exist. Each course has a different baseline, worked out by actually inspecting what's already there rather than assuming:
- **Data Analysis for Management**: most Block 1 classes already have both files. Check each Class folder for existing `Theory Notes.md` / `Chapter N - Theory Notes.md` and `Case Studies - In-Depth Notes.md` before touching it. If a class has no lecture-slide PDF posted yet (check `class.md` — it'll say "slides not posted yet"), skip the Theory Notes for that class rather than inventing content from thin air; a Case Studies note built from whatever case material *does* exist (e.g. a standalone case PDF) is still worth writing.
- **Financial Accounting**: per-topic `Summary Notes - <Topic>.docx` files already serve as the theory-notes equivalent for every class — **do not** create a parallel `Theory Notes.md` for this course unless the user explicitly asks for one; it would just duplicate existing material in a different format. Only add `Case Studies - In-Depth Notes.md`, and only for classes that actually have a case example (most classes carry a running "Coffee Life" case — story `.docx` + template/answers `.xlsx`). If a class has no case example at all (check for Coffee Life or similar files alongside the Summary Notes docs), there's nothing to write notes about — skip it.
- **Managerial Economics**: as of the last pass, this course had no notes at all and needed both files for every class. Re-check before assuming that's still true.

**Reading source files**: PDFs read fine directly. `.docx`/`.xlsx`/`.pptx` need a workaround since the Read tool can't open them:
- `.docx`: `python3` + `zipfile` + regex-stripping `word/document.xml`, or `python-docx` if installed.
- `.xlsx`: `openpyxl` (dump both `values` and `formulas` across every sheet, including less-obvious secondary sheets — answer keys sometimes hide a "simple example" or "comparison" tab that matters for understanding the main one).
- If a PDF slide deck reads back empty or as an image placeholder, it's image-rendered rather than text-layer — re-read it in smaller page batches or fall back to a PDF-to-text tool (`pypdf`) rather than concluding there's nothing in it.

**Cite exact numbers from the source**, not paraphrases — if a spreadsheet's completed answer key shows a specific depreciation schedule or a case PDF states a specific survey result, walk through those real numbers the way the template does, and verify a few cross-file tie-outs where plausible (e.g. a number derived in one class's notes should match a number asserted in a later class's story text, if they're part of the same running case).

**For a big backlog** (multiple courses/blocks missing notes at once), split the work across background agents by course or block rather than writing everything inline — each agent should get: the exact template files to read first, the specific source files for its classes, the per-course inclusion rule above, and an explicit list of what's out of scope (so two agents don't both touch the same class). Confirm scope with the user first if it's ambiguous which classes should get notes (e.g. a course with its own pre-existing note format, like Financial Accounting's Summary Notes) — don't assume full-course coverage is wanted without checking.

---

## 3. Commit and push to git

Standard flow, with two things worth being deliberate about:
- **Stage files by name**, not `git add -A` — review `git status` first, since the working tree may contain the user's own in-progress homework or drafts that showed up between sessions (not created by this skill). Those are fine to include in the same commit (they're legitimate repo content, not secrets) — skim them for anything sensitive first — but exclude obvious duplicates (e.g. a zip someone extracted locally that duplicates an already-tracked folder) rather than committing bloat.
- **Confirm before pushing** — `origin` is a real shared GitHub remote (`github.com/datawheels/Haas`), so treat `git push` as the kind of action to check in on before running, even though `git commit` locally doesn't need that. Once the user has said "push" in the current conversation, later pushes in the same session don't need re-confirming — but a session's first push does.

Commit message: short, states what changed and *why* (new Canvas materials arrived / notes backlog filled / etc.), not a file-by-file list. End with:
```
Co-Authored-By: Claude Sonnet 5 <noreply@anthropic.com>
```

---

## 4. Sync to Google Drive

There is no authorized Google Drive *connector* in this environment (it needs an interactive OAuth flow this harness can't run) — don't try to use Drive MCP tools here, they'll fail or aren't loaded. Instead, Google Drive for Desktop is installed and already mirroring part of this repo locally, so a plain filesystem copy does the job:

```bash
rsync -av "/Users/gulsher/Documents/Projects/Haas/Term 1/" \
  "/Users/gulsher/Library/CloudStorage/GoogleDrive-gulsher@berkeley.edu/My Drive/Haas/Term 1/" \
  --exclude ".DS_Store"
```

**Never add `--delete`** — the Drive-side copy may hold things that were put there directly (outside this repo) and aren't tracked locally; a mirror sync should only ever add/update, never remove. Google Drive for Desktop picks up the change and syncs it up automatically once the local copy is written — no further action needed.

If this folder ever stops existing at that path (e.g. the user resets their Drive sync), locate it fresh: `ls ~/Library/CloudStorage/` will show the mounted account folder name, which may differ from `GoogleDrive-gulsher@berkeley.edu` if the account changes.

**A Drive *folder link/URL* the user pastes (e.g. `drive.google.com/drive/folders/...`) is a different thing** from this sync target — it points at a specific Drive item by ID, which may or may not be anything under "My Drive" or locally synced. Don't assume it's reachable via the rsync path above. If asked to open/read such a link: a plain `WebFetch` will just hit a Google login wall (it's not public), so instead resolve the folder ID locally against Drive for Desktop's own sync database before concluding it's inaccessible:
```bash
DB=$(find ~/Library/"Application Support"/Google/DriveFS -name mirror_metadata_sqlite.db | head -1)
sqlite3 "$DB" "SELECT stable_id, id, local_title, is_folder, trashed FROM items WHERE id = '<FOLDER_ID_FROM_URL>';"
```
This confirms the folder's name and whether it's trashed even when it isn't materialized on disk (e.g. it's "Shared with me" but not added to "My Drive" — which Drive for Desktop only mirrors to a real local path once the user adds it). If it's not locally synced, say so plainly and point the user at adding it to "My Drive" (or authorizing the Drive connector) rather than guessing at its contents.
