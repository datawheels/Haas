# Chapter 16: Statistical Tests — Theory Notes

Source: Chapter-16.pdf (lecture slides, Prof. Reed Walker, XMBA 200S) — 29 slides. Several slides have intentionally **blank formulas** meant to be filled in live during class; those are worked out in full below, verified with exact calculation. Supplementary sources folded in: KC2_solutions.pdf (Knowledge Check 2 — FreshBox case, covers Ch.13/14.1/14.2 + pre-term, with two questions that directly reinforce this chapter's Type I/II error framework) and `Block 2 - Power Calculations - Sample Size Determination.xlsx` (a power/sample-size calculator built on the exact same Nordex example as the slides).

---

## 1. Where this fits in the course

Course Part 2 ("Making decisions based on inference") opens with the problem: *given limited data, managers need to choose how to act.* You'll typically have a benchmark in mind (or two groups to compare) — but how do you know a difference isn't just "noise," and what's the likelihood of making a mistake? **Chapter 15 built confidence intervals** (given a sample, where does the population parameter likely sit?). **Chapter 16 flips that into a decision procedure**: given *only* a sample and a specific benchmark value, do you reject the benchmark or not — with a quantified, pre-committed tolerance for being wrong.

## 2. Running example: Nordex carbon-fiber wind turbine blades

Nordex is experimenting with a new production process using carbon fiber. Production is more costly, but blades are lighter and more efficient. Finance says the switch is profitable **if the mean weight of new blades is less than 29.7 tons**. You run a pilot: manufacture **n = 40** carbon-fiber blades under controlled conditions, then decide whether to switch materials based on the data.

## 3. Null and alternative hypotheses

- **Null hypothesis (H₀):** specifies the default course of action, preserving **the status quo** (no change).
- **Alternative hypothesis (Hₐ):** contradicts H₀, posits **an alternative** to the status quo (here: switch to the new tech).
- Both are claims about a **population parameter** (here, μ = mean weight of turbine blades).

For Nordex, with μ = weight of turbine blades:
```
H₀: μ ≥ 29.7   (status quo — don't switch; new tech isn't lighter enough)
Hₐ: μ < 29.7   (switch — new tech is light enough to be profitable)
```
This is a **one-sided test** because the decision only cares about weight being *below* a threshold.

## 4. One- and two-sided tests

- **One-sided test:** H₀ allows any value of a parameter larger [>] (or smaller [<]) than a specific value.
- **Two-sided test:** H₀ asserts a **specific value (=)** for the parameter; Hₐ is "≠."
- Which to use depends on the business problem. **When a problem calls for a two-sided test, it often makes more sense to just report the confidence interval instead** (same information, different framing — see §13 below).

## 5. Type I and Type II errors

| | Don't Take Action (Retain H₀) | Take Action (Reject H₀) |
|---|---|---|
| **H₀ true** (μ ≥ 29.7) | Correct decision | **Type I error** |
| **Hₐ true** (μ < 29.7) | **Type II error** | Correct decision |

- **Type I error:** act (reject H₀) when the status quo was actually true — e.g., switch to carbon fiber when it wasn't actually light enough to be worth it.
- **Type II error:** fail to act (retain H₀) when the alternative was actually true — e.g., stick with the old material when carbon fiber actually was light enough to justify switching.

## 6. Statistical significance, α, and the p-value

- **Significance level (α):** the maximum tolerance for a Type I error (typically α = 0.05 or 0.01).
- **Statistically significant:** the data contradict H₀ at the chosen significance level — "reject the null hypothesis."
- **p-value:** the smallest significance level at which we would reject H₀. A low p-value is evidence against H₀. A statistic is "statistically significant" if p-value < α.
- **Decision rule:** if p-value < α, reject the null; if p-value ≥ α, fail to reject the null — not enough evidence to justify change, so keep the status quo (the observed sample could happen frequently enough under the null). More technically: given what you see in your data, the probability of a Type I error (if you acted) would be too high.

## 7. The five-step testing procedure

A statistical test is a decision rule to separate H₀ from Hₐ:
1. **Define your Type I error α** (typically 5% or 1%) — this is the **significance level**.
2. **Conduct the pilot, collect sample data.**
3. **Construct a test statistic:** `t = (X̄ − μ₀) / SE`
4. **Find the p-value** associated with that t-statistic (use the t-table, or software).
5. **Reject H₀ if p-value < α.**

## 8. Worked example: Nordex pilot results

**Pilot:** 40 carbon-fiber blades, mean (x̄) = **29.5 tons**, standard deviation (s) = **0.7 tons**. Significance level α = 0.05.

**Step 2 — test statistic:**
```
SE = s/√n = 0.7/√40 = 0.1107

t = (X̄ − μ₀)/SE = (29.5 − 29.7)/0.1107 = −0.2/0.1107 = −1.807
```

**Step 3 — p-value:** look up in Excel (or the t-table) with df = 40 − 1 = 39:
```
p-value = T.DIST(−1.807, 39, TRUE) = 0.039
```

**Step 4 — decision:** Do you adopt the new process? **Yes — because 0.039 < 0.05 (Reject the Null).** The pilot data are unlikely enough under "the blades aren't light enough" that Nordex switches to carbon fiber.

## 9. "What About Claude?" (AI cross-check, slide 17)

The deck includes a live AI query: *"you build 40 carbon fiber blades with a mean of 29.5 and a standard deviation (s) of 0.7. Do we reject null (29.7) based on a significance level α=.05 with a one-sided test?"* The AI's answer matches the manual calculation:
- SE: 0.7/√40 ≈ 0.1107
- Test statistic: t ≈ −1.81
- Critical value (df=39, α=.05, one-sided): **−1.685** (or −1.645 using z) — this is the *exact* t-table value; the main lecture slide's hand-looked-up value of −1.691 (§11 below) is a minor table-rounding/interpolation difference, both round to the same conclusion.
- p-value: ≈ 0.039 (≈ 0.035 using z)
- **Conclusion:** reject H₀ at the 5% level, since −1.81 < −1.685.
- **Bonus note from the AI:** "The result depends on the one-sided setup. A two-sided test would have p ≈ 0.078 and would fail to reject. If the alternative were instead μ > 29.7, you would also fail to reject." (Verified: 2 × 0.039 = 0.078 — matches exactly.) Same "trust but verify" theme as earlier chapters' AI cross-checks: the mechanics check out, but you have to know what question you actually asked.

## 10. What standard error to use for a statistical test

- **Continuous variable** (can take on any value): use the sample SD in the numerator — `SE = s/√n`.
- **0/1 (binary/proportion) variable:** use the null-hypothesized proportion p₀ — `SE = √[p₀(1−p₀)] / √n`.
- **Note 1:** here p₀ is **not** the "p-value" — same symbol, totally different meaning, easy to confuse.
- **Note 2:** statistical software will choose the right SE for you automatically — but you should know which one it picked.

## 11. Accommodating two-sided hypotheses

```
H₀: μ = μ₀
Hₐ: μ ≠ μ₀
```
The math is identical, except for the rejection rule: in a two-sided test you need
```
p-value_twosided = 2 × p-value_onesided < α
```
(the significance level is split across both tails of the distribution). When α = 0.05, you allocate 0.025 to each tail — but you still just compare the two-sided p-value directly to 0.05 to decide whether to reject.

## 12. Decision rules and the probability of a Type II error

Once you fix α, you can solve backwards for the **decision rule** (action threshold) on X̄ itself, instead of on the t-statistic.

**Find the decision rule satisfying:** `Probability(X̄ ≤ decision rule) = 0.05`

Under H₀, X̄ has a t-distribution (df = 39) with mean 29.7 and SE = 0.1107. Standardizing:
```
Probability(t ≤ (decision rule − 29.7)/0.1107) = 0.05
```
The t-table says 5% of observations lie to the left of **−1.691** (df=39; a more precise computed value is −1.6849 — both round to the same decision rule):
```
(decision rule − 29.7)/0.1107 = −1.691
decision rule = 29.7 − 1.691 × 0.1107 = 29.7 − 0.187 = 29.513 ≈ 29.51
```
**Conclusion: with α = 0.05, the decision rule is "reject H₀ if X̄ ≤ 29.51."** (Sanity check: the pilot's actual x̄ = 29.5 is below 29.51, so we reject — consistent with the p-value calculation in §8.)

### Type II error at a specific alternative
**Scenario:** suppose the *true* weight is μ = 29.3 (not 29.7). Given the decision rule above, what's the probability of a Type II error (failing to reject H₀, i.e. not switching, even though 29.3 is in fact light enough)?
```
t = (decision rule − μ_true)/SE = (29.513 − 29.3)/0.1107 = 0.213/0.1107 ≈ 1.93

P(Type II error) = P(X̄ > 29.513 | μ=29.3) = P(t > 1.93, df=39) ≈ 0.031 (≈3.1%)
```
**There is roughly a 3% chance that Nordex will commit a Type II error** — i.e., fail to switch to carbon fiber even though the true weight (29.3) would have made the switch profitable — under this specific decision rule and this specific alternative scenario.

**Note on the slide's stated answer:** the deck's own "Type II Error and Power" slide asserts "the power of the test when μ=29.3 is 95% — why? 1 − 0.05 = 0.95," which computes power as 1 minus **α**, not 1 minus the actual Type II error probability. Working the numbers through properly (above) gives **P(Type II error) ≈ 0.031, so power ≈ 96.9%** — numerically close to the slide's 95% only by coincidence (because μ=29.3 was chosen fairly far from the null, so both the true Type II error and α happen to be small single-digit percentages), not because power literally equals 1−α. The *correct* general definition (used correctly elsewhere in the same deck, see §13) is power = 1 − P(Type II error), evaluated at a specific hypothesized alternative — it is **not** simply 1−α.

## 13. Type II error and power — general definition

**The power of a test is 1 minus the probability of a Type II error.** To calculate P(Type II error), you need a **hypothesized scenario under the alternative hypothesis** — the Type II error probability depends entirely on which specific alternative you plug in (it's not a single number like α is).

**Designing statistical tests (power calculations):**
- Often you choose a sample size such that, under alternatives you think are reasonable, you have a specific chance of being able to reject the null.
- This is called doing a **power calculation** — an essential input into designing pilots or experiments, done *before* collecting data.
- **Convention:** set α = 0.05 and target power = 80%, then solve for the required n.

## 14. Power calculations in practice — the sample-size spreadsheet

`Block 2 - Power Calculations - Sample Size Determination.xlsx` operationalizes §13 using the **exact same Nordex inputs** (μ₀=29.7, μ₁=29.5 — the hypothesized "worth detecting" alternative, σ=0.7, α=0.05 one-sided, target power=80%). Three tabs:

### Tab 1 — "Sample size": deriving the required n
**Step-by-step (all values as calculated in the workbook):**
```
1. Shift to detect: δ = μ0 − μ1 = 29.7 − 29.5 = 0.20
2. z for significance level: zα = NORMSINV(1−0.05) = 1.6449
3. z for power: zβ = NORMSINV(0.80) = 0.8416
4. Total distance needed, in SEs: zα + zβ = 2.4865
5. Noise relative to signal: σ/|δ| = 0.7/0.2 = 3.50
6. Required n (unrounded): [(zα+zβ) × σ/δ]² = (2.4865 × 3.50)² = 8.7027² ≈ 75.74
7. Required n, rounded up (normal/z approximation): n = 76
8. Required n for a t-test (small correction, + zα²/2 for estimating σ from the sample): 
   76 + 1.6449²/2 = 76 + 1.35 = 77.35 → round up to n = 78
```
**The key insight — the actual Nordex pilot was underpowered:** the pilot in the lecture slides used only **n = 40**, but a properly designed power calculation (α=0.05, 80% target power, δ=0.2, σ=0.7) calls for **n ≈ 76–78**. The workbook's "check power at any n" section confirms this directly: plugging n=40 into the power formula gives **SE=0.1107, rejection cutoff=29.518, and power = NORMSDIST(|δ|/SE − zα) = NORMSDIST(0.1622) ≈ 0.564 — only 56.4% power.** In other words, if the true weight really was 29.5 tons, a 40-blade pilot had barely better than a coin-flip's chance of actually detecting it and triggering the switch — it happened to come out statistically significant (p=0.039, §8) this one time, but the pilot wasn't *designed* to reliably catch an effect of this size.

### Tab 2 — "Power curve": power as sample size grows
Holding μ0, μ1, σ, α fixed and varying only n (selected rows):

| n | SE | Rejection cutoff (X̄) | Power |
|---|---|---|---|
| 10 | 0.2214 | 29.336 | 22.9% |
| 40 (actual pilot) | 0.1107 | 29.518 | 56.4% |
| 75 | 0.0808 | 29.567 | 79.7% |
| 80 | 0.0783 | 29.571 | **81.9%** (crosses 80% target) |
| 100 | 0.0700 | 29.585 | 88.7% |
| 150 | 0.0572 | 29.606 | 96.8% |

Power rises steeply at first and flattens out — classic diminishing returns, same √n-in-the-denominator logic as Chapter 15's margin-of-error shrinkage.

### Tab 3 — "Sensitivity": required n as σ and δ vary
Required n scales with **σ²** and with **1/δ²** (the base case is shaded: σ=0.7, δ=0.2 → n=76, matching Tab 1 exactly):

| σ \ δ | 0.10 | 0.15 | 0.20 | 0.25 | 0.30 |
|---|---|---|---|---|---|
| 0.5 | 155 | 69 | 39 | 25 | 18 |
| 0.6 | 223 | 99 | 56 | 36 | 25 |
| **0.7** | 303 | 135 | **76** | 49 | 34 |
| 0.8 | 396 | 176 | 99 | 64 | 44 |
| 0.9 | 501 | 223 | 126 | 81 | 56 |
| 1.0 | 619 | 275 | 155 | 99 | 69 |

Halving the shift you need to detect (δ) roughly quadruples the required sample size (e.g. at σ=0.7: δ=0.2→n=76, δ=0.1→n=303, almost exactly 4×) — the same inverse-square relationship Chapter 15 found between margin of error and n.

## 15. Other properties of tests

**Significance versus importance:**
- Statistical significance does **not** mean you've made an important or meaningful discovery.
- The size of the sample affects the p-value of a test — **with enough data, a trivial difference from H₀ leads to a statistically significant outcome.** (The flip side of §14's lesson: just as too little data can leave a real effect undetected, a huge sample can make a tiny, practically meaningless effect "significant.")

**Confidence interval or test?**
- A **confidence interval** provides a range of parameter values compatible with the observed data.
- A **test** provides a precise analysis of a specific hypothesized value for a parameter.
- (Echoes §4: when a problem is really a two-sided question, reporting the CI often communicates the same information more usefully than a bare reject/fail-to-reject verdict.)

## 16. Pitfalls

- Do not confuse statistical significance with substantive importance.
- Do not think that the p-value is the probability that the null hypothesis is true. (A p-value is a statement about how surprising the *data* would be if H₀ were true — not a probability statement about H₀ itself.)
- Avoid cluttering a test summary with jargon.

## 17. Takeaways (Punchline)

1. **Pick the hypotheses before looking at the data** — don't choose H₀/Hₐ after seeing which framing makes your result look better (same "pre-register before peeking" discipline as Chapter 15's Philip Morris v. EPA confidence-level case).
2. **Choose the null hypothesis on the basis of profitability** — H₀ should encode the status-quo/default action, not an arbitrary convention.
3. **Pick the α level first, taking into account both types of error** — α isn't free; a stricter α (fewer false positives) raises the risk of Type II errors (missed real effects) unless you also increase n.
4. **Think about whether α = 0.05 is appropriate for each test** — it's a convention, not a law.
5. **Report a p-value to summarize the outcome of a test.**

## 18. Reinforcement from Knowledge Check 2 (FreshBox case)

KC2 (`KC2_solutions.pdf`) is nominally a review of Chapters 13/14.1/14.2 and pre-term sampling material (stratified vs. cluster sampling, sampling-frame bias, voluntary-response bias, sampling weights, and a basic sample-size-for-precision calculation) — genuinely new Chapter 16 content is limited, but two questions directly exercise this chapter's Type I/II error framework and are worth keeping as worked reinforcement:

**Q6 (Type I vs. Type II, in a monitoring context):** FreshBox targets a mean delivery time of 30 minutes (known σ=8 min, n=64/day, two-sided control procedure).
- *"FreshBox concludes the process is off target and makes unnecessary adjustments, even though the true mean is 30 minutes"* → **Type I error** (acted/rejected H₀ when H₀ was actually true).
- *"FreshBox concludes the process is on target and makes no adjustments, even though the true mean differs from 30"* → **Type II error** (failed to act/retain H₀ when Hₐ was actually true).

**Q7 (effect of sample size, n: 64→100, α fixed at 5%):**
- Increasing n reduces SE(X̄) = σ/√n → **True**.
- Larger n (fixed α) → narrower control limits (limits = target ± fixed multiple × SE, and SE shrinks) → **True**.
- Larger n does **not** change the Type I error rate — it stays fixed at 5% by construction → **False** (the statement "increasing n increases Type I error" is false).
- Larger n makes it easier to detect a genuine deviation from target — this is **power**, and it rises with n → **True**. This is the exact same mechanism as Tab 2 of the power-calculation spreadsheet (§14): more data concentrates the sampling distribution, shrinking SE, which raises power for any fixed true deviation.

**Q8 (reading a live signal):** control limits [28.5, 31.5] minutes; today's sample mean = 32.2 minutes (outside the upper limit) → correct conclusion is **"there is evidence the process may be off target"** (not "definitely off target," not "a Type I error must have occurred" — you don't know that yet). If FreshBox investigates and finds the true mean actually *was* 30 minutes, the original signal was a **Type I error** (flagged a deviation, but the null was in fact true) — a clean, concrete illustration that a correctly-run test can still be wrong on any single application; that's exactly what the α-level is pricing in.

The remaining KC2 questions (stratified vs. cluster sampling trade-offs, sampling-frame vs. voluntary-response bias, population-share-weighted averages, and the n=400 precision-driven sample-size calculation — `n = (σ/target SE)² = (40/2)² = 400`) are Chapter 13/14 review; the last one is structurally the same calculation as Chapter 15's margin-of-error sample-size formula (`n = 4σ²/MoE²`, since MoE = 2×SE), just expressed directly in terms of a target SE instead of a target margin of error.

---

## Gulsher questions (along with clarification)

*(none yet — add here when you have follow-up questions on this chapter)*
