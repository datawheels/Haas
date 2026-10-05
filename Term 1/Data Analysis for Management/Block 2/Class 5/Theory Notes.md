# Chapter 17: Comparisons, Experimental Design and Implementation — Theory Notes

Source: `Chapter-17.pdf` (lecture slides, Prof. Reed Walker, XMBA 200S) — 55 slides (image-rendered; read in batches). Covers Stine & Foster Ch. 17.1–17.2. Several worked-example slides contain intentionally **blank formulas/results** meant to be filled in live during class; those are completed below using the surrounding slide data. The Hawthorne case that closes the deck has its own full walkthrough in the companion `Case Studies - In-Depth Notes.md` file in this folder — these notes only summarize it to keep the deck's flow, then point there for the complete analysis.

---

## 1. Where this fits in the course

Chapter 16 (Statistical Tests) gave you the machinery to decide, from **one sample**, whether a parameter differs from some fixed benchmark. Chapter 17 is "Course overview: Part 2" wrapping up into "Part 3: Experiments and causality" — it asks a different question: **given two groups (not a sample vs. a fixed number), is the difference between them real, and if so, can you attribute it to a cause?**

Two distinct problems get bundled together in this chapter, and keeping them separate is the whole point:
1. **Mechanics**: how do you statistically test whether two sample means (or proportions) differ by more than noise would produce? (→ the two-sample t-test)
2. **Design**: even if a difference is statistically rock-solid, is it *causal*? (→ randomization, confounding, internal/external validity)

A result can ace #1 and fail #2 — that's exactly the trap the Hawthorne case at the end of the deck is built to illustrate.

## 2. Basic terminology

- **Experiment** — a procedure that uses *randomization* to produce data that reveal causation.
- **Treatment** — something done to a participant that might have an effect; typically one variable taking different values (e.g., 1 if treated, 0 otherwise).
- **Response** — where you look to see if the treatment had an effect; one or more response variables.

**Data for comparisons typically arise one of three ways:**
1. Compare two sets of observations (no randomization — weakest).
2. Obtain random samples from two populations (random *sampling*, not random *assignment*).
3. Run an experiment that isolates a specific cause (random *assignment* — strongest).

## 3. The ideal experiment

In the ideal experiment, the experimenter:
1. **Selects a random sample from a population** → crucial for **external validity** (can you generalize from your sample to the population?).
2. **Assigns subjects at random to treatments (and control)** → crucial for **internal validity** (have you actually identified the causal effect of this specific treatment?).
3. **Compares the response of subjects between treatments.**

Note the two validities answer different questions and you can have one without the other — e.g., a perfectly randomized lab experiment on an unrepresentative sample has internal validity but weak external validity.

## 4. Why randomization is valued: eliminating confounding

**Confounding**: the *only* difference between treatment and control, on average, should be the treatment itself. Randomization means other factors aren't systematically associated with specific treatments. If there *may* be additional systematic differences, those are **potential confounding factors**. **Selection** into particular treatments is the primary concern with non-experimental, "observational" studies.

**Classic examples of observational associations that may be confounded (slide prompts — "is this causal?"):**
- Red/processed meat and cancer risk (WHO/IARC classified processed meat Group 1, red meat Group 2A "probably carcinogenic," explicitly based on "*limited* evidence" where "other explanations... (chance, bias, or confounding) could not be ruled out").
- People who receive heart transplants have shorter life expectancies than people who don't — are heart transplants bad? (No — sicker people get transplants; **confounded by baseline health**.)
- Kids who enroll in test-prep programs do better on exams — is that all from the test prep? (Motivated families self-select into test prep — **confounded by motivation/resources**.)
- Firms/sports teams that change managers often see improved performance afterward — do new managers typically do a great job? (Teams change managers *because* performance was unusually bad — **regression to the mean**, not necessarily managerial skill.)

**The general diagnostic process after observing a pattern in data:**
1. What causal effect is *suggested*?
2. What *alternative stories* are there for the observed pattern?
3. How might you tell which hypothesis is most plausible? (More data? Additional tests? An experiment?)

