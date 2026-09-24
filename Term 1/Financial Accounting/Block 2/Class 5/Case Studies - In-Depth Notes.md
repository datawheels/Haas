# Class 5 Case Studies — In-Depth Notes (Long-Term Assets / Depreciation)

## Suggested study order
1. `Coffee Life Roasting machine.docx` — the story and the questions Erica needs answered.
2. `Coffee Life - roasting machine depreciation schedule.xlsx` — the blank SL/DDB schedule (two sheets: a 5-year and an 8-year useful-life version).
3. `Coffee Life - roasting machine depreciation schedule - completed.xlsx` — the full worked schedule, including the equipment sale.

---

## 1. The story: a depreciation-method proposal, and later a real equipment sale

Coming back from Ethiopia in spring 2016, Brianna and Candace moved fast on the new roasting business — by year-end, staff were hired, a location secured, and the roasting equipment ordered. **The machine cost $2.2M** (including shipping and installation). The manufacturer's recommended useful life was five to eight years; Coffee Life's accounting team **chose the conservative end — five years — with a $0.2M residual (salvage) value**, and depreciates all fixed assets on the **straight-line method**. The machine went into service in January 2017.

Some time later, Erica attends a professional conference and comes back excited about "effective tax management" — she wants to propose to the executive team that Coffee Life **switch from straight-line to double-declining balance (DDB)** depreciation. To prepare her for that pitch, the case asks:
1. What is the depreciation expense each year under straight-line?
2. What is the depreciation expense each year under double-declining balance?
3. Is DDB actually better than straight-line *for tax purposes*?

**The second half of the story, set in 2020:** Brianna, a committed environmentalist, hears about a zero-emissions coffee roaster and wants to replace the existing machine. It's well maintained, and the maintenance contractor estimates its **sale price at $1.2M**. The case then asks you to work out the income-statement and cash-flow effect of that sale — first assuming straight-line depreciation had been used throughout, then assuming DDB had been used instead.

## 2. Straight-line depreciation — the baseline

```
Depreciable base = Cost (2,200,000) − Salvage (200,000) = 2,000,000
Annual SL depreciation = 2,000,000 / 5 years = 400,000/year, flat, for 2017–2021
```

| Year | Beg. NBV | Depreciation | Accum. Dep. | End NBV | Tax shield (21%) |
|---|---|---|---|---|---|
| 2017 | 2,200,000 | 400,000 | 400,000 | 1,800,000 | 84,000 |
| 2018 | 1,800,000 | 400,000 | 800,000 | 1,400,000 | 84,000 |
| 2019 | 1,400,000 | 400,000 | 1,200,000 | 1,000,000 | 84,000 |
| 2020 | 1,000,000 | 400,000 | 1,600,000 | 600,000 | 84,000 |
| 2021 | 600,000 | 400,000 | 2,000,000 | 200,000 | 84,000 |
| **Total** | | **2,000,000** | | | **420,000** |

End-of-life NBV lands exactly on the $200,000 salvage value, as it must under straight-line.

## 3. Double-declining balance — the accelerated alternative

DDB applies a fixed rate of **2 / useful life = 2/5 = 40%** to the *beginning* net book value each year (not to the depreciable base), and is not allowed to depreciate the asset below its salvage value:

```
2017: 2,200,000 × 40% = 880,000   → End NBV 1,320,000
2018: 1,320,000 × 40% = 528,000   → End NBV   792,000
2019:   792,000 × 40% = 316,800   → End NBV   475,200
2020:   475,200 × 40% = 190,080   → End NBV   285,120
2021: formulaic 40% would give 114,048, which would push NBV to $171,072 —
      BELOW the $200,000 salvage floor. So the final year is "plugged":
      Depreciation = 285,120 − 200,000 = 85,120   → End NBV exactly 200,000
```

| Year | Depreciation (DDB) | Tax shield (21%) |
|---|---|---|
| 2017 | 880,000 | 184,800 |
| 2018 | 528,000 | 110,880 |
| 2019 | 316,800 | 66,528 |
| 2020 | 190,080 | 39,916.80 |
| 2021 | 85,120 (plug to salvage floor) | 17,875.20 |
| **Total** | **2,000,000** | **420,000** |

