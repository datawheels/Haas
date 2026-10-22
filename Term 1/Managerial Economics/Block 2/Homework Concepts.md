# Homework Concepts

Running notes on general concepts, as we work through problem sets. No problem-specific answers — just the underlying theory/formulas.

---

## 1. Monopoly Pricing (MR = MC)

**Inverse demand:** Rewrite demand Q = f(P) as P = a − bQ. This is necessary because marginal revenue is derived from price as a function of quantity, not the reverse.

**Marginal revenue shortcut:** For linear inverse demand P = a − bQ, marginal revenue has the *same intercept* and *twice the slope*:

MR = a − 2bQ

**Optimal price shortcut:** With linear demand and constant marginal cost, you can skip straight to:

P\* = (a + MC) / 2

(Derivation: set MR = MC → a − 2bQ = MC → Q = (a−MC)/2b → plug back into P = a − bQ → P = (a+MC)/2.)

---

## 2. Fixed Cost vs. Variable Cost

**Variable cost (VC):** Changes with quantity produced/sold (materials, assembly, shipping). Captured by marginal cost: VC = MC × Q.

**Fixed cost (FC):** Doesn't change with quantity (R&D, tooling, overhead). Sunk before any units are sold.

**Why it matters for pricing:** The profit-maximizing price depends *only* on marginal cost (via MR = MC) — fixed costs never enter that equation. Fixed costs determine whether you're profitable overall, not what price to charge.

**Profit equation:**

Profit = Revenue − Variable Cost − Fixed Cost
Profit = (P×Q) − (MC×Q) − FC

**Contribution margin** = Revenue − Variable Cost = (P − MC) × Q
This is the amount left over to cover fixed costs — *not* the same as profit unless FC is known/subtracted.

---

## 3. Sunk Cost Irrelevance

Since optimal price depends only on *marginal* cost, sunk costs already spent (e.g., past R&D) have **no effect** on the optimal price — they're spent regardless of Q. Whether a *future* cost affects pricing depends on whether it's fixed/sunk relative to the decision at hand, or whether it changes marginal cost.

More generally: **optimal price only responds to marginal cost and demand.** Anything that doesn't change one of those two things — fixed costs (past or future), financing/interest costs, unrelated side revenue streams — is irrelevant to the pricing decision itself, even though it still matters for overall profitability.

---

## 4. Demand-Side Shifts: Intercept vs. Slope

For linear inverse demand P = a − bQ, two different kinds of demand shifts have different pricing implications:

- **Change in a (the intercept / choke price):** Reflects a change in customers' *willingness to pay*. Since P\* = (a+MC)/2 depends on **a**, this *does* change the optimal price.
- **Change in b (the slope, i.e., quantity demanded at each price, holding the choke price fixed):** Reflects *market expansion* (more customers who value the product the same way as before). Since P\* doesn't depend on **b**, this does **not** change the optimal price — only quantity sold changes.

Useful distinction for "does an event justify a new price" questions: ask whether the event changes what people are willing to pay (shifts **a**) or just how many people are in the market (shifts **b**).

---

## 5. Capacity-Constrained Pricing

If a firm is producing at full capacity (selling everything it can make), it's no longer *choosing* Q via MR = MC — Q is fixed at the capacity level. The pricing decision shifts to: **set P so that quantity demanded equals the fixed capacity** (i.e., read price off the demand curve at Q = capacity). Marginal cost drops out of the price-setting logic entirely, since production quantity isn't being chosen anymore — price is just rationing a fixed supply.

Consequence: anything that doesn't shift the *demand curve* (fixed costs, financing costs, unrelated revenue streams) remains irrelevant to price even under a capacity constraint — the mechanism changes (demand-clearing instead of MR=MC), but the "only demand and marginal cost matter" principle still holds, just with marginal cost no longer in play at all.

