# Data Analysis for Management (XMBA 200S) — Deliverables Tracker

**Last verified against live Canvas:** 2026-10-23
**Sources:** `Block 1/Syllabus XMBA200S Fall 2026 - Walker.pdf` (class schedule, grading weights, final exam rules) + Canvas course 1555300 (assignment due dates, posted materials, announcements)

### How to read this file
- Every date below is **already converted to Pacific local time**. Canvas's own API reports deadlines in UTC, and naively quoting that UTC date is wrong — e.g. a Canvas `due_at` of `2026-10-01T06:59:59Z` is **Sept 30, 11:59:59 PM Pacific**, not Oct 1. You shouldn't need to do your own math.
- A deliverable's deadline does **not** line up with when its class happened. Several deadlines land *after* the block that taught the material is already over (right before the *next* block starts) — don't assume something is done just because the related classes are in the past.
- 🔴 = still open / not yet done. ✅ = deadline has passed. ❓ = mentioned in the syllabus but not yet posted to Canvas with real content or a date.

---

## 🔴 What's actually still open (as of 2026-10-23)

| Deliverable | Deadline | Counts toward | Confirmed? |
|---|---|---|---|
| **Assignment 6 — Home Prices Part 1** (in-class team exercise, Class 7) | **Sat Oct 24, 11:59pm** | In-Class Team Assignments: 10% | ✅ Canvas — now a graded assignment (10 pts), previously had no deadline set |
| **Assignment 7 — Home Prices Part 2** (in-class team exercise, Class 8) | **Sat Oct 24, 11:59pm** | In-Class Team Assignments: 10% | ✅ Canvas — newly posted 10/23 (10 pts) |
| **Final Exam** | **Fri Nov 13, 1:00–4:00pm** (in class) | 40% | ✅ Canvas + syllabus |
| Between-Block Team Assignment (Block 3→4) | Not yet posted | 40% *(Between-Block category, shared across all 3 of them — see note below)* | — |
| Knowledge Check — Block 4 | Not yet posted | Not graded | — |

**Note on the 40% Between-Block figure:** the syllabus states "Between-Block Team Assignments: 40%" as one category covering all of them (1→2, 2→3, 3→4) together — it does not say each individual one is worth 40% on its own. Treat that 40% as shared across the set, not per-assignment.

**Assignments 6 and 7 are a different category from the Between-Block assignments** — they're the in-class "Home Prices" team exercises from Class 7/Class 8 (worth 10 points each, under "In-Class Team Assignments," a separate 10%-weight category from the 40% Between-Block one). Both share the same Sat Oct 24, 11:59pm deadline even though they were introduced on different class days.

---

## Grading weights (by category)
| Component | Weight |
|---|---|
| Between-Block Team Assignments (all 3 combined) | 40% |
| Final Exam | 40% |
| In-class Team Assignments | 10% |
| Attendance & Participation | 10% |
| Knowledge Checks | Not graded — self-assessment only |

## Remaining class schedule
| # | Date | Time | Topic | Chapters / material |
|---|---|---|---|---|
| 7 | Thu 10/22 | 8:30–11:30am | The Simple Regression Model and Multiple Regression | Ch. 21, 23 — Wine Case (`Block 3/Wine Case.pdf`), read in advance; in-class "Housing Prices Part 1" team assignment (`Block 3/Class 7/`) |
| 8 | Fri 10/23 | 8:30–11:30am | Building Regression Models and Machine Learning | Ch. 23 Part 2, Ch. 24 — Wine Case discussion continues; Redfin article, "Home Prices Part 2" team assignment (`Block 3/Class 8/`) |
| 9 | Thu 11/12 | 1:00–4:00pm | Categorical Variables, Experimental Design, Wrap-up | Ch. 25 |
| 10 | Fri 11/13 | 1:00–4:00pm | **Final Exam** | — |