**Benefits of Randomized Control Trials (RCTs):**
1. RCTs have no bias (though watch for **attrition** — see §7).
2. Random assignment eliminates lurking variables.
3. RCTs are transparent — simple to explain to non-experts, highly credible.

**Costs of experimentation:**
1. RCTs may be expensive to run.
2. Randomization is not always ethically viable (e.g., Facebook's 2014 revealed news-feed experiment manipulating users' emotions without informed consent).
3. RCTs require replication — without multiple replications you may still have Type I or Type II errors (e.g., publication bias against null results).

## 5. Comparing sample means — the two-sample t-test

With data from a well-designed experiment, you compare sample means between treatment and control — either directly, or against some **break-even level** (e.g., from a profitability calculation). The standard test is the **two-sample t-test**.

**Two-sample t-statistic ("by hand, in case of Apocalypse"):**
```
t = [(x̄₁ − x̄₂) − D₀] / se(x̄₁ − x̄₂)
```
where **D₀** is the break-even/hypothesized difference (specified by the null hypothesis) — this is the key generalization from Chapter 16: you're no longer comparing a single statistic to a population value, you're comparing a **difference between two statistics** to a break-even difference.

**"Gory details" (software will do this for you) — comparing means:**

| | |
|---|---|
| Population parameters | μ₁, μ₂ |
| Null hypothesis | H₀: μ₁ − μ₂ ≤ D₀ |
| Alternative hypothesis | Hₐ: μ₁ − μ₂ > D₀ |
| Sample statistic | x̄₁ − x̄₂ |
| Estimated standard error | se(X̄₁−X̄₂) = √(s₁²/n₁ + s₂²/n₂) |
| Test statistic | t = (X̄₁ − X̄₂ − D₀) / se(X̄₁−X̄₂) |
| Reject H₀ if | p-value < α, or t > t_α |

**Comparing proportions** uses the same logic with z instead of t:

| | |
|---|---|
| Population parameters | p₁, p₂ |
| Null hypothesis | H₀: p₁ − p₂ ≤ D₀ |
| Alternative hypothesis | Hₐ: p₁ − p₂ > D₀ |
| Sample statistic | p̂₁ − p̂₂ |
| Estimated standard error | se(p̂₁−p̂₂) = √[p̂₁(1−p̂₁)/n₁ + p̂₂(1−p̂₂)/n₂] |
| z-statistic | z = (p̂₁ − p̂₂ − D₀) / se(p̂₁−p̂₂) |
| Reject H₀ if | p-value < α, or z > z_α |

