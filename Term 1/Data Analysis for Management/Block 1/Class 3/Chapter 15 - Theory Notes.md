# Chapter 15: Confidence Intervals — Theory Notes

Source: Chapter-15.pdf (lecture slides, Prof. Reed Walker, XMBA 200S) — 35 slides. Several slides are image/table-only or contain intentionally **blank formulas** meant to be filled in live during class; those are worked out in full below.

---

## 1. Where this fits in the course
Chapter 13–14 established: sample means/proportions have a *sampling distribution* (centered at the population parameter, with standard error = σ/√n), and we can calculate how unusual a given sample result is (z-scores, control limits). **Chapter 15 flips the direction of that logic**: instead of "given the population, how surprising is this sample?", it asks **"given only this one sample, where is the population parameter likely to be?"** That's a confidence interval — the bridge from Chapter 14's monitoring/control-limit framework to Chapter 16's hypothesis testing (deciding things with *no* prior information about the population).

## 2. Running example: UC Berkeley Alumni Credit Card
A credit card company pilots a UC Berkeley alumni card: preapproved applications sent to a **random sample of 1,000 alumni**. Two unknown population parameters of interest:
- **p** = proportion who will return/accept the application
- **μ** = average monthly balance carried by those who accept

**Summary statistics from the pilot (slide 7):**

| Quantity | Value |
|---|---|
| Number of offers | 1,000 |
| Number accepted | 140 |
| Proportion accepted, p̂ | 0.14 |
| Average balance, x̄ (n=140 accepters) | $1,990.50 |
| SD of balance, s (n=140) | $2,833.33 |
| Kurtosis K₄ (balance) | 2.975 |

**Note the sample-size switch:** p̂ is calculated over all **1,000** offers (accepted vs. not), but x̄ and s for the *balance* are calculated only over the **140 people who actually accepted** — you can't know a balance for someone who never got the card. This distinction matters for every downstream calculation.

## 3. Confidence interval — core definition
A confidence interval is **a range of plausible values for a population parameter, based on one sample**, built from the sampling distribution of the relevant statistic. To construct one you need:
1. How confident you want to be (choose α, e.g. α=0.05 for 95% confidence)
2. The sample statistic itself (x̄ or p̂)
3. The standard error (SE)

**General formula:** `x̄ ± t_(α/2, df) × SE`, where `SE = s/√n` (using the *sample* SD, s, in place of the usually-unobserved population SD, σ — this substitution is why we use the **t-distribution** instead of the normal/z-distribution).

