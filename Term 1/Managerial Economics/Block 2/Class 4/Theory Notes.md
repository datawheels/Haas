# Price Setting by a Monopolist — Theory Notes

Source: HermalinLectureNotes_v6.pdf, Lecture Note 3 "Costs" (pp. 53–61) and Lecture Note 4 "Introduction to Pricing" (pp. 63–91). No separate Lecture 5 slide deck has been posted for this class yet, so these lecture notes are the primary theory source; all formulas and worked examples below are pulled directly from them.

---

## 1. Where this fits in the course

Block 2 is about demand and pricing. Before you can price anything you need two building blocks: (i) a clean definition of **cost**, especially *marginal cost* (Lecture Note 3), and (ii) a clean definition of **marginal revenue**, derived from demand (Lecture Note 4). Class 4's whole arc is: demand → marginal revenue → the **MR = MC rule** → the profit-maximizing price → the **Lerner markup rule**, which connects that price back to a single summary statistic, the elasticity of demand. This is the toolkit Class 5 then extends into price discrimination.

## 2. Cost foundations (Lecture Note 3, pp. 53–61)

**Capital cost.** If $V_0$ is an asset's resale value today and $V_1$ its resale value at the end of the period, and $r$ is the return the firm could earn elsewhere on that money, then
```
capital cost = rV0 + (V0 − V1)
               forgone return   depreciation
```
Dividing by $V_0$ gives a capital-cost *rate* of $r+\delta$, where $\delta = (V_0-V_1)/V_0$ is the **rate of depreciation**. Key distinction: this is an *economic* measure of depreciation driven by actual resale-value decline (wear and tear, technological obsolescence) — it need not match an *accounting* depreciation schedule (e.g., the IRS's flat 5-year schedule for cars and computers), which "has little to no relation to actual changes in market value."

**Returns to scale and the shape of AC.**
- **Increasing returns to scale**: $AC(x)$ decreasing in $x$ ⟺ $C(\beta x) < \beta C(x)$ for $\beta>1$.
- **Decreasing returns to scale**: $AC(x)$ increasing ⟺ $C(\beta x) > \beta C(x)$.
- **Constant returns to scale**: $AC(x)$ flat ⟺ $C(\beta x) = \beta C(x)$, which implies $C(x) = cx$ (a constant marginal cost $c$).
- If $C(x) = F + cx$ (fixed cost $F$ plus constant per-unit cost $c$), $AC(x) = F/x + c$, which is *decreasing* — spreading overhead over more units. Many real firms have **U-shaped average cost curves**: increasing returns at low output (overhead dominates), decreasing returns at high output (congestion, input scarcity, quality strain).

**Cost causation — the accounting trap.** The lecture notes give two parables that matter directly for the Parker Hannifin case (Section 5 below):
1. **Lefthanded/righthanded scissors.** A firm makes 900 righthanded and 100 lefthanded scissors/day; each unit costs \$1 in labor+materials, plus a \$200 setup cost each time the machine switches products. Allocating the \$400/day setup overhead *by output share* (90%/10%) makes both product lines look equally "costed" at \$2.40/unit — but this is **wrong**: the correct (cost-causation) view is that the lefthanded line alone causes the \$200 lefthanded setup, i.e. its true marginal cost of the first unit is \$202, but $MC(2)=\dots=MC(100)=\$2$. Shutting down the "unprofitable" line based on the naive allocation actually destroys a genuinely profitable product (adding lefthanded scissors: revenue \$500 > cost \$600 is the *wrong* comparison once you allocate correctly — the parable shows how allocating shared overhead on an arbitrary basis, here output share, can flip a correct shut-down/keep decision).
2. **Red pens and blue pens ("the Parable of Red Pens and Blue Pens").** A firm profitably makes 5,000 red pens (30¢/20¢ tiered price) and 3,000 blue pens (25¢) for a genuine daily profit of \$50, using a \$1,000/day machine that is *true shared overhead* (not caused by either line). An "evil accountant" allocates the \$1,000 by output share (5/8 to red, 3/8 to blue), which makes blue pens look unprofitable (–\$75/day). Shutting down blue pens to "fix" this actually drops the firm from +\$50/day to –\$100/day, because the full \$1,000 overhead then lands entirely on red pens. **Moral: don't allocate true shared overhead for decision-making purposes at all** — it has nothing to do with cost causation and can only mislead.

**Summary takeaways (lecture notes' own list):** sunk expenditures are irrelevant for decisions; understand $MC$, $AC$, $C$ and their relationships; returns to scale set the AC curve's shape; allocate costs only by cost causation; never allocate shared overhead for decision-making.

## 3. Simple pricing, profit maximization, and the MR = MC rule (§4.1–4.4)

**Simple (linear/uniform) pricing** — Definition 8: charging the *same* price per unit to every buyer regardless of identity or quantity purchased. It is nondiscriminatory, and it's the only option available when the seller can't identify buyers or can't prevent **arbitrage** (resale from low-price to high-price buyers, which forces a single effective price to hold).

**Profit** is $\pi(x) = R(x) - C(x)$. In the *continuous* case, marginal revenue is defined by analogy to marginal cost:
```
MR(x) = lim_{h→0} [R(x+h) − R(x)] / h = R′(x)
```

**Result 21 (worked derivation):** if $R(x) = Ax - Bx^2$ ($A>0$, $B\ge0$), then $MR(x) = A - 2Bx$ (derived directly from the limit definition in the lecture notes).

**Result 22 (MR = MC rule).** A necessary condition for the profit-maximizing output $x^*$: $MR(x^*) = MC(x^*)$. Derivation logic: at $x^*$, $\pi'(x^*)=0$, and $\pi'(x) = R'(x)-C'(x) = MR(x)-MC(x)$.

**Result 23/24 (sufficiency).** $x^*$ is truly profit-maximizing if, in addition to $MR(x^*)=MC(x^*)$, $MR(x)>MC(x)$ for all $x<x^*$ and $MR(x)<MC(x)$ for all $x>x^*$ — i.e., **MR crosses MC once, from above**.

**Result 26 (Shutdown rule).** Compute the candidate $x^*$ (or discrete $n^*$) from the MR=MC rule; the firm should actually produce it only if $\pi(x^*)\ge \pi(0)=0$ — equivalently, only if $AR(x^*)\ge AC(x^*)$ (average revenue at least covers average cost).

**Example 10 (worked, from the lecture notes, in full):** $R(x)=10x-\frac{1}{1000}x^2$, and $C(x)=0$ if $x=0$, else $2x+F$.
```
MR(x) = 10 − x/500      [from Result 21: A=10, B=1/1000]
MC(x) = 2               [constant, from Result 15]

Set MR(x*) = MC(x*):  10 − x*/500 = 2  ⟹  x* = 4000

Shutdown check: AR(x*) ≥ AC(x*)?
  AR(x*) = 10 − 4000/1000 = 6
  AC(x*) = 2 + F/4000
  6 ≥ 2 + F/4000  ⟺  F ≤ 16,000
```
So the firm should produce 4,000 units *provided* fixed cost $F$ does not exceed \$16,000; otherwise it should shut down entirely. This example is the template for every "should we operate at all" decision downstream.

## 4. Demand, marginal benefit, and consumer surplus (§4.5)

**Individual demand is derived from a benefit function**, $b(q)$ — the dollar-equivalent happiness from $q$ units — with **marginal benefit** $mb(q)$ analogous to marginal revenue. Marginal benefit schedules are always **decreasing** (Observation 1): diminishing marginal utility, plus opportunity-cost "crowding out" of other consumption.

**Consumer surplus** under simple pricing is the consumer's "profit" from buying: $cs(x) = b(x) - px$. The consumer maximizes surplus by choosing $x^*$ where $mb(x^*) = p$ — graphically, where the $mb(\cdot)$ curve crosses the horizontal price line, from above.

**Demand curve** $d(p)$ is literally the inverse of the marginal-benefit schedule: $d(p) = mb^{-1}(p)$ for $p \le mb(0)$, and $d(p)=0$ for $p > mb(0)$. **Example 11:** $b(x) = 10x - x^2 \Rightarrow mb(x) = 10-2x \Rightarrow d(p) = 5 - p/2$ for $p\le10$, else 0.

**Complements and substitutes.** If chips ($p_c$) and salsa are complements, a *higher* $p_c$ shifts salsa's demand curve *in* (down/left) — less benefit per ounce of salsa when you're buying fewer chips to go with it. If beer and wine are substitutes, a higher beer price shifts wine's demand curve *out*. Other demand shifters: exogenous events (a hurricane increases demand for bottled water/plywood — benefit itself shifts up), and technology (USB drives caused floppy-disk demand to shift in — equivalent to the "price" of a substitute falling toward zero).

**Aggregate demand** is just the horizontal sum of individual demand curves: $D(p) = \sum_n d_n(p)$. **Example 12 (worked):** 1,000 type-A consumers with $d_A(p)=150-3p$ (for $p\le50$) and 2,000 type-B consumers with $d_B(p)=1000-2p$ (for $p\le500$) aggregate to:
```
D(p) = 2,150,000 − 7,000p   for p ≤ 50
D(p) = 2,000,000 − 4,000p   for 50 < p ≤ 500
D(p) = 0                     for p > 500
```
This is the piecewise-kink pattern you should expect whenever heterogeneous groups have different price ceilings ($mb(0)$).

## 5. Demand elasticity (§4.6)

```
ε_D = D′(p) × p / D(p)
```
Interpreted as the percent change in quantity demanded per percent change in price. Because demand curves slope down, $\varepsilon_D<0$ always.

## 6. Marginal revenue and elasticity under simple pricing (§4.7)

**Deriving MR from demand (the "driving-down-the-price" effect).** If the firm sells $dq$ more units, it gains $dq \times P(q)$ (selling more, the "good news") but loses $-dp\times q$ on *all* units already being sold at the old price (the "bad news," since $P(\cdot)$ must fall to sell more). Net:

**Result 27:** $MR(q) = P(q) + P'(q)q$, where the $P'(q)q$ term (negative, since demand slopes down) *is* the driving-down-the-price effect.

**Example 13 (worked):** demand $D(p) = 500{,}000 - 2500p$. Inverting: $P(q) = 200 - q/2500$. Then
```
MR(q) = (200 − q/2500) + (−1/2500)q = 200 − 2q/2500 = 200 − q/1250
```
Three general patterns this illustrates: (1) if inverse demand is linear, MR is linear too; (2) MR and inverse demand **share the same intercept** (here, 200); (3) MR's slope is **exactly twice** inverse demand's slope (−1/1250 vs. −1/2500). Memorize this "same intercept, double slope" rule — it's the fastest way to sanity-check an MR curve by eye.

**Result 28 (MR's sign and elasticity):**
```
MR(q)/P(q) = 1 + 1/ε_D
```
- If $\varepsilon_D < -1$ (**elastic**): MR is positive.
- If $\varepsilon_D = -1$ (**unitary elastic**): MR is exactly zero.
- If $\varepsilon_D > -1$ (**inelastic**): MR is *negative*.

**Result 29 (a firm never voluntarily prices on the inelastic portion of demand):** on the inelastic portion, raising price *simultaneously* raises revenue (since $|\%\Delta Q| < |\%\Delta P|$) and cuts cost (producing less). A move that both raises revenue and cuts cost is a free win, so an optimizing firm will never stop there — it always keeps raising price/cutting quantity until it reaches the elastic (or at worst unitary-elastic) region.

## 7. The profit-maximizing price (§4.8) — full worked example

**Example 14 ("from start to finish"):** demand $D(p) = 1{,}000{,}000 - 50{,}000p$; costs $C(q)=0$ if $q=0$, else $6q + 1{,}400{,}000$.

```
Invert demand:      P(q) = 20 − q/50,000
MR(q) = P(q) + P′(q)q = 20 − q/25,000
MC(q) = 6                                   [constant, Result 15]

Set MR = MC:   20 − q/25,000 = 6
               q* = (20−6) × 25,000 = 350,000

Price:  P(350,000) = 20 − 350,000/50,000 = 13   → profit-maximizing price = $13

Shutdown check:
  AC(q*) = 6 + 1,400,000/350,000 = 6 + 4 = 10
  AR(q*) = P(q*) = 13 ≥ AC(q*) = 10  →  firm should produce

Profit: π(350,000) = 13×350,000 − (6×350,000 + 1,400,000)
                    = 4,550,000 − 3,500,000 = 1,050,000
```
**Maximum profit = \$1,050,000.** This is the canonical template calculation for "given a demand curve and a cost function, find price, quantity, and profit."

## 8. The Lerner Markup Rule (§4.9) — the key formula for Class 4's articles

**Result 30 (Lerner markup rule).** At the profit-maximizing price and quantity under simple pricing, the *proportion* of price that is markup over marginal cost equals $-1/\varepsilon_D$:
```
(p* − MC(q*)) / p* = −1/ε_D
```
**Derivation (from the notes):** start from $MR(q)=p\times(1+1/\varepsilon_D)$ (Result 28 rearranged) and $MR(q^*)=MC(q^*)$ at the optimum:
```
(p*−MC(q*))/p* = (p*−MR(q*))/p* = (p* − p*(1+1/ε_D))/p* = −1/ε_D
```
**Reading the rule:** the *more elastic* demand is (larger $|\varepsilon_D|$), the *smaller* the optimal markup as a fraction of price. A firm facing highly price-sensitive customers cannot sustain a fat margin; a firm facing inelastic (captive) demand can charge a large markup over cost. **This single formula is the analytical backbone for both the Parker Hannifin and chocolate-company articles** — a uniform 35% markup rule is optimal *only* if $-1/\varepsilon_D$ happens to equal 0.35 for every product, which is true only by coincidence when a firm sells a heterogeneous portfolio with different elasticities per product.

**Example 15 (worked — responding to a cost shock):** marginal cost rises from \$10.00 to \$10.50 (+5%); elasticity at the current price is $\varepsilon_D=-1.25$. Using the Lerner rule:
```
(p − 10.50)/p = −1/(−1.25) = 0.8
p − 10.50 = 0.8p  ⟹  p = 10.50/0.2 = $52.50
```
New optimal price: **\$52.50**.

**Example 16 (general result — the "pass-through" rule):** if marginal cost rises by a small percentage $\delta$, the Lerner rule implies the optimal response (for small changes, holding $\varepsilon_D$ roughly constant) is to **raise price by approximately the same percentage** $\delta$. E.g., a 2% cost increase ⟹ raise price ~2%. And if $\varepsilon_D=-1.5$, a 2% price increase yields an approximate 3% reduction in units sold (since $\%\Delta Q \approx \varepsilon_D \times \%\Delta P$).

## 9. Summary (Lecture Note 4's own recap, §4.10)

1. Determine MR and MC schedules.
2. Solve $MR(q)=MC(q)$ for a *candidate* profit-maximizing quantity; confirm MR crosses MC once from above.
3. Check the shutdown rule (is $AR(q^*)\ge AC(q^*)$?).
4. Individual → aggregate demand; MR under simple pricing has a "good news" (more units sold) and "bad news" (driving-down-the-price) component.
5. The Lerner markup rule connects the optimal price-cost margin to a single number: $-1/\varepsilon_D$.

---

## Cross-cutting themes

1. **A uniform markup rule is a special case, not a law of economics.** The Lerner rule shows the *correct* markup on any given item is $-1/\varepsilon_D$ for *that* item's own demand elasticity — a flat 35% (or any single number) applied across an entire portfolio is optimal only when every item happens to share the same elasticity, which is essentially never true for a diversified product line. This is the single formula that explains why "tear up the flat markup" articles make economic sense.
2. **Marginal cost, not average cost, drives the pricing decision** — the MR=MC rule never references AC except for the separate shutdown check. A firm can therefore rationally sell some units near marginal cost (thin margin, high elasticity) while charging a large markup on others (fat margin, low elasticity), even if company-wide average cost accounting makes this look "inconsistent."
3. **Elasticity is the bridge between "abstract economics" and "pricing manager's dashboard."** Every pricing decision in the Class 4 articles — bowling-alley-style holiday-week markups, Parker Hannifin's move away from a flat rule, the chocolate company's quarterly repricing — is, underneath, an attempt to estimate $\varepsilon_D$ for a specific product/segment/time period and apply (implicitly or explicitly) the Lerner rule to it.
4. **Cost causation matters as much as demand.** The scissors and red-pens/blue-pens parables (Lecture Note 3) are the theoretical foundation for *why* a firm might mistakenly believe some of its "niche" products are unprofitable (because of naive overhead allocation) and cut a flat markup rule to compensate — when the real fix is to price by elasticity, not to re-allocate shared costs.

---

## Gulsher questions (along with clarification)

*(none yet — add here when you have follow-up questions on Class 4's monopoly pricing material)*