**What changes going from one-sample to two-sample tests (slide's explicit list):**
1. The statistic of interest is no longer one statistic from a sample — it's a **difference** between two statistics.
2. The comparison is now against a "break-even difference," not a population mean/proportion.
3. SE's: use SE(difference), not the simple one-sample SE formula.
4. For means, degrees of freedom (needed for t-tables) use the rule of thumb **n₁ + n₂ − 2**. (Software — e.g. Welch's approximation — gives more accurate df/p-values; rely on it when available.)

## 6. Worked example: the Great Minds curriculum experiment

**Setup.** Great Minds is a K–8 curriculum-development company. Curriculum is licensed to a school/district for a fee; adoption depends on whether it measurably boosts student achievement relative to the status quo. Let μ_G = mean test score in the population of schools using the Great Minds curriculum (**treatment**); μ_C = mean test score under conventional teaching (**control**).

**The district's decision rule, stated as hypotheses:** the district only adopts if the new curriculum improves state test scores by **more than 2 points on average**:
```
H₀: μ_G − μ_C ≤ 2        Hₐ: μ_G − μ_C > 2        (D₀ = 2)
```

**Experiment design.** Before implementing district-wide, the NYC Department of Education pilots it: **63 schools randomly selected** from 700+ in the city, then randomly split — **33 → treatment** (Great Minds curriculum), **30 → control** (conventional).

**Descriptive statistics (filled-in from the slide table):**

| | n | Mean | SD | Skewness | Kurtosis |
|---|---|---|---|---|---|
| Great Minds Curriculum | n_G = 33 | x̄_G = 15.42 | s_G = 14.37 | −0.052 | 0.100 |
| Conventional | n_C = 30 | x̄_C = 7.00 (7.01 on the CI slide — rounding) | s_C = 12.36 | 0.342 | −0.565 |

Raw gap: 15.42 − 7.00 = **8.42 points** in favor of Great Minds — comfortably above the 2-point threshold *on its face*. Question the slides pose: is the difference statistically significant, and is it large enough for the district to adopt?

**Step 1 — standard error of the difference (filled in from the blank slide):**
```
se(x̄_G − x̄_C) = √(s_G²/n_G + s_C²/n_C) = √(14.37²/33 + 12.36²/30)
              = √(206.497/33 + 152.770/30) = √(6.257 + 5.092) = √11.349 ≈ 3.369
```

**Step 2 — the t-statistic, testing against the district's actual breakeven (D₀ = 2), filled in from the blank slide:**
```
t = [(x̄_G − x̄_C) − D₀] / se = (8.42 − 2) / 3.369 = 6.42 / 3.369 ≈ 1.906
```
**df = n_G + n_C − 2 = 61.** On the t-table at df = 61, the one-sided critical value at α = 0.05 is t₀.₀₅ ≈ **1.671**. Since **1.906 > 1.671**, the one-tailed p-value is below 0.05 — specifically **p ≈ 0.031**.

**Thus, we reject H₀ at the 5% significance level** — the Great Minds advantage is statistically greater than the district's 2-point breakeven.

**"What Does Claude Say?" (slide 29) — the deck shows an AI tool working this exact problem** given only the summary-statistics table and the one-sided null of D₀=2: it reproduces the same numbers (observed difference 8.42, SE 3.369, Welch df ≈ 61, critical t₀.₀₅ ≈ 1.671, one-tailed p ≈ 0.031) and concludes "reject H₀ — the difference in means exceeds 2." Same "AI gets the mechanics right if you ask it the right, precisely-specified question" theme as Chapter 15's AI confidence-interval example — note the AI had to be told explicitly this was a *one-sided* test against a *non-zero* D₀=2, not the default two-sided test against zero.

**95% confidence intervals for the individual means (slide table):**

| | Great Minds | Conventional |
|---|---|---|
| Mean | 15.42 | 7.01 |
| Std Dev | 14.37 | 12.36 |
| Std Err Mean | 2.50 | 2.26 |
| Upper 95% | 20.52 | 11.62 |
| Lower 95% | 10.33 | 2.39 |
| n | 33 | 30 |

(Check: 15.42 ± t*(0.025, 32)×2.50 = 15.42 ± 2.037×2.50 = 15.42 ± 5.09 ≈ [10.33, 20.52] ✓. Similarly for Conventional with df=29, t*≈2.045: 7.01 ± 2.045×2.26 ≈ [2.39, 11.63] ✓.)

**95% confidence interval for the *difference* μ_G − μ_C (against D₀ = 0, not the 2-point breakeven — a different, more general question):**
```
(x̄_G − x̄_C) ± t_(α/2, 61) × se(x̄_G − x̄_C) = 8.42 ± 2.00 × 3.37 = 8.42 ± 6.74 = [1.68, 15.15]
```
Since this interval **excludes 0**, the means are statistically significantly different in the "plain vanilla" sense too — students in Great Minds schools score between **1.7 and 15.2 points higher**, 95% confidence. (Note this is a *different* question from §6's hypothesis test against D₀=2 — the CI tells you the plausible range for the raw difference; the hypothesis test tells you whether that difference clears the district's specific economic bar. Both point the same direction here, but they need not.)

**What about external validity?** This experiment comes from a subset of NYC schools. Does it generalize to other NYC schools? Elsewhere? The slide leaves this as an open discussion question — a reminder that even a textbook-clean RCT only buys you *internal* validity for free; *external* validity (generalizing beyond the sampled 63 schools) is a separate, harder claim.

## 7. Experimental pitfalls

1. **Non-compliance** — participants don't comply with their assigned treatment. Analysts often report **Intention-to-Treat (ITT)** estimates: the average difference between people *assigned* to treatment vs. assigned to control (not actually-treated vs. actually-control). This affects interpretation but can still deliver a valid causal estimate *of the effect of the offer*, comparing all treatment-assigned to all control-assigned observations. (See §12 below — this is exactly the problem Instrumental Variables solves when you want the effect on those who actually took the treatment.)
2. **Attrition** — participants drop out of the study. Unlike simple non-compliance, this can bias the comparison and make the test no longer causal (e.g., if dropout is correlated with treatment and with the outcome).
3. **Testing too many, or not pre-specified, outcomes** — with a 5% significance level, the Type I error rate across 20 outcomes tested is **1 − 0.95²⁰ = 0.64** — a 64% chance of at least one false positive if you test enough things and only report what's "significant." Pre-specify your hypotheses and primary outcome(s) before collecting data.

## 8. Best practices / experimental playbook

- **Pre-register hypotheses + power calculations** (which test, what sample size, what significance level) — see §11 below for why this matters so much in practice.
- **Balance table at baseline**: check that randomization actually "worked" (treatment and control look similar on observable pre-treatment characteristics).
- **Balance table at endline**: check participants at endline still look balanced, or whether there's sample selection (non-random attrition). If there is, revisit bounds/weighting techniques from earlier chapters.
- **Other design considerations**: if you only have *randomized encouragement*, not actual treatment compliance, estimate "intention to treat" differences, or use **instrumental variable techniques** to estimate "treatment on the treated" (§12). Correct for multiple hypothesis testing when you do have to test many outcomes.

## 9. Worked example: Credit Indemnity — a multi-arm field marketing experiment

Credit Indemnity is a major South African micro-lender: short-term, high-interest, uncollateralized credit; typical loan ≈ $150 (about a third of the borrower's monthly income), ~4-month term. **Business question:** how do interest rates and other letter content affect loan demand? (Motivation: firms spend billions on advertising but rarely get clean causal evidence on what in an ad actually works, because observational studies of advertising are confounded — who sees which ad is rarely random.)

**The experiment:** credit offers mailed to **50,000+ households**; several offer features randomly varied simultaneously (a **factorial design**). Outcome of interest: **applied** = 1 if the household applied for a loan in the month following the offer. Overall mean application rate: **8.50%** (n = 53,194, SD = 0.279).

**Treatment 1 — Interest rate.** Rates randomly varied from **3.25% to 11.75%** per month (mean 7.93%, SD 2.42). Result: the probability of applying **falls about 0.3 percentage points for every 100-basis-point (1pp) increase** in the monthly interest rate offered — a clean, downward-sloping demand curve recovered purely from random price variation (something an observational study of "who got which rate" could never cleanly identify, since lenders don't offer rates at random to begin with).

**Treatment 2 — Including a photo.** 80% of letters included a photo (half female, half male); 20% had none. Including a **female** photo increased applications by **0.5 percentage points** off a ~8% base — equivalent to a **2-percentage-point reduction in the interest rate**. The effect of including a **male** photo was small and statistically insignificant.

**Treatment 3 — Number of worked examples.** Either 1 or 4 hypothetical loan-amount/term/repayment examples were shown (all letters also said "loans available in other amounts"). Including **only a single example** (vs. four) **increased applications by 0.6 percentage points**.

**Treatment 4 — Explicitly reporting the interest rate.** Some letters showed the interest rate explicitly (e.g., "3.99%"); others just showed the loan amount/term/repayment table without the rate. **No evidence** that showing the rate explicitly had any observable impact on applications — i.e., the actual repayment numbers mattered, not whether the rate itself was legible.

**Treatment 5 — Suggested use of funds.** All letters suggested something to spend the cash on: school, debt payoff, home repair, an appliance, or (for ~20% of letters) simply "you can use this cash for anything you want." Result: **the most successful "suggested activity" was no suggested activity at all** — the generic "anything you want" framing outperformed every specific suggestion, none of which had any impact of its own.

**Results summary — ranked by what worked:** (1) lower interest rate, (2) including the photo of a woman, (3) including only one example, (4) no suggested activity. **Implication (the slide's explicit takeaway):** seemingly non-informative advertising content plays a real, measurable role in consumer decisions, and it's hard to predict *ex ante* which specific content features will matter — experimentation (here, a cheap multi-arm factorial mail test) is a low-cost way to discover what actually works, regardless of what you're selling.

## 10. Hawthorne case (summary — full analysis in companion Case Studies notes)

The deck closes with the Hawthorne lighting case (Fresh Taste Inc., Omaha plant): a +20.2 units/day productivity gap between normal lighting (n=320, mean 452.2) and improved lighting (n=220, mean 472.4) that is statistically significant (t≈2.71, 95% CI [5.6, 34.8]) but **not causally clean**, because lighting was installed "sporadically" and "most often" in Department 1 "because it was easiest" — a textbook case of **non-random treatment assignment contaminating an otherwise-solid two-sample comparison**, plus the namesake risk that workers who know they're being observed change behavior regardless of treatment (the real "Hawthorne effect"). The deck's Exhibit B breaks results out **by department**, which is exactly the fix §4/§7 of this file call for. See `Case Studies - In-Depth Notes.md` in this folder for the full worked t-test, CI, and discussion-question answers.

---

## 11. Beyond the chapter: why power calculations are useful

*(Supplementary reading: `Block2 - Chapter 17 (beyond) - Why Power Calculations are Useful.pdf` — a real 2025 preprint, Kohavi, Linowski, Vermeer, Boisseranc, Furuseth, Gelman, Imbens & Rajagopal, "Power Analysis is Essential: High-Powered Tests Suggest Minimal to No Effect of Rounded Shapes on Click-Through Rates.")*

This paper is a direct, concrete illustration of Chapter 17's "RCTs require replication" pitfall (§7.3) and the pre-registration/power-calculation best practice (§8).

**The claim under scrutiny:** Biswas, Abell & Chacko (2023, *Journal of Consumer Research*) reported that simply rounding the corners of square buttons on a web page increased click-through rate by **55%** (n = 919 visits total, p = 0.037).

**Why the authors were skeptical:** having reviewed thousands of real A/B tests at large companies, they note typical UI-change lifts are **under 1%, rarely over 2–3%** — a claimed 55% lift was implausibly large on priors alone.

**The replication:** three new, high-powered A/B tests (SeaWorld Orlando, and two Norwegian retail sites run by Coop) with **over 2.8 million, 2.2 million, and 1.9 million users respectively** — more than 2,000× the original sample. Results:

| Study | n control | n treatment | Conv. control | Conv. treatment | Lift | p-value |
|---|---|---|---|---|---|---|
| BAC (original) | 445 | 474 | 7.19% | 11.18% | **55.49%** | 0.037 |
| SeaWorld Orlando | 1,448,041 | 1,448,066 | 47.13% | 47.21% | 0.16% | 0.20 |
| Obs-BYGG | 1,126,132 | 1,124,100 | 5.43% | 5.45% | 0.29% | 0.60 |
| Obs | 977,499 | 976,653 | 10.07% | 10.14% | 0.73% | 0.09 |

Meta-analysis across all three replications: weighted-average lift of just **0.21%** (p = 0.08) — with over **7.1 million users total**, the authors still could not reject the null of no effect. The true effect, if any, is roughly **two orders of magnitude smaller** than the original claim.

**The core lesson — the "winner's curse":** underpowered studies (power below 50%) that do manage to hit statistical significance *must*, mechanically, exaggerate the true effect to clear the significance bar — a small, noisy study can only "win" (reach p<0.05) by drawing an unusually large sample fluctuation. Significant results from tiny samples are systematically inflated.

**The sample-size formula (industry standard, α=0.05, 80% power):**
```
n ≈ 16σ² / δ²
```
where σ is the within-group standard deviation of the measurement and **δ is the Minimum Detectable Effect (MDE)** you want to be able to reliably find. **Worked example from the paper:** the original BAC study had a control-group click-through rate of 7.19%, so σ = √[p(1−p)] = √[0.0719 × 0.9281] ≈ 0.0673. Requiring an MDE of a 2% *relative* lift (i.e., 0.0719 × 2% ≈ 0.00144 absolute):
```
n ≈ 16 × 0.0673 / (0.0719 × 0.02)² = 1.0768 / (0.001438)² ≈ 1.0768 / 0.00000207 ≈ 520,735 users per variant
```
Even accepting a much larger 10% relative MDE would still require **over 20,000 users per variant** — the original study's 445/474 per arm was never powered to detect anything smaller than a wildly implausible effect, which is precisely why a "significant" 55% result from it was suspect from the start.

**Takeaway for this course:** "statistically significant" and "true and replicable" are not the same thing — an underpowered-but-significant finding is a red flag, not a win, and the fix (as in §8's playbook) is to **pre-register the MDE and compute the required sample size before running the experiment**, not after seeing a tempting p-value.

## 12. Beyond the chapter: instrumental variable methods for imperfect compliance

*(Supplementary reading: `Block2 - Chapter 17 (beyond) - Instrumental Variable Methods.pdf` — Chapter 7, "Instrumental variables: When people don't do what they were assigned to," from Robson Tigre's online book *Everyday Causal Inference*. The PNG `Block2-imbensGelman2.png` in this folder, despite its filename, is actually a screenshot of a tweet by Victor Chernozhukov praising the §11 power-calculations paper above, not IV-specific content.)*

This directly extends §7's "non-compliance" pitfall and §8's playbook line about "randomized encouragement... instrumental variable techniques to estimate treatment on the treated."

**The problem — imperfect compliance.** In Chapter 4/§3 of this file we assumed everyone assigned to treatment actually gets it. In reality, you can randomly offer/invite/encourage, but you can't force use: send discount coupons but not everyone redeems them; offer a free trial but many never activate it. Adoption rates below 5–10% from an invitation are common.

**Two different, legitimate estimates when compliance is imperfect:**
- **Intention-to-Treat (ITT)** = avg(outcome | assigned to treatment) − avg(outcome | assigned to control). Answers: *"What's the impact of offering this program to everyone?"* Preserves the clean logic of randomization (any difference between the two *assignment* groups is causal), but is **diluted** — it mixes together people who actually switched because of the invitation and people who ignored it entirely.
- **Local Average Treatment Effect (LATE)** = the effect specifically for **compliers** — people who take the treatment only if assigned to it (not **always-takers**, who take it regardless; not **never-takers**, who refuse regardless; assuming no **defiers**, who do the opposite of their assignment — the **monotonicity** assumption).

**The Wald estimator — scaling the diluted ITT back up:**
```
LATE = ITT / First stage
```
where **First stage** = avg(treatment uptake | assigned to treatment) − avg(treatment uptake | assigned to control), i.e., how much the instrument (the invitation) actually moved people into treatment.

**Worked numeric example from the chapter (email-frequency experiment, simulated to match a known ground truth of R$15/customer):** 10,000 customers, half randomly invited to switch to daily marketing emails, revenue measured over 60 days.
- **First stage** = 0.36 − 0.055 = **0.31** (36% of invited customers switched; 5.5% of control customers found the daily-email setting on their own) — well above the "weak instrument" danger zone (first-stage F-statistic should exceed 10; it was).
- **ITT ≈ R$4.2 per customer** (statistically significant) — "if we send this invitation to everyone, expect about R$4.2 extra revenue per customer," averaged over compliers and the ~69% who ignored the invitation entirely.
- **LATE = ITT / First stage = 4.2 / 0.31 ≈ R$13.6** — the effect of *actually* switching to daily emails, for the people who switched *because* of the invitation. This lands close to the simulation's true planted effect of R$15, recovered even though two-thirds of invited customers didn't comply.
- **Naive "as-treated" comparison** (comparing those who opted in vs. those who didn't, ignoring the instrument entirely) gives **R$18.7** — overestimates the true effect by about 25%, because switchers are a self-selected, more-engaged group; this is exactly the **selection/confounding** problem §4 warns about, re-appearing even inside a randomized experiment once you condition on a post-treatment choice (who complied).

**Two-stage least squares (2SLS)** is the regression implementation of the same Wald-estimator logic — first stage regresses actual treatment uptake on the random instrument (+ covariates), second stage regresses the outcome on the *predicted* uptake from stage one. Standard software computes both stages and correct standard errors automatically.

**Four assumptions required for IV/LATE to be valid** (a "credibility hierarchy" from easiest to hardest to defend):
1. **Relevance** — the instrument must actually move treatment uptake (testable: first-stage F-statistic > 10).
2. **Independence** — the instrument is uncorrelated with confounders (usually guaranteed by design if the instrument itself was randomized, as here).
3. **Exclusion restriction** — the instrument affects the outcome *only* through the treatment, no direct path (hardest to defend; e.g., if the invitation email itself contained a discount code, that would violate exclusion).
4. **Monotonicity** — no "defiers"; typically a safe assumption in simple encouragement designs.

**Why this belongs in a "beyond the chapter" note on comparisons:** it is the formal fix for exactly the non-compliance pitfall this chapter flags (§7.1) but doesn't resolve — ITT alone tells a manager the expected ROI of *sending* an offer (useful for budgeting/forecasting), while LATE tells them whether the *underlying mechanism* (the treatment itself, for people who actually take it) works at all (useful for product/feature decisions). Mixing the two up — e.g., quoting the LATE's larger number as if it applies to everyone you invite — is flagged in the source chapter as one of the most common real-world mistakes in presenting experiment results to stakeholders.

---

## 13. Punchline / cross-cutting themes

1. **Observational comparisons almost always carry lurking variables; only random assignment eliminates them by design.** Every "is X caused by Y?" example in this chapter (meat and cancer, heart transplants, test prep, new managers, the Hawthorne case) has a plausible confounding story that a clean RCT would have ruled out for free.
2. **Statistical significance and economic/managerial significance are two different bars, and both matter.** The Great Minds example needed *both* "is 8.42 points real?" (t-test) *and* "is it big enough to be worth the $$ to adopt?" (test against D₀=2, not D₀=0) — the same lesson Chapter 15's Hawthorne-style breakeven comparisons taught with confidence intervals.
3. **A clean experimental design buys you internal validity; it says nothing about external validity.** The Great Minds pilot (63 NYC schools) and the Hawthorne case (3 departments, one winter) both raise "does this generalize?" as a separate, unresolved question from "was the internal comparison valid?"
4. **Non-compliance and attrition are not the same failure, and they call for different fixes.** Simple non-compliance still permits a valid ITT estimate (or LATE via instrumental variables, §12); attrition can break the randomization itself and needs the bounds/weighting tools from earlier chapters.
5. **A "statistically significant" result from an underpowered study is a yellow flag, not a green light** — the winner's curse (§11) means small, noisy "wins" are systematically exaggerated, which is why pre-registering a power calculation (not just a hypothesis) is now standard best practice before running any A/B test.
6. **Experimentation is cheap relative to the value of being right about *why* something moved.** The Credit Indemnity mail experiment (§9) found that unpredictable, "non-informative" content choices (a woman's photo, one example instead of four, no suggested use of funds) moved demand as much as the interest rate itself — and none of it could have been discovered by guessing or by an observational study of past mail campaigns, only by randomizing the content itself.

---

## Gulsher questions (along with clarification)

*(none yet — add here when you have follow-up questions on this chapter)*