## 4. The t-distribution (slides 12–14)
- Looks like a normal distribution but with **wider/fatter tails** — it accounts for the extra uncertainty introduced by estimating σ with s instead of knowing it.
- Degrees of freedom, **df = n − 1**, controls its exact shape.
- As n grows, the t-distribution converges to the standard normal (slide 13's chart shows this directly: at df=3 the red dashed t-curve is visibly flatter/wider-tailed than the black standard normal, but at df=9 the two curves are nearly indistinguishable).
- **Finding the t-statistic:** for a 95% CI (α=0.05) with n=35 (df=34), you want the t-value that puts 0.025 in each tail: `t_(0.025, 34)`. Excel: `T.INV(0.025, 34) = 2.032`. Stata: `display invttail(34, 0.025)` → same result.

## 5. Confidence interval for a proportion — worked example

**Standard error formula:** SE = √[p̂(1−p̂)/n] — this follows from the general SE = σ/√n rule, using the fact that a proportion's population variance is p(1−p) (see Chapter 11).

**Worked calculation (filled in from the blank slide, verified against the "How Does AI Do Here?" slide):**
```
p̂ = 0.14, n = 1,000
SE = √(0.14 × 0.86 / 1000) = √0.0001204 ≈ 0.01097

95% CI = 0.14 ± 1.96 × 0.01097 = 0.14 ± 0.0215
        = [0.1185, 0.1615] ≈ [11.9%, 16.2%]
```
Rounded, the slides report this as **"between about 12% and 16%."** Sample-size check for using the normal/CLT approximation: nₚ̂ = 140 and n(1−p̂) = 860, both well above the usual rule-of-thumb minimum of 10 — condition satisfied.

**"Can we do better?"** A larger sample size shrinks the SE (it's in the denominator as √n), which narrows the interval — a more precise estimate of p, at the cost of a bigger/more expensive sample.

## 6. Confidence interval for a mean — worked example

Same procedure as for p, but SE = s/√n directly (no p(1−p) substitution needed since balance is a continuous variable, not a proportion).

**Worked calculation (filled in from the blank slide):**
```
s = $2,833.33, n = 140  (accepters only — see the sample-size note above)
SE = 2,833.33 / √140 = 2,833.33 / 11.832 ≈ $239.46

df = 139, t*(0.025, 139) ≈ 1.977   (essentially = z=1.96 at this large n)

95% CI = 1,990.50 ± 1.977 × 239.46 = 1,990.50 ± 473.42
        = [$1,517, $2,464]
```
The slides round this to **"between $1,516 and $2,465"** — matches. Using z=1.96 instead of t gives [$1,521, $2,460], essentially identical at this sample size (n=140 is large enough that t ≈ z).

**Discussion prompt on the slide:** "Might μ be $1,250?" — **Answer:** it's *possible* (a CI doesn't say impossible values outside it can't occur), but *unlikely* given the sample evidence — $1,250 sits well below the lower bound of the 95% CI.

## 7. Interpreting confidence intervals correctly (slide 20) — memorize the WRONG answers to avoid them

The slide explicitly lists three **incorrect** interpretations of the $1,516–$2,465 interval:
1. ❌ "95% of all customers keep a balance of $1,520 to $2,460" — wrong: the interval is about the **mean**, not about individual customers' balances (individual balances vary far more widely, as shown by s = $2,833).
2. ❌ "The mean balance of 95% of samples of 140 accounts will fall between $1,520 and $2,460" — wrong: this describes a *different, hypothetical* interval computed from *many* future samples, not the confidence level's actual meaning.
3. ❌ "The mean balance is between $1,520 and $2,460" — wrong: this states it as a certain fact, but a CI is a statement about **confidence in the *procedure***, not a probability statement about where the fixed, unknown μ definitely lies.

**Correct interpretation (implied, standard stats framing):** "If we repeated this sampling procedure many times, 95% of the resulting confidence intervals would contain the true population mean." Any single interval either does or doesn't contain μ — you just don't know which, but the *method* is reliable 95% of the time.

## 8. "How Does AI Do Here?" (slide 21)
The deck includes a live screenshot of an AI tool being asked to "calculate the confidence interval for the proportion and then for the mean" given the summary-statistics table. The AI's answer matches the manual calculations above almost exactly:
- Proportion CI: (11.85%, 16.15%) — flags the condition check (np̂=140, n(1−p̂)=860, both >10) automatically.
- Mean CI: **correctly catches that n=140 (not 1,000) applies here**, since balance data only exists for accepters — this is the single easiest mistake to make in this whole example, and the slide is explicitly testing whether you (or your AI) notice it.
- Reports both the t-based ($1,517–$2,464) and z-based ($1,521–$2,460) versions, noting they're "essentially identical at this sample size."

**Take-away purpose of this slide:** shows that an AI tool can correctly execute the mechanics *if you feed it the right numbers and it catches the n-switch* — but you still need to understand the definitions well enough to check its work (same "trust but verify" theme as Chapter 13's discussion of AI-assisted survey design).

## 9. Margin of Error (slides 23–28)

**Definition:** an informal, back-of-the-envelope 95% CI that rounds the t/z multiplier to **2** instead of 1.96 (close enough for quick use):
- For a **mean**: margin of error = 2 × (s/√n)
- For a **proportion**: margin of error = 2 × √[p̂(1−p̂)/n]

This is the number reported in election polls and surveys — e.g., "46% approve, ±2 percentage points."

**What affects margin of error:**
1. Level of confidence chosen
2. Variation in the underlying data
3. Number of sample observations (n)

### Determining sample size in advance
- **For a study about μ:** n = 4σ²/(Margin of Error)² — since MoE = 2×σ/√n, solving for n gives this. Requires an *estimate* of σ² up front, typically from a pilot sample (since you must choose n before collecting your main data).
  - **Worked example (slide 27):** A nutritionist wants average calorie intake known to within ±50 calories at 95% confidence; a pilot study estimates σ = 430.
    ```
    n = 4σ² / (MoE)² = 4 × 430² / 50² = 4 × 184,900 / 2,500 = 739,600 / 2,500 = 295.84
    → round up to n = 296
    ```
- **For a study about a proportion p:** no pilot sample needed — just use the **worst case** p = 0.5, since p(1−p) is maximized at p=0.5 (giving σ = 0.5, the largest possible value, so you never under-plan sample size no matter the true p). This simplifies the formula to just: **n = 1/(Margin of Error)²**

**Sample sizes for various margins of error at 95% coverage, using p=0.5 (slide 28):**

| n | Margin of Error |
|---|---|
| 100 | 10% |
| 400 | 5% |
| 625 | 4% |
| 1,112 | 3% |
| 2,500 | 2% |
| 10,000 | 1% |

Notice the pattern: **halving the margin of error requires roughly quadrupling n** (100→400 to go from 10%→5%; 2,500→10,000 to go from 2%→1%) — a direct consequence of MoE ∝ 1/√n.

## 10. Caution: Margin of Error with Non-Response (slide 29)
The slide explicitly flags that the standard margin-of-error formula **only accounts for sampling error**, not non-response bias, and points back to **Chapter 14's "Mitigation #5: Worst-Case Bounds"** as the fix. This slide references the Wisconsin governor's race polling failure (see companion "Case Studies" notes) and a real methods paper — Dominitz & Manski (2025), *"Using Total Margin of Error to Account for Non-Sampling Error in Election Polls"* — which formalizes combining the sampling-error margin with a worst-case non-response bound into a single **"Total Margin of Error" (TME)**. A calculator implementing this exact method is in this folder: `Chapter 15 (beyond) - TotalMarginOfError_calculator.xlsx` (see the Case Studies notes for a full walkthrough).

**The core insight to remember:** the standard "±2 points" margin of error you see reported is *only* the sampling-error component — it says nothing about bias from who didn't respond. A poll can report a tiny, precise-looking margin of error while its *true* uncertainty (once non-response is accounted for) is many times wider.

## 11. Extended case: Philip Morris v. U.S. EPA (slides 30–33)

**Background:** In 1993 the EPA released "Respiratory Health Effects of Passive Smoking," concluding secondhand smoke causes lung cancer in nonsmokers and classifying it a "Group A carcinogen" (same category as asbestos, benzene, radon) — triggering increased regulation. A key estimate: secondhand smoke exposure reduces lifespan by **1.6 years** relative to average, based on a study of thousands of nonsmokers living with smokers. The EPA reported a **90% confidence interval of 0.12 to 3.08 years**.

**The lawsuit:** Philip Morris and RJR Nabisco sued the EPA, alleging the findings were "manipulated" to "falsely disparage" cigarettes, seeking to have the report declared "null and void." **The battle centered specifically on the choice of a 90% (not 95%) confidence interval.**

**The tobacco industry's argument:** epidemiological studies conventionally use 95% CIs; choosing 90% instead misrepresented the result's precision. And they had a mathematical point:
- Ratio of t-multipliers: t_{.025} / t_{.05} (large n) = 1.96/1.645 = **1.19** → a 95% CI is about **20% wider** than a 90% CI for the same data.
- Recomputed at 95%: the interval becomes **−0.16 to 3.36 years** — note this range now **includes zero (and even slightly negative values)**, meaning at 95% confidence you could no longer rule out that secondhand smoke has *no effect* on lifespan (or even, implausibly, a positive one). At 90% confidence, the interval (0.12 to 3.08) stayed entirely above zero.

**The EPA's defense:** they didn't want to report a 95% CI because they argued it wasn't scientifically plausible that passive smoke *decreases* cancer risk, and showing an interval that dipped near/below zero would have been confusing given that prior.

**Outcome:** the U.S. District Court ruled **in favor of the tobacco industry** in 1998, finding the EPA had failed to follow proper scientific/epidemiological practice and had "cherry picked" evidence, stating: *"The EPA publicly committed to a conclusion before research had begun … and adjusted established procedure and scientific norms to validate the Agency's public conclusion."*

**Why this belongs in the confidence-interval chapter — the discussion questions the slides pose but don't answer:**
- Choosing your confidence level (90% vs. 95%) is a **researcher decision**, not a fixed scientific standard — and that decision can be made *after* seeing how it affects the reported range, which is precisely the kind of "choosing your analysis after seeing the result" that undermines the credibility of a statistical claim.
- A **narrower interval that conveniently avoids crossing zero** looks more "significant" and harder to challenge — this is a real-world illustration of why the choice of α should be justified *before* seeing data, not selected because it produces a more convincing-looking result.
- Many practicing scientists still sided with the EPA's underlying conclusion (an editorial called the case against secondhand smoke "overwhelming") — this case is less about whether secondhand smoke is harmful (subsequent research broadly confirms it is) and more about **the specific statistical practice of picking your confidence level to get the interval you want.**

## 12. Punchline (slide 34)
You now have precise tools to:
1. Decide when a sample result is unusual enough to act on (Chapter 14's control limits / hypothesis-style thinking).
2. State what a sample tells you about an unknown population parameter (this chapter's confidence intervals).

**What's next (Chapter 16):** statistical testing — making decisions using *only* sample data, with no independent information about the population or the underlying process.

---

## Gulsher questions (along with clarification)

*(none yet — add here when you have follow-up questions on Chapter 15, same format as the Chapter 13/14 notes files)*