**Value of relaxing a capacity constraint by one unit:** if a firm could add one more unit of capacity, its value equals the marginal revenue (not price!) at the current capacity-bound quantity — MR(Q) = a − 2bQ evaluated at Q=capacity — summed across every market/instance where that capacity is actually binding (and zero wherever it isn't). Compare this total to the cost of adding the unit. MR is used instead of price because selling one more unit typically requires lowering the price paid by *all* units, not just the marginal one.

---

## 6. Elasticity-Based Pricing (Lerner Rule)

An equivalent way to write the MR=MC condition, using elasticity instead of raw demand parameters:

MR = P × (1 − 1/|e|)  — using elasticity as a positive magnitude, or equivalently
MR = P × (1 + 1/ε_d) — using elasticity in its natural signed (negative) form

Both are the same formula; just whether the minus sign lives inside the elasticity (signed) or outside it (magnitude + explicit minus). Demand elasticity is always ≤ 0 by the law of demand, so when a problem quotes "the elasticity is X," it usually means the *absolute value* is X and the true signed value is −X.

**Lerner Rule corollary:** a profit-maximizing firm should never knowingly operate where demand is inelastic (|e|<1), since MR is negative there — meaning selling fewer units would increase both revenue and profit. Always operate on the elastic portion of demand (|e|≥1, i.e., ε_d≤−1).

**Combining elasticities across segments sharing one price:** when a single price serves multiple segments with different elasticities (e.g., forced uniform pricing due to arbitrage/resale/legal constraints), the *combined* elasticity is a **quantity-weighted average** of the segment elasticities:

e_total = (Q₁/Q_total)×e₁ + (Q₂/Q_total)×e₂ + ...

Plug e_total into the MR formula once to get a single combined MR comparable to MC — don't average the segments' individual MR values directly, since that's not mathematically equivalent and gives the wrong answer.

**Direction-of-adjustment rule (general optimization logic):** away from the true optimum, the sign of (MR − MC) tells you which way to move:
- MR > MC → the firm is under-producing/underselling relative to the optimum → should sell **more** (lower price)
- MR < MC → the firm is over-producing/overselling relative to the optimum → should sell **less** (raise price)
This is just the first-order condition of profit maximization (Profit = TR−TC, dProfit/dQ = MR−MC) applied away from the stationary point — the same logic used to *derive* MR=MC in the first place.

**Costs that scale with quantity sold belong in MC, even if framed as a contingent/uncertain risk** (e.g., "expected liability of $X per unit sold") — add it to marginal cost rather than treating it as a fixed cost, since it moves with Q.

**Risk aversion and uncertain costs:** a risk-neutral decision-maker treats an uncertain cost at its expected value. A risk-averse decision-maker treats it as *worse* than its expected value — they'd pay a premium above the expected cost to eliminate the uncertainty (a "certainty equivalent" that's higher than the expected cost, for a bad/risky outcome). So risk aversion reinforces (doesn't offset) whatever conclusion follows from treating an uncertain cost at its expected value — it pushes further in the same direction, not toward neutrality.

---

## 7. Combining Separate Demand Curves Into One

When multiple segments must be served at a **single uniform price** (arbitrage/resale/legal constraint prevents discrimination), build a combined demand curve by **summing quantities at each price**: Q_total(P) = Q₁(P) + Q₂(P). Watch for **kinks**: if segments have different choke prices (demand hits zero at different P), the combined curve only includes all segments over the price range where all are still active; above the lowest choke price, drop that segment from the sum. Then treat the combined curve as an ordinary monopoly problem (find inverse demand, apply MR=MC), and sanity-check that the resulting price actually falls within the range where your assumption (which segments are active) holds.

**Price discrimination vs. uniform pricing:** the ability to charge different prices to different segments is always **weakly more profitable** than being forced into one uniform price — discrimination lets you match price to each segment's own willingness to pay, while a uniform price is a compromise that's too high for some potential buyers (losing sales) and too low relative to others' willingness to pay (leaving money on the table). This is why firms invest in preventing arbitrage/resale between markets.

---

## 8. Two-Part Tariffs (Fixed Fee + Usage Price)

When customers are **identical** (same demand curve) and arbitrage/resale isn't an issue, a firm can do better than a single per-unit price by splitting pricing into two separate tools:
- **Usage price = MC.** This maximizes total value created (every unit worth more to the customer than it costs to provide gets consumed), rather than restricting quantity the way a markup-above-MC price does.
- **Fixed/membership fee = each customer's consumer surplus** at that usage price. Since all customers are identical, this fee can be set to extract the *entire* surplus without losing any customers, turning what would have been "value the customer keeps" into firm profit.

**Consumer surplus (linear demand):** the triangle between the demand curve and the price line, from 0 to the quantity purchased:
CS = ½ × Q × (choke price − P)
where choke price is the "a" intercept of inverse demand (the price at which quantity demanded hits zero).

This is why two-part tariffs often dramatically outperform simple per-unit pricing: simple pricing has to use one number to both ration usage *and* extract profit, and does both jobs worse than two separate tools would.

---

## 9. Price Discrimination Under a Shared Capacity Constraint

When multiple segments are priced separately (discrimination is possible) but together exceed a **shared capacity limit**, you can't just apply MR=MC independently to each segment — if their combined unconstrained quantities exceed capacity, total cost is effectively fixed (determined by the capacity, not by the allocation), so profit-maximization becomes a pure **revenue-maximizing allocation problem**: given a fixed total Q to split across segments, the optimal split sets

MR₁ = MR₂ = ... (marginal revenue equalized across all segments)

together with the capacity constraint (ΣQᵢ = capacity). If marginal revenues aren't equal, shifting a unit from the lower-MR segment to the higher-MR segment raises total revenue at no extra cost. This is the discrimination analogue of "MR=MC" — here cost is pinned down by the constraint, so only the revenue side is being optimized.

**Key contrast:** when segments are *not* capacity-linked, one segment's demand changing/appearing has **no effect** on another segment's price (each priced independently via its own MR=MC). When a *shared constraint* links them, one segment's presence **does** affect another's price/quantity, because serving one segment more means serving the other less.
