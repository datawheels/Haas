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
