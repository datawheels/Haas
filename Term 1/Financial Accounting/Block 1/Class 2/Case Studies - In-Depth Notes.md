# Class 2 Case Studies — In-Depth Notes (Balance Sheet & Income Statement Basics)

## Suggested study order
1. `Coffee Life story.docx` — meet the running company used across the entire term.
2. `Coffee Life - financial statements.xlsx` — the completed 2018/2019 BS, IS, CF statement, plus a "Connections" tab that maps how the three statements interlock.
3. `Sudoku challenge.docx` + `Sudoku challenge.xlsx` (template) + `Sudoku challenge completed.xlsx` (answers) — a self-contained puzzle, unrelated to Coffee Life, that forces you to internalize those same cross-statement identities without any statement being handed to you pre-built.

---

## 1. Coffee Life — the company behind every case this term

**The story:** Brianna and Candace Harris grew up in New Orleans and, after unfulfilling corporate jobs (Candace eventually earning a top MBA), opened a neighborhood café, Coffee Life, built around the warmth of their childhood home. It succeeded quickly and expanded. Three years in, a vacation to Ethiopia to learn about coffee's origins turned into a second business line: a large coffee-roasting facility that imports green beans from Ethiopia, roasts them into Coffee Life's signature blends, and sells the output both through the company's own (now 30+) café locations and to outside retail chains, cafés, and restaurants. The sisters co-CEO the company — Brianna the visionary, Candace the operator — and while Coffee Life remains **privately held** (funded by family savings plus outside capital from financial partners), management **prepares its financial statements as if it were public** and reviews them regularly with investors.

**Why this setup matters pedagogically, right from Class 2:** the "privately held but reports like a public company" framing is what licenses every later case in the term. It gives the course a single, continuous, GAAP-quality set of financial statements that can be revisited from a new angle each block — accounts receivable and revenue recognition (Class 3), inventory costing (Class 4), depreciation of the roasting machine (Class 5), and ultimately the cash flow statement (Class 7) — without ever having to introduce a new company or re-explain the business model. The two segments (cafés + roasting/wholesale) also matter concretely: the roasting segment is the one that carries inventory, extends credit to wholesale customers, and owns the depreciable equipment that later cases hinge on — the café segment is largely cash-and-carry retail and doesn't generate the same accounting complexity.

---

## 2. `Coffee Life - financial statements.xlsx` — the completed FY2018/FY2019 statements

This is the first fully-built instance of the three statements Coffee Life will use for the rest of the term. The point of Class 2 is simply to see how the Balance Sheet, Income Statement, and Cash Flow Statement **tie to each other** — the "Connections" tab is effectively the answer key to that question, and it's the logic every later Coffee Life file (and the Sudoku challenge below) quietly assumes you already understand.

### Balance Sheet ($'000)

| | FY2018 | FY2019 |
|---|---|---|
| Cash and cash equivalents | 432 | 500 |
| Accounts receivable, net | 3,108 | 3,579 |
| Inventory | 1,790 | 2,114 |
| Prepaid expenses and other current assets | 560 | 470 |
| **Total current assets** | **5,890** | **6,663** |
| PP&E, net | 10,340 | 12,075 |
| Other long-term assets | 450 | 479 |
| Intangible assets | 1,040 | 800 |
| Goodwill | 3,300 | 3,300 |
| **TOTAL ASSETS** | **21,020** | **23,317** |
| Accounts payable | 1,180 | 1,315 |
| Accrued liabilities | 1,710 | 1,911 |
| Deferred revenue, current | 735 | 890 |
| Short-term debt | 1,605 | 1,833 |
| **Total current liabilities** | **5,230** | **5,949** |
| Long-term debt | 7,500 | 8,000 |
| Other long-term liabilities | 1,500 | 1,500 |
| **Total liabilities** | **14,230** | **15,449** |
| Common stock and APIC | 1,100 | 1,100 |
| Retained earnings | 5,690 | 6,768 |
| **Total shareholders' equity** | **6,790** | **7,868** |
| **TOTAL LIABILITIES AND EQUITY** | **21,020** | **23,317** |

Every column balances exactly (`Check accounting equation` row = 0 on both sides) — the whole point of a balance sheet is that it *has* to. Note the ending-2019 retained earnings figure isn't an independent input: the spreadsheet computes it as `Beginning RE (5,690) + Net Income (2,328, from the Income Statement) + Cash dividends paid (−1,250, from the Cash Flow Statement) = 6,768`. This one formula is the single clearest illustration in the whole file of how the three statements physically connect through one account.

