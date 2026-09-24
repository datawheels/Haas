# Class 3 Case Studies — In-Depth Notes (Accounts Receivable & Payable, Revenue Recognition)

## Suggested study order
1. `Coffee Life Accounts receivable.docx` — the story and the two questions Erica needs answered.
2. `Coffee Life Accounts receivable - template.xlsx` — the blank schedule (a "simple example" tab plus the real Coffee Life template).
3. `Coffee Life Accounts receivable - with answers.xlsx` — the completed schedule, which ties directly back to the FY2019 balance sheet and income statement built in Class 2.

---

## 1. The story: Erica Johnson and Coffee Life's credit-risk problem

Erica Johnson met the Harris sisters as a college senior at a networking event for Black-owned businesses; she joined Coffee Life looking for her first accounting job and, by 2020, leads its entire accounting function — revenue recognition, the allowance for doubtful accounts, inventory costing, and depreciation schedules all run through her.

Coffee Life's **roasting/wholesale segment** sells to outside retail chains, cafés, and restaurants on credit, which exposes the company to credit risk. To manage it, Coffee Life maintains a **reserve for uncollectable accounts** (the allowance for doubtful accounts), sized differently by customer type:
- **Small vendors:** a flat **3% of credit sales** is reserved, regardless of aging.
- **Large vendors:** the company keeps an **aging schedule** and reserves a higher percentage the further past due a balance is.

**The task for FY2019:** using the data Erica collected — a $160K write-off during the year, $9,331K of new credit sales, $8,660K of cash collected, $4,700K of those credit sales attributable to small vendors, and an aging schedule for large-vendor balances — determine (1) the required allowance for uncollectable accounts, (2) the year-end gross and net AR balances, and (3) the bad debt expense for the year.

**The forward-looking twist:** by late 2020, COVID-19 has hit some of Coffee Life's wholesale customers hard — some have closed permanently, others are struggling to pay. Erica now believes closer to **7%** (not 3%) of small-vendor AR might go uncollected, and the case asks two "what if" questions: how would the FY2019 financial statements have looked if Erica had known about the pandemic and reserved for it in advance, versus if she had recorded *no* reserve at all?

---

## 2. Warm-up: the "AR simple example" tab — learning the two distinct mechanics first

Before tackling Coffee Life's real numbers, the answer key includes a small, made-up numerical warm-up that isolates the two *separate* events that touch the allowance account, because they're easy to conflate:

```
Beginning:          Gross AR 100,000   |  Reserve 100    |  Net AR 99,900

Event A — re-estimating the required reserve (a P&L event):
  Reserve needed = 2% × 100,000 = 2,000
  Increase in reserve = 2,000 − 100 = 1,900  →  this IS the bad debt expense
  After this event:   Gross AR 100,000  |  Reserve 2,000  |  Net AR 98,000

Event B — writing off a specific $1,000 balance (a balance-sheet-only reclassification):
  Gross AR falls by 1,000  →  99,000
  Reserve falls by the SAME 1,000 →  1,000
  Net AR: 99,000 − 1,000 = 98,000   ← UNCHANGED by the write-off
```

**The point of this warm-up:** a write-off never touches net AR or the income statement — it simply removes a specific balance from *both* gross AR and the reserve by the same amount, because the loss was already anticipated (reserved for) earlier. Only *changing the size of the required reserve* creates bad debt expense. Students who don't separate these two mechanics tend to double-count the loss (once through the reserve estimate, again through the write-off) or assume a write-off hurts current-period profit — it doesn't; the profit hit already happened when the reserve was originally built up.

---

## 3. The real Coffee Life AR schedule — full walkthrough

### Opening position (end of FY2018 / beginning of FY2019)
```
Gross AR    3,298
Allowance    (190)
Net AR      3,108        ← matches the FY2018 balance sheet net-AR figure from Class 2
```

### Step 1 — record the actual $160K write-off
A write-off reduces gross AR *and* the allowance by the same amount — net AR is unaffected (exactly the mechanic from the warm-up above):
```
Gross AR:    3,298 − 160 = 3,138
Allowance:     190 − 160 =    30
Net AR:      3,138 −  30 = 3,108   (unchanged, as expected)
```

