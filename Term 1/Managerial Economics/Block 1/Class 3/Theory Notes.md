# Class 3: Fixed, Variable, and Marginal Costs — Theory Notes

Source: `EMBA_Lecture_3.pdf` (Prof. Steve Tadelis, 34 slide-pages, titled "A Classification of Economic Costs and Introduction to Price Setting") cross-referenced with `HermalinLectureNotes_v6.pdf` §3.3–3.5 "Relations Among Costs," "Costs in a Continuous Context," and "A Graphical Analysis of Costs" (printed pp. 43–48, the syllabus's pp. 45–50 range).

---

## 1. Where this fits

Class 2 established the vocabulary (opportunity cost, sunk cost, overhead/variable/marginal cost) via one-off examples. Class 3 turns that vocabulary into a *quantity-choice* tool: given a cost structure, how much should a firm produce, and when should it shut down entirely? The lecture opens with a full recap of Class 2 (slides 2, 9–10: expenses vs. costs, opportunity costs, sunk costs), then works one extended numerical example (the "combs" deep dive) end to end, before pivoting into a first look at pricing.

## 2. The Shared Overhead Fallacy (slides 6–8) — causal cost allocation

**Setup:** You tutor in two cities. Berkeley: $30/hr, 5 hrs/day. Palo Alto: $40/hr, 2 hrs/day. Your alternative use of time is the Berkeley Library at $20/hr. Commuting to Palo Alto costs 3 hours on the road plus $25 in tolls/gas/wear.
```
Daily income = 5(30) + 2(40) − 25 = 150 + 80 − 25 = $205
```
**Naive (revenue-proportional) overhead allocation:** commuting "overhead" = 3 hrs × $20 (lost library income) + $25 = **$85**. Revenues: $150 Berkeley (65%), $80 Palo Alto (35%). Allocate overhead proportionally: Berkeley gets 0.65×85=$55.25, Palo Alto gets 0.35×85=$29.75.
```
Berkeley "net income" = 5×(30−20) − $55.25 = $50 − $55.25 = −$5.25
Palo Alto "net income" = 2×(40−20) − $29.75 = $40 − $29.75 = +$10.25
```
**An accountant using this allocation recommends: drop Berkeley, keep Palo Alto, spend those 5 hours at the library.** Sounds reasonable — but it's wrong.

**The fix — causal allocation (Result 11 from Class 2 Theory Notes, restated on slide 8):** *"If it can't be causally allocated, don't allocate it at all."* Here, **all** of the commute is caused by the Palo Alto trip (there's no Palo Alto business without the drive). Allocating the full $85 to Palo Alto instead:
```
Berkeley net income = 5×(30−20) = $50
Palo Alto net income = 2×(40−20) − $85 = $40 − $85 = −$45
```
**The correct conclusion is the exact opposite of the naive one: drop Palo Alto, keep Berkeley.** The lesson: overhead should be allocated to whatever activity *causes* it, never in proportion to revenue or any other arbitrary base — an unallocable or non-causal allocation actively produces the wrong decision, not just an imprecise one.

## 3. A Categorization of Costs (slides 11–12; Hermalin §3.2–3.3, Class 2 Theory Notes §8)

- **Variable costs:** incurred per unit of production (raw materials, direct labor).
- **Overhead (fixed) costs:** incurred by the activity, don't vary with production (machine leases, HR staff). These can themselves be sunk (R&D, past rent), caused by one activity, caused by several activities, or shared by the whole company (C-suite, general admin) — the harder the cost is to trace to a cause, the more dangerous naive allocation becomes (§2 above).
- **Total cost:** `C(q) = F + V(q)`, F = fixed cost, V(q) = variable cost.
- **Average cost:** `AC(q) = C(q)/q`.
- **Marginal cost:** `MC(q) = C(q) − C(q−1) = V(q) − V(q−1)` (fixed cost drops out of the *difference*, since it's the same at q and q−1).

**Hermalin's baseball analogy (Ch. 3.3, p. 44):** think of MC(j) as 1 if a hitter gets a hit on his jth at-bat, 0 otherwise. His batting average (=AC) rises after a hit (MC=1 > his current average) and falls after an out (MC=0 < his current average). Formally:
```
Result 14: If average cost is declining, marginal cost is below average cost.
           If average cost is increasing, marginal cost is above average cost.
Result 16: The MC schedule crosses the AC schedule exactly at AC's minimum.
```
(Proof sketch: `AC(n+1) = MC(n+1)/(n+1) + [n/(n+1)]AC(n)`; if MC(n+1) > AC(n), the weighted average must rise, and vice versa — see Hermalin p. 44 footnote for the full algebra.)

**Continuous version (Hermalin §3.4, p. 45–47):** for a continuous quantity x, `MC(x) = lim(h→0) [C(x+h)−C(x)]/h = C′(x)`, i.e., **marginal cost is the derivative of total cost**. Worked forms: if `C(x)=Ax`, MC(x)=A (constant). If `C(x)=Ax²+Bx`, MC(x)=2Ax+B (linear, rising). If there's overhead F, `C(x) = 0 if x=0, else G(x)+F` — the function is discontinuous at 0 (can't define MC(0)), but MC(x) for x>0 doesn't depend on F at all, since F is a constant shift and drops out of the derivative — **fixed costs never affect marginal cost.**

**Graphical relations (Hermalin §3.5, p. 47–48):** since `AC(x) = C(x)/x`, we get `C(x) = x·AC(x)` — total cost at quantity x̂ is the *area of the rectangle* with width x̂ and height AC(x̂) under the AC curve. Plotting AC(x) (typically U-shaped: falling while spreading fixed costs over more units, eventually rising as variable costs increase per unit) together with MC(x) (typically upward-sloping) shows MC crossing AC exactly at AC's minimum (Result 16), visually confirming the baseball-average logic above.

## 4. The Average Cost Fallacy — the "combs" deep dive (slides 14–22)

**The naive pitch (slide 14):** "Market price of combs is $1. Average cost of a comb is 90¢. 10,000 combs/day → profit = $1,000/day, a 10% return. Are you happy?"

**The real cost structure, uncovered on further scrutiny (slide 15):**
- Overhead: $500/day (machine & space)
- Materials: $0.30/comb
- Labor: $500/hr for the first 8 hours, then **time-and-a-half** ($750/hr) after
- Each hour of production makes 1,000 combs

**First 8,000 combs (slide 16):**
```
C(8,000) = F + material + labor = $500 + (0.3×8,000) + (0.5×8,000) = $500 + $2,400 + $4,000 = $6,900
Revenue = $8,000 → Profit on first 8,000 = $1,100
```
**Next 2,000 combs (hours 9–10, overtime labor at $0.75/comb):**
```
Cost of next 2,000 = (0.3×2,000) + (0.75×2,000) = $600 + $1,500 = $2,100
Revenue = $2,000 → Loss on next 2,000 = −$100
```
**"Should you be happy? NO!"** — you're making $1,100 on the first 8,000 combs but *losing* $100 on the last 2,000, even though the blended average cost across all 10,000 (90¢) still looks profitable against the $1 price. **The reason:** "if average costs are below the price per unit, you are making a positive profit *on average*, but not necessarily on every unit sold" — the last 2,000 units actually cost $1.05 each vs. a $1 price.

**Full piecewise cost function (slide 18):**
```
C(q) = 500 + (0.3+0.5)q = 500 + 0.8q            if q ≤ 8,000
C(q) = 500 + 6,400 + (0.3+0.75)(q−8,000) = −1,500 + 1.05q   if q > 8,000
```
(Graphed on slide 19: a kinked upward line, slope 0.8 up to q=8,000, then steeper slope 1.05 beyond.) The corresponding **AC(q)/MC(q)/Price graph (slide 20)** shows: MC = 0.8 for q≤8,000, jumping to MC = 1.05 for q>8,000; AC starts high (spreading the $500 fixed cost over few units), falls to a minimum around 0.8625 near q=8,000, and starts rising again for q>8,000 as the higher marginal cost pulls the average up; Price ($1) sits *above* MC for q<8,000 and *below* MC for q>8,000.

**Optimal Behavior (slides 21–22):**
```
For q < 8,000:  MC(q) = 0.80 < 1.00 = p   → producing is profitable, keep going
For q > 8,000:  MC(q) = 1.05 > 1.00 = p   → producing is unprofitable, stop
```
**General rule:** produce every unit for which the marginal revenue (here, just price, under simple pricing) exceeds marginal cost; don't produce any unit for which marginal cost exceeds price. **Critically: AC(q) plays no role in deciding how much to produce — it only tells you whether to produce *at all* (the operate/shut-down decision).** This is the single most important sentence in the deck's Summary slide (23): *"Average costs are important for operate/shut-down decisions, but not for optimal quantity! Marginal costs are important for optimal quantity decisions!"*

## 5. Introduction to Pricing (slides 24–34) — brief preview, picked up fully in Block 2

The deck pivots from "given a price, how much to produce" to "how do you find demand, and what price should you set." **A firm's general problem:** choose quantity or price to maximize Profit = Revenue − Cost = p×q − C(q).

**Where demand comes from — the chocolate/WTP auction (slides 3–4, run live in class):** students bid their willingness-to-pay (WTP) for a piece of chocolate; the top 10 bidders win, each paying the 11th-highest ("highest losing") bid — a live Vickrey-style mechanism designed to elicit honest WTP.

**From individual WTP to a market demand curve (slides 27–29):** sorting individual WTPs from highest to lowest and plotting them **is** the market demand curve — "marginal WTP is the demand function." Unlike most disciplines' convention, economics plots quantity as a function of price, `p(q)`, not `q(p)`. A firm can't price-discriminate perfectly (charge student 1 exactly $5, student 2 exactly $4.75, etc.) because arbitrage breaks it: a low-WTP buyer could resell to a higher-WTP buyer. **Implication: a firm must set one price for all** — "simple (monopoly) pricing."

**Revenue and marginal revenue (slides 30–32):** plotting revenue = p(q)×q against q produces a hump shape peaking where marginal revenue MR=0 (here, at q=10, revenue=$25). **If MC=0**, the profit-maximizing quantity is exactly where MR=0 (maximize revenue) — "does this remind you of anything? Combs!" (the same "produce while marginal benefit exceeds marginal cost" logic as §4).

**Harder case, MC=1 (slide 33):** compare the two integer quantities straddling where MR crosses MC=1: at q=6, p=$3.75, profit = 6×(3.75−1) = **$16.50**; at q=8, p=$3, profit = 8×(3−1) = **$16.00**. **Choose q=6** (higher profit) — since q must be an integer, you check both candidates neighboring the crossing point rather than relying on a continuous first-order condition alone.

**Summary (slide 34):** *"MC and demand (MR) determine the optimal price/quantity. AC(q) is not playing a role for how to price or how much to produce, only matters for if to produce at all!"* — the exact same punchline as §4, now generalized from a single fixed price to a firm that sets its own price.

## Cross-cutting themes / Punchline

1. **Marginal reasoning, not average reasoning, drives every quantity/pricing decision in this course.** The combs example, the Shared Overhead Fallacy, and the MC=1 pricing example are three different costumes on the identical idea: compare the *next* unit's cost to the *next* unit's benefit; never let a blended average mislead you about a specific marginal unit.
2. **Average cost still matters — but only for the binary operate/shut-down decision**, not for choosing *how much* to produce once you've decided to operate. Confusing these two questions is the single most common error this class is built to inoculate against.
3. **Fixed costs are causally about *why* a cost exists, not just *when* it was paid.** Sunk-ness (Class 2) and fixed-vs-variable (Class 3) are related but distinct: a fixed cost is fixed because it doesn't vary with output; it becomes *sunk* only once it's unavoidable over your relevant decision horizon. Overhead can be non-sunk (a machine lease you could still cancel) or sunk (R&D already spent).
4. **Setting up Brand X (picked up at the start of Block 2):** the last "after class" item assigns `Brand_X.pdf` + `Brand_X_Data.xls` — a young Brand X executive is puzzled why the price of her firm's proprietary "Chemical Z" jumps around quarter to quarter (e.g., $3.06/gallon this quarter vs. $3.07 three years ago, selling a near-identical ~4.2M gallons both times) even though demand looks stable. Brand X uses a cost-plus pricing rule (unit cost + 20% markup), and the quarter-40 cost breakdown shows raw materials (whose locked-in price swings quarter to quarter) as by far the largest and most volatile cost component (~$1.69/gallon of a $2.55 unit cost). This is exactly a "confusing AC-based pricing with MC/demand-based pricing" setup (§4–5 above) — the assignment (not solved here) asks you to judge Brand X's pricing strategy and recommend one of your own using the 40-quarter panel in `Brand_X_Data.xls` (columns: Quarter, Profit, Demand, Price, raw-material-% of unit cost).

---

## Gulsher questions (along with clarification)

*(none yet — add here when you have follow-up questions on Class 3)*
