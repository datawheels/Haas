# Class 2: Decision Making Under Uncertainty and Economic Costs — Theory Notes

Source: `XMBA_201A_Lecture_2.pdf` (Prof. Steve Tadelis, 35 slide-pages, two topics in one deck) cross-referenced with `HermalinLectureNotes_v6.pdf` — the tail of Chapter 1 (§1.5 Real Options, p. 18–19, recap), Chapter 2 "Risk Aversion" §2.1–2.2 (pp. 21–23), and Chapter 3 "Costs" §3.1–3.2 (pp. 37–42, opportunity cost and cost concepts — the syllabus's pp. 29–44 range).

---

## Part A: Decision Making Under Uncertainty (continued)

### 1. Recap and risk attitudes (slides 2, 5)

Decision trees "frame problems": boil them to core issues, force critical thinking, surface implicit assumptions. The open question left from Class 1 is how to handle **values and probabilities** you're unsure of — and, new this class, how to handle a decision maker's **attitude toward risk**.

**Formal risk-attitude definitions**, using a lottery *L* that pays $0 or $100 with equal probability (EV = $50), with *v(x)* the decision maker's value/utility function:
- **Risk-neutral:** Ev(L) = v($50) — e.g., v(x) = x for all x. (An expected-value maximizer — everything from Class 1 assumed this.)
- **Risk-averse:** Ev(L) < v($50) — e.g., v(x) = √x. The lottery is *worse* than its expected value.
- **Risk-loving:** Ev(L) > v($50) — e.g., v(x) = x². The lottery is *better* than its expected value.

**Hermalin's formalization (Ch. 2.1, pp. 21–22)** sharpens this with the **certainty-equivalent value (CE)**: *the minimum payment a decision maker would accept, with certainty, rather than face a gamble.* For a lottery with EV = $500,000 (a 50/50 shot at $1M or $0), most people would sell their ticket for well under $500,000 — say $400,000 — which reveals CE = $400,000 < EV = $500,000, i.e., risk aversion.
- **Definition 3 (risk averse):** CE ≤ EV for all gambles, CE < EV for at least some.
- **Definition 4 (risk neutral):** CE = EV for all gambles.
- **Definition 5 (risk loving):** CE ≥ EV for all gambles, CE > EV for at least some (rare in practice — even casino-goers typically buy homeowner's insurance).

### 2. A primer on discounted cash flows (slides 13, 15)

Needed as a building block for the real-options examples below. If you're promised $1,000 in exactly one year and the bank charges 12% interest, then borrowing $x today obligates you to repay $y = $x × 1.12 in a year. Solving for what the bank would lend you against a $1,000 promise:
```
$1,000 in 1 year is worth $1,000 / 1.12 = $892.86 today.
```
For a payment n years out, discount by (1.12)ⁿ — e.g., 2 years: divide by (1.12)².

### 3. Real options and reversibility — the lemonade-stand example (slides 9–12)

**Setup:** A proprietary recipe guarantees $100/day profit for 2 remaining days (total $200, certain). An experimental recipe instead yields, with equal probability, either $(x+50) or $(x−50) per day (expected daily profit = x). **Question: what's the lowest x that makes trying the experiment worthwhile?**

Naive answer: x = $100, since then E[2-day profit] = ½(150)+½(50) = $100/day matches the status quo. **But the correct answer is lower, because the decision is reversible** — if day 1's experiment goes badly, you can switch back to the proven recipe for day 2.

**Full decision tree (for 50 < x < 100):**
```
Experiment → Good outcome (p=.5): (x+50)+(x+50) = 2x+100
           → Bad outcome (p=.5):  → Stick:       (x−50)+(x−50) = 2x−100
                                   → Switch back: (x−50)+100    = x+50
Status quo → 100+100 = 200 (certain)
```
Switching is valuable iff `½(2x+100) + ½(x+50) > 200`, i.e., `x > 83⅓`. **This is $16.67 lower than the naive $100 threshold** — the option to abandon a bad experiment mid-course (reversibility) lowers the bar for trying it, because the downside is bounded while the upside is not.

**Pricing the option itself (slide 12):** at x = $90 (good outcome $140/day, bad outcome $40/day), expected profit *with* the option to switch back = ½(2×90+100) + ½(90+50) = ½(280)+½(140) = **$210**. Without the option (must commit for both days regardless): ½(280)+½(80) = **$180**. **Option value = $210 − $180 = $30.**

**Harder self-study version, with discounting (slides 16–18):** a $2M/yr proprietary process for 5 years at IRR=10% has NPV = 2 + 2/1.1 + 2/1.1² + ... + 2/1.1⁴ = **$8.34M**. An experimental alternative yields $(x+1)M or $(x−1)M/yr with equal probability. Switching (with the ability to revert after year 1) is valuable iff `½(x−1+6.34) + ½(x+1)(1+1/1.1+...+1/1.1⁴) > 8.34`, solving to **x > $1.39M** (vs. a naive $2M threshold). At x=$1.5M: option value = $8.63M (with reversibility) − $6.25M (without) = **$2.38M**.

**Punchline:** *reversibility is itself economically valuable* — it's exactly the real-options idea from Hermalin §1.5 (Class 1 Theory Notes §6), just applied to abandoning a bad bet mid-stream rather than delaying a launch.

### 4. Airline jet-fuel hedging (slides 25–29) — opportunity cost is about the *decision*, not the *paperwork*

Southwest can buy options to purchase jet fuel at $1.50/gallon. A route breaks even at $1.51/gallon. Current spot = $1.50/gallon; it may rise to $2 or fall to $1, equally likely.

**Unhedged:** if price rises to $2, buying at spot to operate costs −$0.49/gallon (below breakeven) → drop the route, payoff $0. If price falls to $1, operating nets **+$0.51/gallon**.

**Hedged (holds $1.50 options):** if price rises to $2, Southwest can *exercise the option, resell the fuel at $2* → **+$0.50/gallon** even without flying the route, or exercise-and-operate for a thin $0.01/gallon. If price falls to $1, the option is worthless (let it lapse) and buy at spot for the same **+$0.51/gallon** as the unhedged case.

> **Result (as stated on the slide):** *Although Southwest's acquisition cost of fuel depends on whether it has hedges, its opportunity cost reflects the spot price in either case.* Whether or not you hedged, the "true" cost of using a gallon of fuel today is always what you could get for it on the open market right now — exactly Hermalin's chemical-inventory logic below.

---

## Part B: Introduction to Economic Costs

### 5. Make-or-buy and the opportunity cost of "free" resources (slides 20–24)

**Setup:** Building an HR dashboard internally needs $75K of cloud services (market price) + 1,800 engineering hours at $125/hr = $225K labor, total **$300K**. An external developer bids **$250K**. → *Buy* (cheaper).

**Twist — "the friendly cloud provider":** you haven't hired the developer yet, and a friend offers the $75K of cloud services *for free*. **An accountant's decision tree** (treating "free" as $0 cost) says: Buy = $1,000K−$250K = $750K net; Make = $1,000K−$225K (just labor, since cloud is free) = **$775K → make it yourself.**

**An economist's decision tree** recognizes the free cloud capacity itself has a market value **X** (you could resell it, or redeploy it to another project worth $X) — its *opportunity cost* is not zero just because you didn't pay cash for it:
```
Sell cloud & buy developer: $1,000K + X − $250K = $750K + X
Make it yourself:            $1,000K − $225K = $775K
```
**Conclusion: if X > $25K, sell the cloud capacity and hire the developer instead** — the accountant's "$775K > $750K, so make it yourself" answer silently assumed the free resource is worthless, which is almost never true.

### 6. Sunk cost — the second half of the "friendly cloud" story (slides 32–34)

Continuing the story: suppose you *did* choose to build it yourself, and — after already spending $75K on cloud (unused) and 200 hours ($25K) of labor — you learn about the $250K outside developer, with 1,600 engineering hours ($200K) still remaining to finish in-house. **What should you do now?**
- If you can resell the *unused* cloud capacity for at least $50K, you should hire the contractor (compare $200K remaining in-house labor vs. $250K − $50K resale = $200K net cost of the contractor — a wash or better).
- **The $25K of labor already spent is a sunk cost.** It has already been "burned," cannot be recovered, and does *not* affect any forward-looking comparison between the remaining alternatives — it should be ignored entirely, even though it *feels* relevant.

**The sunk-cost fallacy** (slide 34): the psychological pull to keep going because of what you've *already* invested — "what does this imply about project champions?" (they're the people least likely to objectively recognize their own project's sunk costs), the price of a movie ticket for a bad movie, or money already paid for a vacation/hobby/training. "The sunk-cost fallacy has a powerful pull, and it takes lots of discipline to resist it."

**Opportunity cost vs. expense** (slide 31): these are *not* the same axis. For a full-time MBA: tuition and books are *both* a cost and an expense. Your forgone salary is a **cost, but not an expense** (no cash leaves your pocket, but you still give up real value). Room & board would have been paid whether or not you got the MBA, so it's an **expense, but not an opportunity cost** of the MBA decision.

**Summary slide (35):** Two different jobs get done with "expenses" — record-keeping (accounting) vs. decision-making (economics). Two key differences between economists and accountants: (1) accountants are less able/willing to recognize opportunity costs; (2) accountants are not allowed to ignore sunk costs (GAAP requires recording historical cost). **Separating accounting objectives from decision objectives is critical.**

### 7. Hermalin's formal treatment of opportunity cost (Ch. 3.1, pp. 37–41)

> **Opportunity cost:** the value of the most highly valued forgone activity or use of a good.

**The chemical-inventory example (p. 37):** you bought 1,000 liters of a chemical at $10/liter ($10,000 spent). Before you use it, the market price jumps to $11/liter. **The cost of using it is not your $10,000 expenditure, but $11,000** — your true next-best alternative is selling it at the new market price. If producing with it yields only $10,500 of product, you've actually taken an **$500 loss** relative to selling it (not a "$500 profit" relative to your original $10,000 cost) — the difference between the naïve expenditure view and the correct opportunity-cost view is exactly $11,000 − $10,500 vs. $10,500 − $10,000.

Two derived concepts:
- **Imputed cost:** a cost not tied to any expenditure (e.g., the $11,000 above — you don't pay anyone $11,000, but using the chemical still costs you that much).
- **Sunk expenditure:** an expenditure already made — or one you'll incur *regardless of which relevant alternative you choose* — over the relevant decision-making horizon. Not a cost, because it can't be avoided by any available choice. *"There is no point crying over spilled milk."*

**Formula:** `Cost = Expenditures − Sunk Expenditures + Imputed Costs`

**Worked examples directly from Hermalin (useful vocabulary for the case notes):**
- *Ex. 1 — Store lease:* rent ($5,000/mo, locked in 6 more months) is sunk; true opportunity cost of staying open is only the *avoidable* $3,000/mo difference between staying open ($8,000 total expenditure) and shutting down ($5,000, just the rent). Even though staying open "loses" $2,000/mo on paper (revenue $6,000 − expenses $8,000), staying open is *better* than shutting down by $3,000/mo, since shutting down still costs the full $5,000 rent.
- *Ex. 2 — Theater tickets:* nightly expenses ($3,000) are sunk once the show is running; the right price to quote a charity buying out the house (300 seats) is **not** $3,000 but $5,000 — the forgone *revenue* from the 100 tickets you'd otherwise sell at $50 each.
- **Result 10:** *If, within the set of relevant decisions, an expense is unavoidable, then it is not a cost.*
- *Ex. 3 — Warehouse:* whether a $500,000 renovation is a "cost" of selling the warehouse depends on your *next-best alternative use* — if the warehouse would otherwise sit idle, the $500K is a real cost of the sale; if your next-best alternative is to use the (now-usable) warehouse yourself for $600K of value, the $500K would be spent either way and is **not** a cost of the sale.
- **Result 11 (Cost causation):** *If a decision causes you to incur an expense you wouldn't incur under the next-best alternative, that expense is a cost of the decision (caused by it). If the expense would be incurred anyway under the next-best alternative, it is not a cost of the decision.*
- *Ex. 4 — Gasoline "price gouging":* when wholesale gas prices rise, stations raise retail prices on gas already sitting in their tanks — not price gouging, but opportunity cost: the "old, cheap" gas is a perfect substitute for "new, expensive" gas and could be resold wholesale at the new price, so its true cost today equals the new price.
- *Ex. 5 — Free hotel rooms:* a conglomerate that owns a hotel doesn't get free rooms for its executives just because it "owns" the asset — if the hotel sells out anyway, the true cost per room is the $250 forgone from an outside guest, not the $50 marginal maintenance cost.

### 8. Cost concepts — total, average, marginal (Ch. 3.2, p. 41–42, previewing Class 3)

- **Overhead (fixed) cost:** incurred by operating, doesn't vary with units produced.
- **Variable cost:** varies with each unit produced.
- **Average cost (AC):** total cost ÷ units produced, `AC = C/x`.
- **Marginal cost (MC):** the *additional* cost of producing one more unit — the correct concept for *how much* to produce, because "the cost of an activity is the value of the next-best alternative," and stopping at unit 19 (say) only saves you the 20th unit's marginal cost, not the average.

**Worked example (Hermalin's Ex. 6, p. 42):** a firm with $100/day fixed maintenance, $5 material + $8 labor + $2 shipping = $15/unit variable, considers an order for 20 units at $21/unit: profit = (20×$21) − (20×$15+$100) = $420−$400 = **$20**, accept. A *second* order arrives afterward for 10 more units at only $18/unit. Using (wrong) average cost of $20/unit ($400/20), you'd reject it as a $2/unit loss. Using the *correct* marginal cost of $15/unit (maintenance is already sunk for the day), you'd accept it: (20×$21+10×$18) − (30×$15+$100) = $606 − $550 = **$56 total profit**, i.e., **$50 more** than stopping at the first order (extra profit on the 2nd order = $56−$20 = $36, or $3.60/unit above the $15 marginal cost). **This "marginal cost, not average cost" theme is the central topic of Class 3.**

## Cross-cutting themes / Punchline

1. **Opportunity cost is "what you give up," not "what you paid."** Every worked example this class — the free cloud, the hedged jet fuel, the chemical inventory, the "free" hotel room — makes the same point from a different angle: an asset's cost for decision purposes is its best forgone alternative use, which can be far from (above or below) its historical purchase price or accounting book value.
2. **Sunk costs should be ignored going forward, full stop** — but accountants *can't* ignore them (GAAP requires expensing/depreciating historical costs), which is precisely why "the accountant's answer" and "the economist's answer" diverge in the HR-dashboard example.
3. **Reversibility (real options) has real economic value**, and can be quantified the same way information is valued (Class 1): compare the best achievable expected payoff *with* the contingent flexibility to the best payoff *without* it.
4. **Risk aversion changes, but does not eliminate, the decision-tree machinery** — it just means you compare certainty-equivalents (which can be less than EV) rather than raw expected values. This becomes directly relevant to whether Merck should "wait" (a risky, high-variance branch) or "launch now" (a certain payoff) — see the companion Case Studies notes.

---

## Gulsher questions (along with clarification)

*(none yet — add here when you have follow-up questions on Class 2)*
