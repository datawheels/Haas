# Class 4 Case Studies — In-Depth Notes (Chapter 16: Statistical Tests)

## Suggested study order
1. Chapter-16.pdf (core theory — see companion "Theory Notes.md")
2. Team Assignment 3 — "Free Shipping Isn't Free" (apply the five-step testing procedure to a real randomized pilot; this file works every number in the assignment through to a final numeric answer, computed directly from `meridian_customers.csv` rather than taken on faith from the printed table)

All figures below were computed directly from `meridian_customers.csv` (5,000 rows) using pandas/scipy — not transcribed from the assignment PDF — and they match the assignment's own printed pilot means/SDs exactly, confirming the dataset is the real data behind the case.

---

## 1. The business setup

Meridian Outfitters (fictional online outdoor-apparel retailer) piloted a more generous free-shipping offer last quarter: **2,468 randomly chosen customers** (`test_group = Treatment`, out of 5,000 total active customers) saw "free shipping over $50" instead of the standard "free shipping over $75." The remaining **2,532 customers** (`test_group = Control`) kept the $75 threshold. (Verified directly from the CSV: `value_counts()` gives exactly 2,468 Treatment / 2,532 Control — matches the assignment's stated pilot size precisely.)

**The tension:**
- **CMO:** wants the $50 threshold rolled out to everyone — pilot customers ordered more often.
- **Finance:** objects — pilot customers paid **$4.72/order** in shipping fees vs. a historical **$6.62/order**, i.e. Meridian collects roughly **$4 less per customer per quarter** in shipping fees once the threshold drops to $50, and a perk is hard to claw back once customers have seen it.

**Verified directly from the data:** `shipping_cost_avg` — Treatment mean = **$4.7236**, Control mean = **$6.6238** — matches the assignment's $4.72 / $6.62 figures exactly. Per-order shipping-fee loss = $6.6238 − $4.7236 = **$1.90/order**; at the Treatment group's actual order rate (1.9194 orders/quarter), that's **≈ $3.65/customer/quarter** in forgone shipping revenue — close to the assignment's rounded "~$4" estimate.

## 2. Registering the test before touching the data

The assignment's core discipline (straight out of Chapter 15/16's "decide before you peek" theme): **commit to a metric, hypotheses, and an action threshold before looking at results.**

