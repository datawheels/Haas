# Class 2 Case Studies — In-Depth Notes

Three items, covering both halves of Class 2 (decision making under uncertainty, then introduction to economic costs). See companion "Theory Notes.md" for the underlying decision-tree, real-options, and opportunity-cost machinery each case draws on.

## Suggested study order
1. Merck Pharma and Covid Vaccines (decision trees, value of information, risk aversion)
2. Why Merck Is Betting Big on One Cancer Drug (R&D allocation under risk)
3. Pasona — Farms in Downtown Tokyo (opportunity cost)

---

## 1. Merck Pharma and Covid Vaccines

Source: `Merck Pharma and Covid Vaccines.pdf` (Prof. Steve Tadelis case). **The user has already built a full worked decision tree for this case** in `Merck Decision Tree.md` and `Merck Decision Tree (Mermaid).md` in this folder — this section summarizes and interprets that existing work rather than re-deriving it, and answers the four discussion questions class.md poses.

### Background
September 2020: Dr. Patricia Okuna, R&D director at Merck, must decide whether to move forward now with the current Covid vaccine ("Version A") or delay 3 months for a possibly-better "Version B." Merck estimates: 50% chance B materializes as an effective vaccine; if it does, 40% chance of **high efficacy** ($5.60/dose profit) vs. 60% chance of **mediocre efficacy** ($2.00/dose profit if sold in-house, or a licensing option worth half as much, $1.00/dose, that "protects Merck's reputation"). If B fails to materialize (50%), the 3-month delay still lets Merck refine Version A, yielding one of three scenarios: weak competition ($3.50, p=.4), strong competition ($3.00, p=.4), or merely "good but not very good" efficacy regardless of competition ($2.50, p=.2). Proceeding immediately with Version A is a **certain** $2.85/dose.

