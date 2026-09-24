# Class 4 Case Studies — In-Depth Notes (COGS & Inventory)

## Suggested study order
1. `Coffee Life Inventory.docx` — the story and the four questions Erica needs to answer.
2. `Coffee Life Inventory - template.xlsx` — the blank production/sales schedule.
3. `Coffee Life Inventory - with answers.xlsx` — the completed LIFO/FIFO comparison, the "delay production" what-if, and the inventory-audit write-off.

---

## 1. The story: LIFO, rising coffee prices, and a margin gap Erica has to explain

Most of Coffee Life's inventory sits in the roasting segment: the company buys green beans (increasingly expensive, as severe weather has hit Ethiopia and other major coffee-growing regions) and roasts them domestically, capitalizing all production costs into inventory. **Coffee Life accounts for inventory under LIFO** (last-in, first-out); Erica maintains a batch-by-batch production-cost ledger and uses it to compute COGS each period.

At quarter-end, management reviews performance against peers — and Erica is worried: **Coffee Life's gross margin is declining, and its peers (who use FIFO) are outperforming it**, even though the underlying driver (rising coffee prices) is the same for everyone. She's asked to:
1. Calculate COGS and ending inventory under Coffee Life's actual method (LIFO).
2. Calculate what COGS and ending inventory *would have been* under FIFO (the peers' method) — same production, same sales.
3. Explain the recent underperformance relative to peers.
4. Decide whether to recommend switching from LIFO to FIFO.
5. Assess a real decision she almost made: when coffee prices spiked in March, she considered pausing production for the last three batches, then decided against it — was that a mistake?
6. Handle an inventory-audit finding: five 10 lb. bags are missing and need to be written off.

## 2. The production and sales data (Q1 2020, through March)

Eleven production batches, at steadily rising cost per 10 lb. bag:

| Batch | Bags | Cost/bag |
|---|---|---|
| Date 1 | 35,000 | $19.50 |
| Date 2 | 25,000 | $22.00 |
| Date 3 | 15,000 | $22.50 |
| Date 4 | 15,000 | $23.10 |
| Date 5 | 10,000 | $25.20 |
| Date 6 | 15,000 | $26.00 |
| Date 7 | 15,000 | $26.10 |
| Date 8 | 15,000 | $26.00 |
| Date 9 | 13,000 | $27.50 |
| Date 10 | 20,000 | $27.80 |
| Date 11 | 12,000 | $29.00 |
| **Total produced** | **190,000** | |

Sales for the quarter: **90,000 bags at an average price of $60/bag → $5,400K of revenue** (same for every costing method — revenue doesn't depend on inventory accounting).

## 3. LIFO vs. FIFO — the full calculation, side by side

**Under LIFO** ("last produced, first expensed"): the 90,000 bags sold are assumed to be the *most recently produced* units — Dates 6–11 (15,000+15,000+15,000+13,000+20,000+12,000 = 90,000 bags exactly). Ending inventory is what's left: the *oldest* 100,000 bags, Dates 1–5.
```
COGS (LIFO)       = Σ(Dates 6–11 qty × cost) = $2,433.0K
Ending inv. (LIFO) = Σ(Dates 1–5 qty × cost) = $2,168.5K
Gross profit (LIFO) = 5,400 − 2,433 = $2,967.0K   → margin 54.9%
```

**Under FIFO** ("first produced, first expensed"): the 90,000 bags sold are assumed to be the *earliest* units — Dates 1–4 (35,000+25,000+15,000+15,000 = 90,000 bags exactly). Ending inventory is the *newest* 100,000 bags, Dates 5–11.
```
COGS (FIFO)        = Σ(Dates 1–4 qty × cost)  = $1,916.5K
Ending inv. (FIFO) = Σ(Dates 5–11 qty × cost) = $2,685.0K
Gross profit (FIFO) = 5,400 − 1,916.5 = $3,483.5K   → margin 64.5%
```

**The gap that's worrying Erica:**
```
COGS difference (LIFO − FIFO) = 2,433.0 − 1,916.5 = $516.5K
Tax rate = 21%
Tax savings from using LIFO = 516.5 × 21% = $108.5K
```

**The explanation for management:** Coffee Life's lower margin relative to FIFO peers is **not** an operating or competitive problem — it's a pure accounting-method artifact of a rising-price environment. LIFO immediately charges the *newest, most expensive* production to COGS, while FIFO leaves the expensive batches sitting on the balance sheet as ending inventory and expenses the cheaper, older batches instead. Any company using LIFO will show a lower gross margin than an otherwise-identical FIFO company whenever costs are rising — which is exactly what's happening with coffee prices. In exchange, LIFO generates a real, current-period **cash tax saving of $108.5K**, because it reports less taxable income right now.

**Should Erica recommend switching to FIFO?** No — not without giving up something real. Switching would report a rosier margin, but it forfeits the tax savings LIFO is generating during exactly the inflationary period when that saving is most valuable (and under U.S. GAAP, a company using LIFO for tax purposes must also use it for financial reporting — the "LIFO conformity rule" — so this isn't a decision that can be made independently for each audience). The right move is to **disclose and explain** the LIFO-vs-FIFO gap to investors (exactly what management is already doing in the quarterly review), not to sacrifice a genuine cash benefit purely to make the reported margin resemble peers'.

## 4. The production-pause decision — a genuine paradox under LIFO

Erica considered halting production for the final three (most expensive) batches — Dates 9, 10, 11 ($27.50, $27.80, $29.00) — when prices spiked in March, then decided to keep producing. The case asks you to recompute COGS and ending inventory as if those three batches had *not* been produced, and to judge whether continuing production was a mistake.

With only Dates 1–8 produced (145,000 bags total) and the same 90,000 bags sold, LIFO now has to reach further back to find 90,000 units to expense: it fully consumes Dates 3–8 (85,000 bags) and then dips into 5,000 bags from Date 2 (at $22.00/bag) to make up the difference:
```
COGS (LIFO, no Dates 9–11) = Σ(Dates 3–8 qty × cost) + 5,000 × $22.00
                           = $2,107.5K + $110.0K = $2,217.5K
Ending inv. = 35,000 bags @ $19.50 (all of Date 1) + 20,000 bags @ $22.00 (remainder of Date 2)
            = $1,122.5K
Gross profit = 5,400 − 2,217.5 = $3,182.5K   → margin 58.9%
```

**The paradox:** halting production of the three priciest batches actually *raised* reported gross margin (58.9% vs. the actual 54.9%) — even though Coffee Life still produced far more (145,000 bags) than it sold (90,000). That's because under LIFO, whichever units happen to be the *most recently produced* — regardless of whether the business physically needed them to cover this quarter's sales — are the ones charged to COGS. Producing three additional expensive batches, even though 145,000 bags already exceeded the 90,000 bags demanded, pulled those newer, pricier costs into this quarter's income statement purely because of *when* they were made.

**Was continuing production a mistake?** Not economically — production decisions should be driven by real operating needs (building inventory ahead of future demand, hedging against further price increases, keeping the roasting facility running efficiently), not by their mechanical effect on this quarter's LIFO-based COGS. But the case is deliberately showing you the *temptation*: a manager focused narrowly on this quarter's reported margin could improve it simply by timing production cutoffs around quarter-end — a reminder that LIFO gross margin, in an inflationary environment, is not a clean measure of underlying business performance and can be nudged by decisions that have nothing to do with actual profitability.

## 5. The inventory audit — a shrinkage write-off

The quarterly physical audit turns up **five missing 10 lb. bags**. Under LIFO, the cost assigned to a shrinkage loss is the cost of the *most recently added surviving layer* — here, Date 5 ($25.20/bag), since Dates 1–4 have already been fully consumed in COGS and Date 5 is the newest layer still sitting in ending inventory:
```
Impairment = 5 bags × $25.20/bag = $126.0K
```
**Accounting treatment:** increase COGS (or a separate inventory shrinkage/write-off expense) by $126K, and reduce the inventory balance on the balance sheet by the same $126K. This is a small but exact illustration of a broader LIFO mechanic: even a loss (not a sale) is costed out of the *most recent* surviving layer, consistent with LIFO's last-in-first-out convention applying to *any* reduction in the inventory pool, not just sales.

## Why this case was chosen for the COGS/Inventory topic
The Coffee Life inventory case does three things a textbook problem rarely combines in one scenario: (1) it shows LIFO and FIFO producing genuinely different, real-dollar outcomes from *identical* underlying production and sales data, making the abstract "cost-flow assumption" concept concrete; (2) it uses a realistic rising-price environment (coffee, 2020) to demonstrate the specific, predictable *direction* of the LIFO-vs-FIFO gross-margin gap, and forces you to translate that gap into a business explanation rather than an operational excuse; and (3) the production-pause "what if" is a deliberately uncomfortable case of an accounting method creating an incentive that has nothing to do with sound business strategy — teaching you to separate the real economics of a production decision from its mechanical effect on a reported accounting number, a distinction every manager eventually has to make when quarterly numbers are on the line.
