# Class 1 Case Study — In-Depth Notes: "Something Rotten in Fenmark"

Source: `Fenmark_Case.pdf` (3 pages, Prof. Benjamin Hermalin) + supplementary data `fish_restaurant.xls`, both analyzed live in `XMBA_201A_Lecture_1.pdf` slides 9–15. See companion "Theory Notes.md" §7 for the profit-formula framework this case is built on.

---

## 1. The setup

Fenmark's is a chain of fish restaurants founded in 1931, expanded into a chain after 1946, now run by CEO Christina Gauss. Every Fenmark's pledges same-day-fresh fish: any fish not sold by day's end is thrown out ("**wastage**"). Because delivery happens by 10am and can't be adjusted intraday, each restaurant manager sets a daily **standing order** — "it's a guessing game," per one manager.

Gauss has noticed that "restaurants with the largest average wastage per day also had the lowest profit per day on fish," and is considering centralizing/overriding managers' standing-order decisions. Two restaurants are given as data (also summarized on lecture slide 10):

| | Low-Waste Restaurant | High-Waste Restaurant |
|---|---|---|
| Price charged | $15.00 | $15.00 |
| Cost per fish | $6.00 | $6.00 |
| Standing order (X) | 400 | 420 |
| Average daily wastage | 14.82 | 43.80 |
| Average daily profit | $3,377.67 | $3,123.00 |

Restaurant manager Daniel Bernoulli (high-waste) pushes back: "would you rather I keep running out of fish? ... stocking out is a bad thing too."

**The three study questions the case poses:** (1) What is the problem at Fenmark's? (2) What is (are) the cause(s)? (3) What do the data suggest about which cause(s) are most likely responsible?

## 2. What the raw data in `fish_restaurant.xls` actually show

The workbook has two sheets, "Low-waste Restaurant" and "High-waste Restaurant," each with 360 days of `Sales`, `Wastage`, `Profit` (holidays/special weekends excluded per the case notes). I recomputed summary statistics directly from the 360-day panels (not just the headline averages Gauss cites):

| Statistic | Low-Waste (X=400) | High-Waste (X=420) |
|---|---|---|
| Mean sales | 385.18 | 376.20 |
| **Std. dev. of sales (≈ demand volatility)** | **22.27** | **55.43** |
| Min / max sales | 297 / 400 | 149 / 420 |
| Days sold out (demand ≥ X) | 185 / 360 = **51.4%** | 148 / 360 = **41.1%** |
| Mean wastage | 14.82 | 43.80 |
| Std. dev. of profit | 333.98 | 831.40 |

**This is the key fact the case is testing for: the high-waste restaurant's demand is roughly 2.5× as volatile as the low-waste restaurant's (σ = 55.43 vs. 22.27).** Gauss's framing — "the data really point to our throwing away too much fish" — implicitly assumes wastage is a *management quality* problem (sloppy or overly-generous ordering). The variance data instead point to wastage being substantially a *demand uncertainty* problem: a restaurant facing a much wider demand distribution will rationally carry more average wastage (and more stockouts) at *any* standing order, simply because it's guessing at a noisier target — exactly Bernoulli's objection.

## 3. The counterfactual/marginal analysis (lecture slides 13–15) — is either restaurant actually mismanaged?

The lecture deck runs a live "what if the standing order were X−1 or X+1?" counterfactual for both restaurants using the day-by-day data (slides 13–14):

- **Low-waste restaurant (X=400):** Avg. profit at X=400 is $3,377.67. At X=399 (hypothetical −1): $3,378.96. At X=401 (hypothetical +1): $3,379.38 to $3,379.04 depending on the sensitivity check. All four numbers are **within about $2 of each other** — the manager is sitting almost exactly at the profit-maximizing order quantity; small deviations up or down barely move average profit at all.
- **High-waste restaurant (X=420):** Avg. profit at X=420 is $3,123.00. At X=419: $3,122.83. At X=421: $3,123.17. Again, **changes of less than $0.20** — this manager, too, is sitting almost exactly at her local profit optimum.