**The key observation:** the **total** depreciation ($2,000,000) and the **total** tax shield ($420,000) over the full five years are *identical* under SL and DDB — only the *timing* differs. DDB front-loads $184,800 + $110,880 + $66,528 = **$362,208** of tax shield into 2017–2019 alone, versus SL's $84,000 × 3 = $252,000 over the same three years — pulling forward an extra **$110,208** of tax benefit.

**Answering Erica's Question 3 — is DDB "better" for tax purposes?** Not in total-dollar terms — the lifetime tax bill is exactly the same either way, since both methods eventually depreciate the full $2,000,000 base. What DDB actually buys is a **timing advantage**: getting the deduction sooner is worth more than getting it later, purely because of the time value of money. That's the argument Erica should actually bring to the executive team — not "we'll pay less tax," but "we'll pay the same tax, later."

## 4. The 2020 equipment sale — where the method choice comes back to bite (or not)

The machine is sold in 2020 for **$1.2M**, using the **end-of-2019 net book value** as the basis for the gain/loss calculation (i.e., the sale is evaluated as of the start of 2020, before that year's depreciation is taken):

**Under straight-line** (the method Coffee Life actually used):
```
NBV at end of 2019 = 1,000,000
Gain on sale = 1,200,000 − 1,000,000 = 200,000
Tax owed on gain = 21% × 200,000 = 42,000
Net cash proceeds = 1,200,000 − 42,000 = 1,158,000
```
This $200K gain is exactly the figure later referenced as fact in the Class 7 cash-flow story ("the sale resulted in a gain of $200K") — confirming that straight-line is the method Coffee Life's real books actually used.

**Under DDB (hypothetically, "what if"):**
```
NBV at end of 2019 = 475,200   (far lower — DDB had already expensed much more by 2019)
Gain on sale = 1,200,000 − 475,200 = 724,800
Tax owed on gain = 21% × 724,800 = 152,208
Net cash proceeds = 1,200,000 − 152,208 = 1,047,792
```
DDB produces a *much bigger* taxable gain at sale — and therefore *lower* net proceeds from the sale itself ($1,047,792 vs. $1,158,000) — precisely because DDB had already "used up" more of the asset's tax shield in the earlier years, leaving a smaller book value to offset the sale price against.

**The reconciling punchline — total cash benefit through the point of sale is identical either way:**
```
SL:  Net sale proceeds (1,158,000) + cumulative 2017–2019 tax shield (84,000 × 3 = 252,000) = 1,410,000
DDB: Net sale proceeds (1,047,792) + cumulative 2017–2019 tax shield (184,800+110,880+66,528 = 362,208) = 1,410,000
```
Exactly equal. This is the cleanest possible demonstration that **depreciation method is a cash-flow *timing* decision, not a total-value decision.** Accelerated depreciation shifts tax benefit earlier in exchange for a bigger taxable gain (and correspondingly smaller net proceeds) if the asset is sold before the end of its useful life — but the combined total, across the full holding period, doesn't change.

## 5. A second lever: the useful-life estimate itself (the 8-year comparison sheet)

The workbook also includes a full 5-year vs. 8-year comparison. Spreading the *same* $2,000,000 depreciable base over 8 years instead of 5 drops straight-line depreciation to **$250,000/year** instead of $400,000/year — a **$150,000/year** difference. Coffee Life deliberately chose the **shorter, more conservative** end of the manufacturer's 5–8 year recommended range, which means **higher near-term depreciation expense and lower near-term reported profit** than a peer company using the longer estimate — a judgment call made well before the SL-vs-DDB method question ever comes up, and consistent with the story's description of Coffee Life's accounting team as deliberately conservative.

## Why this case was chosen for the Long-Term Assets / Depreciation topic
The roasting-machine case bundles three distinct judgment calls that all affect reported profit without changing the underlying economics one dollar: **(1)** the useful-life estimate (5 vs. 8 years, both within the manufacturer's own recommended range); **(2)** the depreciation method (straight-line vs. double-declining balance); and **(3)** what happens when a depreciated asset is sold before the end of that assumed life — where the earlier method choice mechanically determines the size of the gain (and the tax due) at the moment of sale. The case is built so all three lessons converge on the same conclusion: none of these choices change how much cash Coffee Life ultimately collects and how much tax it ultimately pays over the asset's full life — they only change *when* the profit, the tax shield, and the cash show up. That distinction — timing vs. total value — is the single most important idea in the depreciation topic, and the case makes it land by forcing you to compute the "total plus tax shield" reconciliation and watch both methods arrive at the identical $1,410,000.