**Two competing metrics, each with planning-stage benchmarks (last year's same-quarter numbers):**

| Metric | Bar | Planning mean | Planning SD |
|---|---|---|---|
| Orders per customer (CMO's metric) | > 1.78 (any increase is a win) | 1.78 | 1.8 |
| Revenue per customer (Finance's metric) | > 170 (must clear the ~$4 subsidy cost) | 166 | 230 |

**Hypotheses (one-sided in both cases — both executives only care about an increase, not any decrease):**
```
Orders:   H0: μ_orders  ≤ 1.78     Ha: μ_orders  > 1.78
Revenue:  H0: μ_revenue ≤ 170      Ha: μ_revenue > 170
```
One-sided because the business question is directional — "does the pilot beat the bar," not "is the pilot different from the bar in either direction." (Chapter 16, §4 of the Theory Notes: when the question really is two-sided, you'd report a CI instead — which is exactly what the assignment's second half asks for, see §6 below.)

**Type I vs. Type II error costs, in this business:**
- **Type I error (roll out when it shouldn't have):** Meridian locks in a permanent ~$4/customer/quarter shipping subsidy for no real revenue gain — a recurring margin hit, and "hard to take back once customers have seen it."
- **Type II error (don't roll out when it should have):** Meridian leaves real incremental revenue on the table and keeps a stricter shipping threshold than its true economics would support — an opportunity cost, but a reversible one (you can always test again or roll out later).

**Action thresholds** (registered using the *planning* SD and n = 2,468, not the SD you'd see after peeking at the pilot — this is the point of registering in advance): `threshold = bar + z_α × SD/√n`, with z_{0.05} = 1.6449 for a one-sided α = 0.05 test:
```
Orders threshold:  1.78 + 1.6449 × 1.8/√2468  = 1.78 + 0.0596 = 1.8396 ≈ 1.84 orders
Revenue threshold: 170  + 1.6449 × 230/√2468  = 170  + 7.615  = 177.615 ≈ $177.62
```

## 3. Running the registered test

**Computed directly from the CSV (Treatment customers only, n = 2,468):**

| Metric and bar | Pilot mean | Pilot SD | t-statistic | p (one-sided) |
|---|---|---|---|---|
| Orders per customer — bar 1.78 | 1.9194 | 1.8034 | **3.839** (df=2467) | **0.0000632** |
| Revenue per customer — bar $170 | $175.4127 | $230.9118 | **1.164** (df=2467) | **0.1222** |

(Both means/SDs match the assignment's printed table of 1.92 / 1.80 and $175.41 / $230.91 exactly — confirms the t-statistics and p-values above are the correct fill-ins for the assignment's blank columns.)

```
t_orders  = (1.9194 − 1.78)  / (1.8034/√2468)  = 0.1394 / 0.0363  = 3.839 → p = 0.0000632
t_revenue = (175.4127 − 170) / (230.9118/√2468) = 5.4127 / 4.6481 = 1.164 → p = 0.1222
```

## 4. Deciding twice — threshold rule vs. p-value rule

**Orders:**
- Threshold rule: pilot mean 1.9194 > action threshold 1.8396 → **act (reject H₀)**.
- p-value rule: p = 0.0000632 < α = 0.05 → **reject H₀**.
- **Agree.** Both rules say: orders clearly beat the bar.

**Revenue:**
- Threshold rule: pilot mean $175.41 < action threshold $177.62 → **don't act (fail to reject H₀)**.
- p-value rule: p = 0.1222 ≥ α = 0.05 → **fail to reject H₀**.
- **Agree.** Both rules say: revenue has not cleared Finance's bar with enough confidence.

**Why the two rules are always the same rule in different units:** the threshold rule is just the p-value rule re-expressed on the scale of X̄ instead of the scale of t. `threshold = bar + z_α × SE` is exactly the X̄-value whose t-statistic equals z_α — so "X̄ beats the threshold" and "t beats z_α" (equivalently, "p beats α") are the identical comparison, just before vs. after standardizing. This is precisely Chapter 16 §12's "decision rule" construction (the Nordex 29.51-ton cutoff), applied twice here.

## 5. "p = 0.12 proved the rollout doesn't pay" — what's wrong with that claim

A teammate says: *"revenue missed the bar, p = 0.12 — the pilot proved the rollout doesn't pay."* This is wrong on two counts (straight out of Chapter 16 §16's Pitfalls):

1. **p = 0.12 is not the probability that the rollout doesn't pay, and it isn't a probability about H₀ at all.** It's the probability of seeing pilot revenue *at least this far above $170*, if the true population mean were exactly $170 (or less). A p-value of 0.12 means the data are *not surprising enough* to clear the pre-registered 5% bar — that's **absence of (sufficiently strong) evidence**, not **evidence of absence**.
2. **"Fail to reject" ≠ "proved false."** The test retains H₀ because the data don't clear the threshold confidently — but H₀ ("revenue ≤ $170") could still be false; the pilot (n=2,468) may simply be underpowered to detect the true gap. (Quantified in §7 below: it is.)

The honest statement: *the pilot did not provide strong enough evidence, at the pre-registered 5% significance level, to conclude average revenue durably exceeds $170 — it's inconclusive on that specific bar, not a negative finding.*

## 6. The second AI prompt: basket size and the revenue confidence interval

**Two-sided test of `avg_order_value` against last year's $90.75:**
```
Pilot avg_order_value: mean = $88.5424, SD = $31.0693, n = 2468
SE = 31.0693/√2468 = 0.6254
t = (88.5424 − 90.75)/0.6254 = −3.530  (df = 2467)
p (two-sided) = 0.00042
```
**The basket got significantly smaller** — highly significant (p = 0.00042), and in the direction you'd expect: a lower free-shipping threshold ($50 vs. $75) means customers no longer need to bundle purchases into a single large order to qualify for free shipping, so they split the same overall spend into **more, smaller orders**. This is exactly the mechanism behind the CMO/Finance disagreement: **more orders, less per order** — both the CMO's "orders are up" and the shrinking average basket are the same underlying behavior change, just measured two different ways. Neither executive is wrong about the facts; they're emphasizing different facts.

**95% confidence interval for mean `revenue_90d`:**
```
mean = $175.4127, SE = $4.6481, t*(0.025, df=2467) ≈ 1.9609
95% CI = 175.4127 ± 1.9609 × 4.6481 = 175.4127 ± 9.1147
        = [$166.30, $184.53]
```

## 7. Three worlds — what the revenue CI does and doesn't rule out

**[$166.30, $184.53]** against the three benchmarks the assignment poses:
- **$166 (revenue roughly unchanged from last year):** falls just **below** the lower bound (166.30 > 166) — *technically* excluded, but only by $0.30 against a standard error of $4.65 (a fifteenth of one SE) — this is not a meaningful exclusion; "essentially flat revenue" is still well within the data's noise band.
- **$170 (exact breakeven on the subsidy):** falls **inside** the interval — **not ruled out**.
- **$178 (a rollout that pays for the $4 subsidy three times over):** falls **inside** the interval — **not ruled out**.

**What this leaves the CFO deciding on:** the interval is wide enough to be statistically compatible with almost the entire plausible range, from "this barely moved the needle" to "this comfortably pays for itself several times over." The data **cannot distinguish** a mediocre rollout from a great one — which is a *sample-size* problem, not a flaw in the test.

## 8. Why the revenue test is ambiguous — a power calculation (ties back to Chapter 16 §13–14)

Exactly the same lesson as the Nordex wind-turbine pilot in the Theory Notes (where n=40 gave only 56% power to detect the targeted effect): check what size of true revenue lift this pilot (n=2,468, planning SD=$230, α=0.05 one-sided, 80% target power) could actually have been expected to detect.

```
Minimum detectable effect (MDE) at n=2,468:
  MDE = (z_α + z_β) × σ/√n = 2.4865 × 230/√2468 = 2.4865 × 4.6300 ≈ $11.51

→ At 80% power, this pilot could reliably detect a revenue lift of about $11.51 or more above the $170 bar.
→ The actual observed gap was just $5.41 above the bar (175.41 − 170) — well under the minimum detectable effect.
```
Equivalently, solving the other direction — the sample size that *would* have been needed to detect the observed $5.41 gap at 80% power:
```
n_required = [(z_α+z_β) × σ/δ]² = (2.4865 × 230/5.41)² ≈ 11,175 customers (per arm)
```
**The revenue test wasn't underpowered by accident — the true effect (if any) is simply small relative to revenue's enormous customer-to-customer noise (SD ≈ $231, versus a mean of ~$175).** The pilot had plenty of power to catch the orders effect (which is large relative to its own noise: SD 1.80 vs. a shift of ~0.14 orders, yet still produced a p-value of 0.00006 — orders are a much "cleaner," lower-noise signal than revenue), but was never going to reliably resolve a single-digit-dollar revenue question with only ~2,500 customers per arm.

## 9. Bonus: the "proper" randomized comparison (a Chapter 17 preview)

The assignment's registered tests compare the Treatment pilot against **last year's historical benchmarks** (1.78 orders, $170 revenue) — but the dataset also contains a **true randomized Control group** (n=2,532, same quarter, standard $75 threshold), which is the methodologically cleaner comparison (removes any seasonal/year-over-year confound). Computed directly as a two-sample Welch t-test, previewing Chapter 17 (Comparisons/A-B Testing, next class):

```
Orders,  Treatment vs. Control:  mean diff = 1.9194 − 1.7816 = 0.1378,  t = 2.737,  p = 0.0062  → significant
Revenue, Treatment vs. Control:  mean diff = 175.41 − 165.83 = 9.58,    t = 1.464,  p = 0.1432  → not significant
```
Same qualitative story as the registered one-sample tests: **orders up, significantly; revenue up, but not significantly** — reassuring, since it means the conclusion doesn't hinge on which comparison benchmark (last year's historical average vs. this quarter's randomized Control group) you pick. The randomized Treatment-vs-Control revenue gap ($9.58) is bigger than the one-sample gap over the $170 bar ($5.41), and would need n ≈ 3,595 per arm for 80% power — still above the actual 2,468, but much closer to adequate than the $170-bar comparison. This is a hint that Finance's $170 bar (bar + subsidy) is a harder target to clear with this sample size than simply "beat the Control group."

## 10. Recommendation to the CMO

**Not a clean go or no-go — "something else": extend the pilot (or pool more quarters) before a full rollout commitment, with revenue as the pre-registered decision metric.**

Reasoning:
- The **orders** evidence is unambiguous (p = 0.00006, both rules agree, holds up under the randomized Treatment-vs-Control comparison too) — customers genuinely order more often under the $50 threshold.
- The **revenue** evidence is genuinely inconclusive, not negative — the pilot is underpowered (§8) to distinguish "roughly breakeven" from "pays for itself three times over" at the sample size collected. A premature rollout risks locking in a permanent $3.65–4/customer/quarter shipping subsidy (Type I error, per §2) without knowing whether the extra orders actually cover it.
- The **basket-size shrinkage** (§6) confirms the mechanism driving both results — customers are splitting orders to hit $50, not necessarily spending more overall — which is exactly the kind of behavior that a longer pilot window (capturing more full purchase cycles, not just split orders) could help resolve.
- Concretely: run the pilot roughly **4–5× longer, or recruit a similarly sized additional cohort**, to get into the n≈11,000-ish range (§8) needed to resolve the revenue question with 80% power at the $170 bar — or, more practically, ask whether Finance would accept resolving the lower bar of "beats Control" (n≈3,600, §9) as the decision criterion instead, which is within reach of a moderately extended pilot.

---

## Cross-cutting themes
1. **A statistical test's threshold rule and its p-value rule are the same comparison in different units** — one is phrased on the scale of the raw statistic (X̄ vs. an action threshold), the other on the scale of significance (p vs. α). Registering the action threshold *before* the test, as this assignment requires, makes that equivalence concrete rather than abstract.
2. **"Fail to reject" is not "proved false," and a p-value is not the probability H₀ is true** — the revenue test (p=0.12) is the textbook illustration from Chapter 16's Pitfalls slide, not a hypothetical: the honest read is "inconclusive, probably underpowered," not "the rollout doesn't pay."
3. **Statistical significance tracks signal-to-noise, not importance** — the orders metric (small shift, but tiny noise relative to that shift) produced an overwhelming p-value, while the revenue metric (larger absolute shift, but enormous customer-to-customer noise) produced an ambiguous one. The business importance of the two metrics is arguably reversed from their statistical clarity.
4. **An underpowered test and a true null look identical from the outside** — exactly the Nordex pilot's lesson in the Theory Notes (n=40 giving only 56% power), replayed here at business scale: a $2,468-customer pilot sounds large, but whether it's *adequately* large depends entirely on the effect size relative to the outcome's noise, which is a calculation you have to actually do (§8), not an intuition you can eyeball from n alone.
5. **Two business leaders can look at the same randomized pilot and reach opposite conclusions without either being wrong about the facts** — the CMO (orders) and Finance (revenue/basket size) are both reading real, correctly-computed signals; the disagreement is about which bar matters, not about the arithmetic. Registering a single pre-committed metric and threshold (§2) is precisely the discipline that prevents this from becoming a post-hoc argument over which number to believe.