**This directly answers study question 3.** The data do *not* support "the managers are ordering badly" as the dominant explanation — both are near-optimal *given their restaurant's own demand distribution*. Slide 15 ("What's going on?") makes this visually explicit: it plots profit against waste as two separate hump-shaped curves — one for low-waste restaurants, one for high-waste restaurants — each peaking near its own respective wastage level. Gauss's proposed fix (reduce wastage by fiat) would slide each restaurant *down its own curve*, away from its peak, exactly the "Haas Consulting Services" arrow drawn moving down-and-left off each curve in the slide. The tempting but wrong intervention is to compare the two restaurants' wastage levels directly, as if they were on the *same* curve.

## 4. Answering the three study questions directly

**Q1 — What is the problem at Fenmark's?** On the surface, the "problem" Gauss identifies is elevated wastage correlating with lower profit across restaurants. But per the analysis above, the real problem is a **measurement/attribution problem**: Gauss is comparing average wastage *across* restaurants with structurally different demand volatility and inferring a *causal, correctable* management failure, when the marginal analysis shows both managers are near-optimally set given their own local demand distributions.

**Q2 — What are the causes?** Using the profit formula from the Theory Notes (§7): `Profits = 9D − 6(X−D)` if X≥D, `9D − 9(D−X)` if X≤D. The optimal standing order trades off the (relatively cheap) opportunity cost of waste ($6/fish overordered, since cost is sunk once ordered but the $6 itself was avoidable had you ordered less) against the (relatively expensive) opportunity cost of a lost sale ($9 margin foregone per fish underordered). Because losing a sale is more costly at the margin than wasting a fish ($9 > $6), the profit-maximizing order quantity should sit **above** the median/mean demand, deliberately accepting some average wastage — this is a standard newsvendor-style asymmetric-cost result, not evidence of a mistake. A *high-variance* demand restaurant will rationally carry both higher average wastage **and** a higher stockout rate simultaneously (consistent with the data: the high-waste restaurant actually stocks out *less* often, 41.1% vs. 51.4%, despite wasting 3× as much on average — its wider order (420 vs. 400) is a rational response to wider demand, not overordering per se).

**Q3 — What do the data suggest about causes?** The marginal (counterfactual) analysis is the decisive piece of evidence: since local perturbations of ±1 fish barely move either restaurant's average profit, neither manager is meaningfully mispricing the wastage/stockout tradeoff. The dominant explanatory variable across restaurants is **demand volatility** (σ), not manager competence or effort. If Gauss wants to reduce total wastage across the chain, the higher-leverage lever is investing in **demand forecasting/demand-shaping tools** (or menu/promotional levers that dampen demand volatility) for the noisier restaurants — not stripping standing-order authority from managers, which (per the marginal analysis) would move each restaurant *away* from, not toward, its profit optimum.

## Cross-cutting themes

1. **A correlation across units (restaurants) with heterogeneous underlying uncertainty is not evidence of a controllable inefficiency within any single unit** — the same statistical trap as comparing two students' test-score variance without accounting for differences in test difficulty. Always ask "is the *comparison group* structurally different before concluding a within-group actor made a mistake?"
2. **Marginal analysis is the correct diagnostic tool, not average comparisons.** Gauss's instinct — compare average wastage across restaurants — is exactly the kind of "average cost" reasoning the course will explicitly warn against again in Class 3 (the "Average Cost Fallacy"). The right question was always "what happens to profit if I move the standing order by one unit?", which the counterfactual slides answer directly: essentially nothing, for either restaurant.
3. **This case is the concrete instance of the opportunity-cost profit formula introduced in Theory Notes §7** — every fish wasted has an opportunity cost of $6 (the sunk purchase, but a purchase that was itself avoidable via a lower order); every unmet customer has an opportunity cost of $9 (the forgone margin). Understanding *why* the optimal order sits above expected demand (because $9 > $6) is the direct forerunner of Class 2/3's formal opportunity-cost and marginal-cost machinery.

---

*(No open questions logged yet for this case — Fenmark's formal spreadsheet solution and TA discussion slides were "not posted yet" as of when class.md was captured; revisit this file once those are available.)*