### Q1 — Order of events and decisions; draw the tree
Per the existing `Merck Decision Tree (Mermaid).md`: **Decision 1** — launch A now (certain $2.85) or wait 3 months (chance node). If wait: **Nature** resolves whether B succeeds (p=.5) or fails (p=.5). If B succeeds: **Nature** resolves efficacy — high (p=.4, terminal $5.60) or mediocre (p=.6, leading to **Decision 2**: sell in-house $2.00 vs. license $1.00). If B fails: **Nature** resolves the refined-A competitive scenario (weak $3.50 p=.4 / strong $3.00 p=.4 / good-not-very-good $2.50 p=.2, all terminal). Solving by backward induction (as worked in the existing file): EV(succeed branch) = .4(5.60)+.6(2.00) = **3.44**; EV(fail branch) = .4(3.50)+.4(3.00)+.2(2.50) = **3.10**; EV(wait) = .5(3.44)+.5(3.10) = **3.27**. Since 3.27 > 2.85, **wait for Version B**, and if B turns out mediocre, **sell in-house rather than license** ($2.00 > $1.00, even though licensing "protects reputation" — the case treats the $1.00 licensing payoff as already net of that reputational benefit, and it's still dominated).

### Q2 — What judgment calls / ambiguities does building this tree require?
Several assumptions are baked in that the case doesn't fully defend, and are worth flagging explicitly (this is exactly the "identify critical assumptions" discipline from Class 1 Theory Notes §1):
- **Independence assumption:** the model treats "does B succeed" and "what happens to refined-A's competitive position" as two separate, unconnected chance events. In reality a competitor's vaccine progress driving B's fate might *also* affect A's competitive landscape (correlated states of the world), which the tree ignores.
- **The reputation cost is folded silently into a single number.** Licensing a mediocre B yields exactly half the in-house profit ($1.00 vs $2.00) and is described as "protecting reputation" — but the tree has no separate branch for the *reputational damage* of selling a mediocre vaccine in-house; it's implicitly assumed to already be netted into the $2.00 figure (or ignored). A more complete tree might carry reputation as its own state variable affecting *future* (not just this) decisions.
- **Discretizing efficacy into two states** ("high" vs. "mediocre" for B; "weak/strong competition" and "good-not-very-good" for refined A) is a modeling simplification — a continuous efficacy/competition spectrum is collapsed to make the tree tractable, per the Class 1 "toy model" methodology.
- **The probabilities themselves (.5, .4/.6, .4/.4/.2) are Dr. Okuna's team's subjective estimates**, not objective frequencies — a classic case of the "$64K question: values and probabilities?" flagged on Lecture 2 slide 2. Different reasonable estimates would move the wait-vs-launch conclusion, so a sensitivity/robustness check (as Class 1's methodology recommends) is warranted before committing.
- **The tree assumes profits are quoted on a per-dose basis independent of volume/capacity** — it implicitly ignores production capacity constraints or how fast each version could actually be manufactured and distributed.

### Q3 — How much would it be worth to know ahead of time if B will succeed?
Apply the **Fundamental Rule of Information** (Theory Notes, Class 1 §5, Hermalin Result 1): information has value *only if it has the potential to change your action*. Check both possible worlds:
- **Told B will succeed:** best action is still "wait," worth 3.44 (vs. 2.85 for launching now) — same choice as without the information.
- **Told B will fail:** best action is still "wait" (to get the refine-A benefits), worth 3.10 (vs. 2.85 for launching now) — again the same choice.

**Because "wait" dominates "launch A now" in *both* possible worlds, learning B's fate ahead of time does not change the top-level wait-vs-launch decision at all** — which is exactly why this information carries very little value, consistent with Hermalin's **Result 3** (value of information is maximized at indifference, and here the two branches, 3.44 vs 2.85 and 3.10 vs 2.85, are *not* close to indifferent — wait wins comfortably either way). This matches the professor's own stated answer on Lecture 2 slide 4: *"Value of knowing if B will succeed? 1 cent loss per vaccine saved, but only with probability 0.5!"* — i.e., the information is worth only a fraction of a cent per dose in expectation (0.5 × $0.01 × quantity), a small, second-order value coming from finer execution/timing decisions within the "wait" branch (e.g., how much to invest in refining A while waiting), not from flipping the overall wait/launch call.

### Q4 — Would the decision maker's degree of risk aversion possibly change their choices?
Yes. "Launch A now" is a **certain** $2.85. "Wait" has expected value $3.27 but a **wide spread** of possible outcomes ranging from $1.00 (license a mediocre B) up to $5.60 (B succeeds with high efficacy) — a materially riskier prospect. Under risk aversion (Theory Notes §1, Hermalin Definition 3: CE ≤ EV, with CE < EV for at least some gambles), Dr. Okuna's **certainty-equivalent** value for the "wait" branch could fall below its $3.27 expected value — and if her risk aversion is strong enough, her CE for waiting could drop below $2.85, **flipping her choice to "launch A now" despite its lower expected value.** This is the general lesson that Class 1's "don't confuse decision quality with outcome quality" needs a companion warning: *optimal decisions for a risk-neutral EV-maximizer are not necessarily optimal for a risk-averse decision maker* — the whole tree's recommendation is conditional on the (unstated) assumption that Merck's leadership is risk-neutral.

---

## 2. Why Merck Is Betting Big on One Cancer Drug

Source: `Why Merck Is Betting Big on One Cancer Drug.pdf` (WSJ, Peter Loftus, April 15, 2018).

**The facts:** Merck's Keytruda (a cancer immunotherapy) generated **$3.8 billion** in global sales in 2017 (≈9% of Merck's total revenue), backed by **more than 700 clinical trials across 30+ cancer types** — more trials than any other cancer drug, commanding "more than half of Merck's budget for all clinical drug studies." R&D chief Roger Perlmutter: *"Whatever other projects you're working on, you can stop now, because we're going to be doing this, and we're going to put a lot of muscle behind this."* Merck shed other projects (e.g., licensed away an experimental psoriasis drug) to fund the pivot. Analysts (Credit Suisse) projected Keytruda sales would surpass **$10 billion by 2022** (22% of Merck's total revenue) — and the sales chart on the article shows the trajectory from **$55M (2014) to a projected $29.5B (2024)**, an almost 550× increase in a decade.

### Q1 — Why is Merck shifting R&D resources to Keytruda?
Early clinical data showed Keytruda shrinking tumors effectively across a wide range of cancer types, and competitive pressure was acute: rival Bristol-Myers Squibb had already released positive results for its own immunotherapy, Opdivo. Perlmutter's own framing is a **corner-solution R&D bet**: rather than spreading effort thinly "to bring as many drugs to market as they could" (the pre-Keytruda strategy per consultant Bernard Munos), Merck concentrated resources on the single highest-conviction, highest-payoff opportunity. This is a real-world instance of the R&D-allocation problem posed in Q2 below — and the actual data (sales growing ~500×) suggest the bet paid off, though the article also notes real downside risk realized along the way (the FDA halted two Keytruda trials in blood cancer after excess patient deaths; some studies, e.g., in gastric cancer, showed no survival benefit).

### Q2 (harder) — Optimal R&D allocation for a risk-neutral monopoly with two drugs
**Setup:** total R&D time normalized to 1, split r₁ + r₂ = 1 across two drugs. Drug *i* succeeds with probability pᵢ(rᵢ) (increasing in rᵢ) and pays off xᵢ if successful. A risk-neutral monopoly maximizes expected total payoff:
```
max over r₁∈[0,1]:  p₁(r₁)·x₁ + p₂(1−r₁)·x₂
```
**Interior optimum (if one exists):** taking the first-order condition with respect to r₁ gives
```
p₁′(r₁)·x₁ = p₂′(r₂)·x₂
```
i.e., allocate R&D time until the **marginal expected payoff** from the last unit of time is equalized across both drugs — the same "equate at the margin" logic that runs through this entire course (Class 1 Theory Notes §1: "compare costs and benefits at the margin").

**How the *shape* of pᵢ(rᵢ) determines whether the optimum is interior (diversified) or a corner (all-in on one drug):**
- If both p₁ and p₂ are **concave** in their own rᵢ (diminishing marginal returns to research effort — the first few million dollars of R&D buy more incremental success probability than the next few), the equal-marginal-return condition typically has a well-behaved **interior solution**: some time devoted to each drug.
- If pᵢ(rᵢ) is **convex or S-shaped** over some range (increasing marginal returns — e.g., a drug needs a "critical mass" of research investment before probability of success rises sharply, perhaps because partial-scale trials are uninformative or subscale research teams can't reach key thresholds), then the objective function can be **maximized at a corner** (r₁=1, r₂=0, or vice versa) rather than in the interior — it becomes optimal to go "all in" on the drug whose marginal returns are accelerating fastest, exactly the pattern Merck's real behavior displays.
- The payoff levels xᵢ matter too, independent of curve shape: a very large payoff advantage (x_Keytruda evidently enormous, given the $55M→$29.5B trajectory) can make even a modest edge in p′(r) decisive enough to justify a corner solution.

**Takeaway:** Merck's real-world "bet the company" concentration on Keytruda is only optimal for a risk-neutral firm if pKeytruda(r) exhibits increasing/convex returns to R&D investment near the observed allocation, and/or xKeytruda is disproportionately large relative to its alternatives — both plausible given the article's framing of Keytruda's differentiated, rapidly-scaling commercial trajectory.

### Q3 — How would a risk-averse company allocate differently?
A risk-neutral firm cares only about maximizing E[p₁x₁+p₂x₂] and is indifferent to how that expected payoff is *distributed* across possible outcomes. A **risk-averse** firm (Theory Notes §1: CE ≤ EV) cares about variance too — and concentrating all R&D on a single drug maximizes the variance of the firm's total R&D outcome (success or failure of that one drug now determines the entire portfolio's payoff), exactly the same logic as the Merck-vaccine "wait" branch being riskier than "launch now" in the Covid case above. A risk-averse decision maker would therefore be willing to accept a **lower expected total payoff** in exchange for **diversifying** R&D effort across both drugs (moving r₁ away from a risk-neutral corner solution toward a more interior split), so that a single clinical failure doesn't wipe out the whole bet — the same portfolio-diversification intuition behind Hermalin's Chapter 2.2, "Diversification" (spreading risk across imperfectly-correlated bets lowers the variance of the combined outcome without necessarily lowering its expected value by much, provided the bets aren't perfectly correlated).

---

## 3. Pasona — Farms in Downtown Tokyo

Source: `pasona.pdf` (Prof. Benjamin Hermalin case, "Farms in Downtown Tokyo?!").

**The facts:** Pasona is a Japanese HR/staffing firm (¥182B forecast sales, ¥8.12B forecast operating income for FY2005). CEO Yasuyuki Nambu, concerned about youth unemployment and the "freeter" (young, career-less part-time worker) problem, built an experimental 1,000-square-meter farm — six climate-controlled, artificially-lit rooms, each growing a different crop (e.g., Room 3: rice) — in the **basement of Pasona's own headquarters** in Otemachi, one of downtown Tokyo's most prominent (and expensive) commercial districts. When Prof. Hermalin asked about the farm's annual cost, his guide said labor was "largely free" (urban youth volunteers learning to farm), minor costs covered seed/water, and **80–90% of the total ¥20 million/year cost was electricity** for grow-lights and climate control. Hermalin was "fairly confident the true annual cost was far greater than ¥20 million" — the case ends by asking why.

### Q1 — What enters the costs of the Downtown farm?
As reported: (1) electricity for artificial lighting (each room needs light "especially designed for the crop being grown... in some rooms it seems brighter than the sunniest day") and for maintaining room-specific temperature/humidity (e.g., Room 3's rice needs both kept high) — the dominant reported cost at 80–90% of ¥20M, i.e., roughly ¥16–18M/year; (2) minor consumables — seed, water, and similar farming necessities (no pesticides needed, since the sealed rooms exclude pests); (3) labor, described as "largely free" because it's urban youth learning to farm rather than paid staff.

### Q2 — What might be the largest opportunity cost (and why is the ¥20M figure almost certainly understated)?
Apply Hermalin's own Chapter 3 framework directly (Theory Notes §7, Example 5 — the "free" hotel room for executives, and Example 3 — the warehouse): **an input being "free" in a cash sense does not make it free in a cost sense.** Two inputs are treated as costless in the ¥20M estimate but almost certainly are not:
1. **The 1,000 m² of basement space itself.** Pasona's headquarters sits in Otemachi — commercial real estate there is among the most expensive in the world. The ¥20M estimate implicitly assumes the space has zero opportunity cost simply because Pasona already owns the building and isn't paying rent for the farm specifically — exactly the accounting fallacy Hermalin warns against with the hotel-room example ("unless there is no alternative use of the asset, its use is not free... the cost of using it is the value of its next-best use"). The next-best use of 1,000 m² of prime downtown Tokyo office space — leasing it out, or using it for additional high-value HR/staffing office operations — is almost certainly worth **far more** than the entire reported ¥20M annual cost of the whole farm, and is very likely the single largest true cost.
2. **The "largely free" youth labor.** Even unpaid participant time has an opportunity cost equal to what those participants would otherwise be doing (working, studying, or being trained elsewhere) — treating it as $0 cost, rather than imputing some value to it (Theory Notes §7's "imputed cost" concept), likely understates true cost further, though probably by far less than the real-estate omission.

**Bottom line:** the ¥20M figure captures only the *cash expenditures* (mostly electricity) and misses the dominant **imputed opportunity cost of prime downtown real estate** — precisely the "Cost = Expenditures − Sunk + Imputed Costs" formula from Theory Notes §7. This is likely why Prof. Hermalin, despite loving the tomatoes and lettuce, was "much less content with the cost estimate" — the true economic cost of the Pasona Gardens is almost certainly a multiple of the reported ¥20M once downtown Tokyo real-estate opportunity cost is properly imputed.

---

## Cross-cutting themes
1. **"Free" is a decision-making red flag, not a green light.** Every case this class (the cloud provider in Theory Notes §5, the hotel rooms in §7, and Pasona's "free" space and labor here) makes the identical point: cash cost of zero does not imply economic cost of zero. Always ask "what is the next-best use of this input?"
2. **Risk aversion can flip decisions that look clear-cut under expected-value maximization** — both the Merck vaccine choice (wait vs. launch) and the Merck R&D-allocation choice (concentrate vs. diversify) have this exact structure: a risk-neutral analysis favors the higher-variance, higher-EV option, but a sufficiently risk-averse decision maker would choose differently, and real firms are rarely purely risk-neutral (especially when a bad outcome threatens the whole company, as a failed "bet the company" R&D strategy would for Merck).
3. **The value of information depends on whether it can change your action, not on how "important" the underlying uncertainty feels** — the Merck Covid case is the cleanest illustration: learning whether Version B will succeed *feels* like it should be extremely valuable, but because "wait" already dominates "launch now" in both possible worlds, that specific piece of information turns out to be worth almost nothing at the level of the wait/launch decision.