### Income Statement (FY2019, $'000, shares in '000)

```
Net sales                                22,350
Cost of sales                            (9,899)
Gross profit                             12,451
Sales and marketing expenses            (2,895)
New product development                   (679)
Store operating expenses                (2,450)
Depreciation and amortization expenses  (1,378)
General and administrative expenses       (987)
Other operating expenses                  (569)
Total operating expenses                (8,958)
Operating income                          3,493   (15.6% operating margin)
Interest expense                          (630)
Interest income and other                    25
Income before income taxes                2,888
Provision for income taxes                 (560)
Net income                                2,328
EPS (1,200 weighted avg. shares)            1.94
```

### Cash Flow Statement (FY2019, $'000) — built entirely from the BS/IS above

```
Net income                                   2,328   (= Income statement)
+ Depreciation and amortization              1,378   (= Income statement D&A line)
+ Other non-cash adjustments                     0
Δ Accounts receivable                        (471)   (= 2018 AR − 2019 AR: a $471 increase in AR is a cash outflow)
Δ Inventories                                (324)   (same logic: inventory grew, using cash)
Δ Accounts payable                             135   (AP grew: a source of cash)
Δ Other operating assets/liabilities           446   (prepaid ↓, accrued liab ↑, deferred rev ↑ — all cash-generating)
Net cash flow from operations (CFO)          3,492

Purchases of property                       (2,873)
Sales of property                                0
Net proceeds from other investments            (29)
Net cash flow from investing (CFI)          (2,902)

Proceeds from ST borrowings                  1,228
Repayments of ST borrowings                 (1,000)
Proceeds from LT borrowings                  4,000
Repayments of LT borrowings                 (3,500)
Cash dividends paid                         (1,250)
Net cash flow from financing (CFF)            (522)

Change in cash (CFO + CFI + CFF)                68
Beginning cash                                 432
Ending cash                                    500
```

Every "change in X" line in CFO/CFI is a live formula pulling the FY2018 vs. FY2019 balance sheet figures (e.g., `AR change = 2018 AR − 2019 AR`; an *increase* in an asset always shows up as a *use* of cash, and an *increase* in a liability always shows up as a *source*). The ending cash of $500K reconciles exactly back to the FY2019 balance sheet's cash line — closing the loop between all three statements.

### The "Connections" tab — the master map

The workbook includes a fourth tab that's really the answer key to the whole exercise, laid out as a set of parallel addition chains:

- **Beginning BS → Ending BS:** Cash + Other current assets + LT assets = Total assets; Current liabilities + LT liabilities = Total liabilities; Total liabilities + Common stock + Retained earnings = Total L&E; and **Total assets = Total liabilities + equity** on both the beginning and ending balance sheet.
- **Income Statement:** Revenue − Cost of revenue = Gross profit; Gross profit − Operating expenses = Operating profit; Operating profit − Non-operating expense/(income) = Pre-tax income; Pre-tax income − Taxes = Net income.
- **Cash Flow Statement:** Net income + Adjustments = Cash flow from operations; + Cash flow from investing + Cash flow from financing = Net change in cash; + Beginning cash = Ending cash.
- **Retained earnings roll-forward:** Beginning RE + Net income − Dividends = Ending RE.
- The tab spells out explicitly: *"The net income is the end of the IS and the beginning of the CF statement,"* *"The net income also affects the Retained earnings account on the BS,"* *"The cash on the beginning BS is the beginning cash on the CF statement,"* and *"The change in cash from the CF statement plus the beginning cash is equal to the ending cash on the BS."*

This map is exactly the toolkit needed to solve the Sudoku challenge below — it tells you which unknown cell can be derived from which other cells, and in what order.

---

## 3. The Sudoku challenge (separate exercise — not Coffee Life)

This is a stand-alone, self-contained puzzle: build a *different* fictional company's full BS/IS/CF statement set from a short list of scattered data points, with no pre-built statements to check against. It's called a "sudoku" because, like the number puzzle, most cells can't be filled directly — you have to work out a *solving order*, deriving each unknown from cells you've already pinned down, using exactly the identities from the Connections tab above.

### The given data
```
Revenue = 25,200                    Gross profit margin = 48%
AR = 2,500     Inventory = 3,500     Prepaid expenses = 700     LT investments = 3,000
AP = 30% of cost of revenue
LT debt = 2 × ST debt               Total current liabilities = 5,500
Operating expenses = 6,000          Non-operating expenses = 300     Tax rate = 21%
Prior period RE = 3,000             Dividends paid this period = 200
Beginning cash = 300                CF adjustment to net income = 320
Cash flow from investing = −5,000   Cash flow from financing = 750   (pre-populated)
Common stock = 2,200
```