**Class 7 slides are up** (Chapter 21 + Chapter 23 Part 1, posted 10/22, in `Block 3/Class 7/`). **Class 8's slides are now also up** (Chapter 23 Part 2 + Chapter 24, posted 10/23, in `Block 3/Class 8/`), along with "Team Assignment 7 — Home Prices Part 2" (`Block 3/Class 8/Team Assignment 7 - Home Prices Part 2.docx`) — this turned out to be a genuinely new Part 2 assignment, not the "Solutions" to Class 7's Part 1 that had been expected; both "Team Assignment 6 — Home Prices Part 1" (Class 7) and "Team Assignment 7 — Home Prices Part 2" (Class 8) are now graded Canvas assignments due Sat Oct 24, 11:59pm (see the open-items table above).

**Final-exam prep materials posted 10/13**: a practice final exam and its solutions are in `Final Exam Prep/` (top-level, not block-specific) — open-book/notes but no computer/phone/electronic devices, same format as the real final.

## Final Exam — what to expect
| Field | Detail |
|---|---|
| Date/Time | Fri Nov 13, 1:00–4:00pm, in class |
| Format | Paper exam |
| Materials allowed | Open-book, open-note |
| Devices | None — no laptops, phones, or other devices |
| Collaboration | Individual — no communication with classmates during the exam |
| Weight | 40% of final grade |
| Source | Syllabus, confirmed |

---

## ✅ Already completed
Deadlines passed — for reference only, not action items.

| Deliverable | Deadline |
|---|---|
| Knowledge Check — Block 1 | Thu Sep 10 |
| In-class Assignment 1 (Airline Pricing) | Fri Sep 11 |
| In-class Assignment 2 (Unemployment Rate) | Sat Sep 12 |
| Between-Block Team Assignment (Block 1→2, "SentinelQA") | Wed Sep 30 |
| Knowledge Check — Block 2 | Thu Oct 1 |
| In-class Assignment 3 (Free Shipping Isn't Free) | Thu Oct 1 |
| **Between-Block Team Assignment (Block 2→3)** — "Team Assignment 2" | Wed Oct 22, 8:00am |
| Knowledge Check — Block 3 | Wed Oct 22, 8:00am |

---

## 🔴 Between-Block Team Assignment (Block 2→3) — full detail

| Field | Detail |
|---|---|
| Canvas name | "Team Assignment 2" |
| Deadline | Wed Oct 22, 8:00am Pacific |
| Posted | Oct 5, via Canvas announcement "Between Block Announcement (Block 2→Block 3)" |
| Submission | One zip file per group |
| Files | `Block 2/Between-Block 2 & 3/` — verified byte-for-byte identical to Canvas's official zip |

Three parts:

| Part | Title | What it covers |
|---|---|---|
| 1 | Pricing the Ridgeline Jacket | Fit a linear and a log-log regression of weekly unit sales vs. price for a fictional retailer's jacket; interpret the slope/elasticity; build a 95% prediction interval; advise on a proposed $95 price point |
| 2 | AI Consulting Experiment | Deeper follow-up to the in-class exercise (`Block 2/Class 5/`) — check whether randomization actually balanced treatment/control groups, measure treatment effects with two-sample t-tests, and reconcile a case where the AI group did better on average but *worse* on a planted "outside the frontier" task |
| 3 | Design Your Own Experiment | No dataset — design an original randomized experiment from scratch (sampling frame, level of randomization, stratification, non-compliance, number of outcomes/tests) |

All three require a team AI-use statement at the end, per the course's AI policy.

---

## 🔴 Home Prices Team Assignments (6 & 7) — full detail

| Field | Detail |
|---|---|
| Deadline (both parts) | Sat Oct 24, 11:59pm Pacific |
| Counts toward | In-Class Team Assignments: 10% (separate from the 40% Between-Block category) |
| Points | 10 pts each (20 pts combined) |
| Part 1 files | `Block 3/Class 7/Team Assignment 6 - Home Prices Part 1.docx` + `home_prices.csv` |
| Part 2 files | `Block 3/Class 8/Team Assignment 7 - Home Prices Part 2.docx` |
| Submission | Team, one per group (same pattern as other in-class team assignments) |

---

## ❓ Watch list — not posted yet, but expected
| Item | Status |
|---|---|
| Between-Block Team Assignment (Block 3→4) | No content or date yet |
| Knowledge Check — Block 3 / Block 4 | Ungraded self-assessments, typically posted just before each block |

Re-run the Canvas check (`haas-course-sync` skill) periodically to catch these — there's no fixed/predictable posting schedule based on what's been observed so far.
