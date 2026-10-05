# Class 6 Case Studies — In-Depth Notes (Chapters 19 & 20: Linear & Curved Patterns)

## Suggested study order
1. Chapter-19.pdf / Chapter-20.pdf (core theory — see companion "Theory Notes.md")
2. Team Assignment 5 — Pricing the Ridgeline Jacket (apply everything to `meridian_pricing.csv`)

---

## 0. Setup and context

**Team Assignment 5 — "Pricing the Ridgeline Jacket"** is a continuation of the **Meridian Outfitters** fictional retailer used earlier in Block 2 (Class 4's "Free Shipping Isn't Free" team assignment, which used `meridian_customers.csv`). Here the focus shifts from customer behavior to **pricing a specific product**.

**The business setup (from the assignment doc):** the **Ridgeline rain jacket** is Meridian's best-selling product. Over the last two years the merchandising team has moved its price constantly — markdowns, holiday promotions, deliberate price tests — ranging from **$59** at the deepest discount to **$127** at the top. `meridian_pricing.csv` has one row per week (**104 weeks**) with `price` and `units_sold`. The spring planning meeting is Monday, and the proposal on the table is an **everyday price of $95**. The buyer needs a weekly unit forecast to size the inventory order, and wants to know how much to trust it.

**Data check:** confirmed 104 rows, `price` ranges from **$59 to $127** and `units_sold` ranges from **563 to 2,585** — matching the assignment's description exactly.

All regressions below were computed directly in Python (manual OLS via the normal equations: b1 = Sxy/Sxx, b0 = ȳ−b1x̄; r² = 1−SSE/SST; residual SE = √(SSE/(n−2))) against the actual 104-row dataset, not estimated by eye.

---

## 1. Part 1 — Fit a line and interpret it

**Linear regression, units_sold on price:**
```
units_sold = 3,036.88 − 20.85 × price        r = −0.8895, r² = 0.7911, sₑ = 215.64 (n=104)
```
This matches the assignment's printed check row almost exactly (3,037 / −20.9 / 0.79) — confirming the methodology.

**Interpreting the slope and intercept in business terms:**
- **Slope (−20.85):** each **$1 increase in the Ridgeline's price is associated with ~20.85 fewer units sold per week**, on average, over the observed $59–$127 range. This is an *association from historical price variation* (markdowns, promos, tests), not a controlled experiment — so it's the best available read on price sensitivity, but not guaranteed causal if, say, promotions also coincided with marketing pushes or seasonal demand shifts (a potential lurking variable, per the Ch.19 checklist).
- **Intercept (3,036.88):** the model's "predicted units sold at a price of $0" — but $0 is far outside the observed $59–$127 range, so like the Ch.19 diamond-weight intercept, **this is a pure extrapolation with no real-world meaning** on its own. It only exists mathematically to anchor the line.

**Where the line systematically misses (residual check):** binning the linear-model residuals by price band reveals a clear **U-shaped (bowl) pattern**, not random scatter:

| Price band | n | Mean residual |
|---|---|---|
| $59–70 | 23 | **+136.5** |
| $70–80 | 20 | −78.8 |
| $80–90 | 19 | −124.7 |
| $90–100 | 10 | −69.0 |
| $100–110 | 13 | −87.7 |
| $110–120 | 10 | **+101.7** |
| $120–127 | 8 | **+175.9** |

The straight line **overpredicts** units sold in the middle of the price range ($70–$110, residuals consistently negative) and **underpredicts** at both extremes (large positive residuals at the cheapest and priciest weeks). This is exactly the "bowl-shaped residual plot" diagnostic from Theory Notes §3.2/§3.6 — a signature of a **convex, decreasing demand curve** (diminishing returns to price cuts: the first $10 of discount off $127 buys far fewer extra units than the same $10 off $69). **This is a systematic miss, not ordinary scatter**: ordinary scatter is random noise around zero at every price level; here the *average* residual changes sign in a predictable pattern as price moves across its range — meaning the straight line is the wrong shape, not just imprecise.

---

## 2. Part 2 — Straighten the curve with logs

**Log-log regression, log(units_sold) on log(price):**
```
log(units_sold) = 14.0991 − 1.5904 × log(price)        r = −0.9481, r² = 0.8989, sₑ = 0.1220 (n=104)
```

**Filled-in comparison table (matching the assignment's format):**

| Model | Intercept | Slope | r² |
|---|---|---|---|
| units_sold on price | 3,037 | −20.9 | 0.79 |
| log(units_sold) on log(price) | **14.10** | **−1.59** | **0.90** |

The assignment states "the new slope is about −1.6" — our computed −1.59 matches.

**Interpreting the new slope (elasticity), one sentence:** a **1% increase in the Ridgeline's price is associated with roughly a 1.59% decrease in weekly units sold** — i.e. the jacket has **elastic demand** (elasticity magnitude > 1), meaning quantity responds more than proportionally to price.

**5% price increase — forecast effect:**
```
Units-change factor = 1.05^(−1.5904) = 0.9253  →  units fall ≈ 7.5%
(linear elasticity approximation: −1.59 × 5% ≈ −7.95%, close to the exact 7.5%)
```
**Revenue direction:** revenue = price × units. Computed directly at the two prices:
```
At $95.00: predicted units = 950.1  →  revenue = $90,261/week
At $99.75 (5% higher): predicted units = 879.2  →  revenue = $87,698/week
Revenue change ≈ −2.8% (also ≈ price% + units% = +5% + (−7.5%) ≈ −2.5 to −3%)
```
**Weekly revenue goes *down*** with a price increase, because demand is elastic (|elasticity| > 1): the percentage drop in units outpaces the percentage gain in price. This is the same logic as the Theory Notes' orange-juice example (§3.11) — elastic demand (γ = −1.75 there) meant the chain was leaving money on the table by pricing *too high*, and the same conclusion applies qualitatively here.

**The e^14.1 extrapolation trap:** a teammate exponentiates the intercept: e^14.1 ≈ **1,329,083** (confirmed: exp(14.0991) = 1,327,946 — essentially the same number, the small gap is just 14.1 vs. the exact 14.0991 estimate). The arithmetic is correct, but as a forecast it's absurd — "1.3 million jackets per week at a price of $1." **The rule this suggests:** the intercept of a log-log model corresponds to x=1 (log(1)=0), and **$1 is wildly outside the observed $59–$127 price range** the model was fit on. Combined with part (a)'s finding that the model is only validated where you have data, this is the same "don't extrapolate" lesson as Ch.19's diamond-weight intercept (Theory Notes §2.6) and the Ch.19 checklist item "limit predictions to the range of observed conditions" — a fitted model (linear or log-log) can only be trusted for x-values inside, or very close to, the range it was estimated on. A price of $1 is not a serious business scenario for a rain jacket in the first place, which is itself a sign the number should be distrusted on its face, before even doing the math.

---

## 3. Part 3 — Forecast at the proposed price ($95)

**Is the interval describing the average week at $95, or one particular week?** A **prediction interval** (as opposed to a confidence interval for the mean) describes the range for **one particular future week's** sales at $95 — which is exactly what the buyer needs, since she is sizing a single season's inventory order based on what could actually happen week to week, not the long-run average. A prediction interval is necessarily wider than a confidence interval for the mean because it must account for both the uncertainty in the fitted line *and* the natural week-to-week variability around that line.

**Point prediction and 95% prediction interval at price = $95:**
```
Log scale:  ŷ = 14.0991 + (−1.5904) × log(95) = 6.8566
            se(prediction) = sₑ × √(1 + 1/n + (x0−x̄)²/Sxx) = 0.1228
            95% PI (df=102, t≈1.9835): (6.6131, 7.1001)

Back-transformed (exponentiate):
  Point prediction  ≈ 950 units/week
  95% PI            ≈ (745, 1,212) units/week
```

**Why the interval is not symmetric:** the regression and its prediction interval are built — and are symmetric — on the **log scale**. Converting back to raw units requires exponentiating both endpoints, and **exponentiation is a convex function**: it stretches the upper half of a symmetric log-scale interval more than the lower half. Concretely, the point estimate (950) is only ~205 units above the lower bound (745) but ~262 units below the upper bound (1,212) — the upside genuinely does run farther from the prediction than the downside. This is a direct, mechanical consequence of forecasting on a log scale and then converting back — not a sign of anything wrong with the model.

**"Just give me one number" — what to tell the buyer:**
- **Point prediction (~950 units):** the single best guess, balancing stockout risk and markdown risk evenly. Right choice if the cost of understocking (lost sales, disappointed customers) and the cost of overstocking (end-of-season markdowns) are roughly symmetric to Meridian.
- **Lower bound (~745 units):** a conservative order quantity. Minimizes markdown/inventory-carrying risk, but raises the chance of stocking out if actual demand lands anywhere near or above the point estimate — appropriate if stockouts are cheap to recover from (e.g., jacket is replenishable mid-season) or margins are thin, so excess inventory is the bigger threat.
- **Upper bound (~1,212 units):** an aggressive order quantity that virtually guarantees no stockout, at the cost of carrying meaningfully more unsold inventory if the lower/typical end of the range plays out — appropriate if the Ridgeline is a flagship product where stockouts are reputationally costly and markdown risk is more tolerable.
- The right choice is a **newsvendor-style tradeoff** between the per-unit cost of a stockout (lost margin, lost customer goodwill) and the per-unit cost of excess inventory (markdown losses, carrying cost) — the buyer should pick a point in the interval based on which error is more expensive for this specific product, not default automatically to the midpoint.

**Forecast at $150 (premium colorway) — what to tell the buyer:**
```
Log scale:  ŷ = 14.0991 + (−1.5904) × log(150) = 6.1301
            Back-transformed point prediction ≈ 460 units/week
            95% PI ≈ (358, 590) units/week
```
**Caveat that must accompany this number:** $150 is **above the entire observed price range** in the data (max observed = $127) — this is an **extrapolation**, exactly like the e^14.1 trap in Part 2, just less extreme. The mechanical forecast (~460 units, 95% PI 358–590) can be reported, but it should come with an explicit warning: *the model has never seen a week priced above $127, so there is no evidence the elastic, constant-percentage relationship estimated over $59–$127 continues to hold at $150* — a premium colorway might have genuinely different demand dynamics (different customer segment, perceived quality signal) that this regression cannot speak to. Contrast with the **linear** model's behavior at an even more extreme extrapolation ($150): `3,036.88 − 20.85×150 = −91 units` — a **negative predicted quantity**, which is impossible and makes the extrapolation danger viscerally obvious. The log-log model degrades more gracefully (it can never predict negative units, since exponentiating always gives a positive number) but is still not validated outside its data range.

---

## 4. Tying back to the Theory Notes concepts

| Theory Notes concept (Chapters 19 & 20) | How it shows up in the Ridgeline case |
|---|---|
| Ch.19 §2.9 — residuals should show no pattern | The linear model's binned residuals (§1 above) show a clear U-shape, immediately flagging the straight line as the wrong functional form |
| Ch.19 §2.6 — intercept extrapolation caution | Both the linear intercept (price=$0) and the log-log intercept (price=$1, e^14.1 trap) are nonsensical extrapolations outside the $59–$127 data range |
| Ch.20 §3.4–3.6 — reciprocal/log transformations straighten curves | Log-log transform raises r² from 0.79 to 0.90 and visibly randomizes the residuals — the same diagnostic sequence as the MPG/Weight and pet-food examples |
| Ch.20 §3.7 — log-log slope = elasticity | −1.59 is read directly as the Ridgeline's own-price elasticity of demand (elastic, since \|−1.59\| > 1) |
| Ch.20 §3.11 — Optimal Price = Cost × γ/(1+γ) | **Cannot be computed for this assignment** — unlike the pet-food ($0.60 cost) and orange-juice ($1 cost) bonus examples in the slides, the Ridgeline assignment does not give a per-unit cost figure, so the optimal-price formula can't be completed numerically here. If Meridian's merchandising team supplied a landed cost per jacket, the identical formula from Theory Notes §3.11 would apply directly: Optimal Price = Cost × (−1.5904)/(1−1.5904) = Cost × 2.693 — i.e., optimal price would be roughly **2.7× unit cost**, since the revenue-maximizing/profit-maximizing markup under constant elasticity depends only on the elasticity, not on the specific cost level. |
| Ch.19 §2.10 — r² improving is suggestive but not sufficient on its own | Confirmed by actually checking the residual plot after the log transform, not just citing the r²: 0.79 → 0.90 jump, consistent with Ch.20 §3.10's warning not to compare r² across differently-scaled response variables without also checking residuals |

**Elastic demand, revenue, and the business recommendation:** because the estimated elasticity (−1.59) has magnitude greater than 1, the Ridgeline is in the **elastic** region of its demand curve at the prices tested. Standard pricing theory (and the Theory Notes' orange-juice example, where elastic demand meant the current price was too high) says that when demand is elastic, **cutting price increases total revenue**, and raising price decreases it — consistent with the −2.8% revenue change computed in Part 2 for a 5% price hike. This doesn't automatically mean Meridian should cut the proposed $95 price — profit also depends on unit cost/margin (not given here), not just revenue — but it is the quantitative basis the buyer needs to understand the tradeoff she's making by setting the everyday price at $95.

---

## Team AI-use statement (placeholder)

The assignment's final instruction asks the team to "add your team's AI-use statement (a few sentences — which tools you used and what you used them for)" before submitting. This is intentionally left blank here — it documents what **the submitting team** actually did during the live class exercise (which AI tool(s) they prompted, what for), not something these study notes can fill in on their behalf. Add it directly to the submitted assignment, not to this notes file.

---

## Cross-cutting themes
1. **The same diagnostic loop from the Theory Notes (fit → plot residuals → spot curvature → transform → recheck residuals → recheck r²) is exactly how the Ridgeline price/quantity relationship gets solved** — nothing about the business case requires new statistical machinery beyond what Chapters 19–20 cover.
2. **Extrapolation is the single most recurring trap across this case** — it shows up three separate times: the linear intercept at price=$0, the log-log intercept at price=$1 (e^14.1), and the $150 premium-colorway forecast sitting above the observed $59–$127 range. The fix is always the same: state the forecast, then explicitly flag whether the input is inside or outside the range the model was fit on.
3. **A prediction interval built on a transformed scale is not symmetric once converted back** — this is mechanical (a consequence of exponentiating a symmetric interval), not a modeling flaw, and matters directly for inventory decisions since the upside risk (running out) and downside risk (overstock) are not equal in raw-unit terms even though they were equal in log terms.
4. **Elasticity turns a regression coefficient into a business lever.** The −1.59 slope from the log-log fit isn't just a better-fitting number than the linear model's −20.9 — it's directly interpretable as "how much revenue moves when price moves," which is the actual question the spring planning meeting needs answered, and (with a cost figure) would plug directly into the Optimal Price = Cost×γ/(1+γ) formula from the Theory Notes.