### Step 2 — layer on the year's new credit sales and collections
```
Gross AR = 3,138 + New credit sales (9,331) − Collections (8,660) = 3,809
Allowance = 30 (unchanged — collections/new sales don't touch the reserve estimate)
Net AR = 3,809 − 30 = 3,779
```

### Step 3 — determine the *required* allowance as of year-end, using the two policies
**Small vendors — flat 3%:**
```
Required allowance = 3% × Credit sales to small vendors (4,700) = 141
```
**Large vendors — aging schedule:**
| Bucket | Balance | % uncollectable | Required allowance |
|---|---|---|---|
| Current AR | 1,200 | 0% | 0 |
| 30 days late | 700 | 2% | 14 |
| 60 days late | 500 | 7% | 35 |
| >60 days late | 200 | 20% | 40 |
| **Total (large vendors)** | | | **89** |

```
Total required allowance = Small vendors (141) + Large vendors (89) = 230
```

### Step 4 — the required allowance sets the bad debt expense
```
Required allowance                230
Existing allowance (from Step 2)  (30)
Difference = Bad debt expense      200
```
This $200K bad debt expense is a genuine income-statement charge for FY2019 — the reserve simply wasn't big enough given the actual sales mix and aging profile, so it has to be topped up.

### Step 5 — the year-end AR balances tie exactly back to the FY2019 balance sheet
```
Gross AR (year-end)   3,809
Allowance (year-end)    230
Net AR (year-end)     3,579   ← this is EXACTLY the FY2019 net-AR figure on Coffee Life's balance sheet (Class 2)
```
This is the single most satisfying moment in the exercise: after five steps of building the schedule from scratch, you land precisely on the same $3,579K net-AR figure that was simply *given* as a completed balance-sheet line in Class 2. The case reverse-engineers a number you'd previously taken on faith.

### Step 6 — the bad debt expense flows through to gross profit, and *that* also ties out
```
Sales                                    22,350
Cost of sales, excluding bad debt exp.   (9,699)
Bad debt expense                          (200)
Gross profit                             12,451    ← matches the Class 2 income statement exactly
Gross profit margin                       55.7%
```
Without knowing to include the $200K bad debt expense as part of cost of sales, you'd compute a gross profit of $12,651K and a margin of 56.6% — both wrong, and both a full percentage point off from the actual reported figures.

---

## 4. The COVID "fast forward" — how the choice of reserve reshapes reported profit across periods

The case's closing discussion (echoed directly in the answer key's notes) asks you to reason through three scenarios for the small-vendor reserve rate:

1. **If Erica had known in 2019 that ~7% (not 3%) of small-vendor AR would eventually be uncollectable** and reserved accordingly: FY2019 bad debt expense — and therefore FY2019 profit — would have been **lower** than what was actually reported. FY2020's profit impact then depends entirely on how accurate that forward-looking estimate turns out to be.
2. **If she had reserved *too much*** in anticipation of the pandemic: FY2019 profit would be lower than actual, but FY2020 profit would end up **higher** than it otherwise would, because less additional reserve-building would be needed once 2020's real losses materialize.
3. **If she had recorded no reserve at all** in 2019: FY2019 profit would look **higher** (no bad debt expense drag), but FY2020 profit would very likely be **lower**, once the accounts that go bad in 2020 have to be written off (or newly reserved for) with no cushion already built.

## Why this is the case chosen to teach AR / revenue recognition

This case is built to make three points land at once, using genuinely realistic mechanics rather than a toy example:
1. **The allowance for doubtful accounts is a *judgment estimate*, not a fact** — and the case shows concretely how that judgment (3% flat vs. an aging-based sliding scale) directly determines a real income-statement number (bad debt expense) and a real balance-sheet number (net AR).
2. **Write-offs and reserve re-estimation are mechanically distinct events** that both live inside the same allowance account — conflating them is the single most common error, which is exactly why the answer key includes the "simple example" warm-up before the real numbers.
3. **The forward-looking discussion is a soft introduction to earnings management and estimate timing** — the same $ of eventual bad debt can be recognized earlier (hurting this year, helping next year) or later (helping this year, hurting next year), purely by choice of assumption, with no change to the underlying economics. That tension — the temptation to under-reserve to protect current profit, versus the conservative instinct to reserve ahead of a known risk like COVID-19 — is the real-world issue lurking behind every allowance-for-doubtful-accounts number reported on any company's balance sheet.