### The solving order that actually works (from the completed answer key)

**Step 0 — the Income Statement first, because it's fully self-contained:**
```
Revenue                       25,200
Gross profit = 48% × 25,200   12,096
Cost of revenue = 25,200 − 12,096   13,104
Operating expenses            (6,000)
Operating income               6,096
Non-operating expenses          (300)
Pre-tax income                 5,796
Income taxes = 21% × 5,796    (1,217.16)
Net income                     4,578.84
```

**Step 0.5 — the Cash Flow Statement, because it now only needs Net Income (just solved) plus three given numbers:**
```
Net income                 4,578.84
+ Adjustments                  320
= Cash flow from operations 4,898.84
+ Cash flow from investing  (5,000)   (given)
+ Cash flow from financing     750    (given)
= Net change in cash          648.84
+ Beginning cash                300   (given)
= Ending cash                 948.84
```
This ending-cash figure is the one that later becomes the Cash line on the balance sheet — you cannot get Total Current Assets without it.

**Steps 1–4 — the liabilities and equity side of the balance sheet, using the given ratios:**
1. Accounts payable = 30% × Cost of revenue = 30% × 13,104 = **3,931.20**
2. Short-term debt = Total current liabilities − AP = 5,500 − 3,931.20 = **1,568.80**
3. Long-term debt = 2 × ST debt = 2 × 1,568.80 = **3,137.60**
4. Retained earnings = Prior RE + Net income − Dividends = 3,000 + 4,578.84 − 200 = **7,378.84**

**Step 5 — assemble Total Liabilities and Equity, which forces Total Assets via the accounting equation:**
```
Total liabilities  = Total current liabilities (5,500) + LT debt (3,137.60) = 8,637.60
Total L&E = Total liabilities (8,637.60) + Common stock (2,200) + RE (7,378.84) = 18,216.44
⟹ Total assets MUST also equal 18,216.44 (Assets = Liabilities + Equity, always)
```

**Steps 6–7 — back into the one asset nobody gave you directly (PP&E), by subtraction:**
```
Total current assets = Cash (948.84) + AR (2,500) + Inventory (3,500) + Prepaid (700) = 7,648.84
Total long-term assets = Total assets (18,216.44) − Total current assets (7,648.84) = 10,567.60
PP&E, net = Total LT assets (10,567.60) − LT investments (3,000) = 7,567.60
```
Balance-sheet check: 18,216.44 − 18,216.44 = 0. ✓

### The pedagogical point
PP&E is the one line item in this puzzle that **cannot be solved directly** — there is no clue that gives it to you. It can only be recovered by first nailing down *everything else* and then leaning on the one identity that always has to hold: Assets = Liabilities + Equity. That's the entire teaching purpose of framing this as a "sudoku": it trains you to (1) solve the Income Statement first whenever it's self-contained, (2) recognize that the Cash Flow Statement usually only needs Net Income plus a couple of given lines, and (3) treat the accounting equation not as a check you run *after* building the balance sheet, but as an active tool you use *to build* the balance sheet when a piece is missing. It's the exact same "which cells can I fill, and in what order" logic the Connections tab in the Coffee Life file lays out — just with no completed statement to peek at.

---

## Cross-cutting themes
1. **The three statements are one interlocked system, not three independent documents.** Net income flows from the IS into both the CF statement (its starting line) and the BS (through retained earnings); the CF statement's beginning/ending cash must tie to the BS cash line in both periods; and Assets = Liabilities + Equity is not a "check" performed at the end — it's often the only way to solve for a missing number.
2. **Balance sheet changes drive most of the Cash Flow Statement.** Every "change in AR / inventory / AP / etc." line in CFO is nothing more than the difference between two balance-sheet snapshots — a theme that reappears explicitly and in far more depth in Classes 3, 4, and 5 (AR, inventory, and PP&E are exactly the accounts singled out here).
3. **Not every unknown can be solved "forwards."** Some figures (PP&E in the Sudoku challenge) only fall out once you've solved everything else and then applied the accounting equation in reverse — a habit of mind worth building now, because later Coffee Life cases (e.g., Class 3's AR schedule, which has to tie back to a previously reported net-AR figure) reuse the same "solve everything solvable, then force the final number to reconcile" logic.
4. **Coffee Life's "reports like a public company" framing is a deliberate setup, not incidental color.** It's what allows every subsequent class this term to treat Coffee Life's financial statements as a known, trustworthy baseline and build one new topic on top of them at a time.
