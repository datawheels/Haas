# Chapter 14: Sampling Variation and Quality — Theory Notes

Source: Chapter-14.pdf (lecture slides, Prof. Reed Walker, XMBA 200S) — 65 slides, roughly double the length of Chapter 13. Many slides are image/chart/table-only (no extractable text); those are described in full below since a plain-text read of the PDF misses them entirely.

---

## Part 1: Recap + Forms of Selection Bias (slides 1–19)

### Recap from Chapter 13
The best way to eliminate bias is random selection — if selected at random, any characteristic of the population (including things you can't observe) is uncorrelated with being included in the sample. SRS ensures the sample mimics the population *on average*.

### The used-car example (slides 3–6) — "how do we assess likelihood of bias?"
A Kaggle used-car sales dataset stands in for "the population." Three samples (A, B, C) are compared against it to see if they *look* random:

| | Population | Sample A | Sample B | Sample C |
|---|---|---|---|---|
| N | 8,128 | 3,942 | 1,050 | 1,107 |
| Selling price mean | 638.27 | 1036.67 | 1870.83 | 653.98 |
| Selling price SD | 806.25 | 1009.50 | 1640.53 | 820.31 |
| km_driven mean | 69,820 | 57,805 | 40,276 | 68,073 |
| year mean | 2013.8 | 2016.2 | 2016.4 | 2013.8 |

**How to read this (the point of the exercise):** Sample C's means (price 653.98, km 68,073, year 2013.8) are nearly identical to the population — it looks like a genuine random sample. Samples A and B both have much higher mean selling price and much more recent mean model year than the population — both look like they oversample newer, pricier cars (e.g., pulled from a "recent listings" or "premium" filter), which is a giveaway of a biased sampling frame, not natural sampling variability. **The general technique:** compare a sample's summary statistics on variables you expect to be neutral (like year or mileage) against the known population — if they're systematically off in the same direction, suspect a sampling-frame issue, not chance.

### Four forms of selection bias (slide 7)
1. **Sampling Frame Bias**
2. **Self-Selection Bias / Voluntary Response Bias**
3. **Survivorship Bias**
4. **Measurement Bias**

#### 1. Sampling Frame Bias (slide 8)
Example: Population of interest = 20–35 year-old men. Survey frame = 20–35 year-old **Twitter users** who share age/gender in their profile. The diagram shows nested circles narrowing from "Target Population" → "Internet Population" → "Population w/ Social Media" → "Twitter Population" → "Observed Sample" → "Observed Sample w/ Non-missing target variable." **Each narrowing step is a place representativeness can be lost** — your final sample is drawn from the innermost circle, which may look nothing like the outermost (true) population of interest.

#### 2. Self-Selection Bias (slide 9)
= Voluntary Response Sample: a sample of only people who chose to participate. Big challenge: not representative (example given: non-random non-response of likely voters). Illustrated with generic "Take Our Survey" pop-up ad images — the point being that *who bothers to click* is never a random cross-section.

#### 3. Survivorship Bias (slides 10–12) — the WWII bomber example
The classic illustration: a diagram of a WWII bomber covered in red dots showing where **returning** planes took bullet damage — dots cluster on the wings, tail, and body, with a conspicuous *gap* around the engines and cockpit. The (Abraham Wald) insight: **the military wanted to reinforce where the dots were, but that's backwards** — those planes *survived* being hit there. The real lesson is "how about more protection **here**" (where there are no dots) — planes hit in the engine/cockpit never made it back to be counted at all. **Basing analysis only on the subset of your original sample that "clears a hurdle" or remains in the sample produces bias.**

Business version given: comparing firms that adopt a risky management practice vs. not — you can only observe firms that *stayed in business*. The slide shows two scatterplots:
- **Reality** (all companies, including those that failed): risky practice vs. company performance has a **downward** trend line — risky practice is bad on average.
- **Observed** (only surviving companies): the same data, but firms that got unlucky and failed are simply missing from the dataset — the trend line among survivors looks **upward**.
- **Wrong conclusion you'd draw:** "risky management practice produces big gains!" — when in reality it produces a wide spread of outcomes that's bad on average, and you're only seeing the lucky right tail.
- Imperfect fix: "Selection Correction" (Heckman correction).

#### 4. Measurement Bias (slide 13)
Bias from *how* something is measured, not who's in the sample:
- **Experimenter demand effect:** people answer a survey in a way meant to please the surveyor (e.g., overstating "are you likely to vote?").
- **Strategic responses:** firms may misreport on official government surveys (BLS, Fed, Census) — lying to avoid an audit, or to inflate/deflate reported figures for regulatory reasons.

### Take-aways on selection (slide 14)
The key question, restated from Chapter 13: **who is left in vs. left out?** If the two groups are systematically different, you're in trouble; if they're effectively the same, you're fine. Random samples, drawn on the *correct* frame, guarantee this.

### Five mitigations for selection bias (slides 15–19)
1. **Professional consumer panels** (e.g., Nielsen — tracks >250,000 households across 25 countries via a maintained, managed panel rather than ad-hoc voluntary response).
2. **Recruitment techniques** — references the NYT/Ipsos Wisconsin mail-incentive experiment (also covered in Class 1's case studies): paying $25 for a mail survey raised response rate to ~24% vs. ~2% for a standard phone poll, though results ended up similar on most measures.
3. **Combining polls to average out bias** (polling averages) — references Nate Cohn's "Polling Averages Can Be Useful, but What's Underneath Has Changed" (Class 1 reading). Explicitly flagged: **"not straightforward and not a panacea"** — averaging inputs that share the same bias doesn't cancel it out.
4. **Bias correction / reweighting data** — if you know the *direction* representativeness fails, oversampled groups get downweighted and undersampled groups get upweighted. "Most common technique but not perfect." (Fully worked example in the companion "Case Studies" notes — SurveyWeightingExample.pdf.)
5. **Worst-case bounds** — if you know the response rate, you can bound the true value between two extreme cases (everyone missing supports X vs. everyone missing opposes X) without assuming anything about who's missing. Formal statement: `true support = (share who respond)×(support among respondents) + (share who don't)×(support among nonrespondents)`; since the second term's true value is unknown, plug in 0% and 100% to bracket it. (Fully worked example in "Case Studies" notes — WorstCaseBounds.pdf.)

---

## Part 2: The Sampling Distribution of the Mean & Control Limits (slides 20–65)

### The setup (slides 20–22)
Managers must decide when limited information is "compelling" enough to act (buy a stock? promote a worker? stop a production line?). **Control limits** are thresholds you set in advance that determine when to act — set by balancing the risk of two types of errors.

### Running example: GPS chip HALT testing (slides 25–26, 31–32, 42–48)
A GPS chip manufacturer runs Highly Accelerated Life Testing (HALT): each chip is scored 0–16 (number of tests passed out of 16). When the process is functioning properly, chips pass on average **μ = 7** tests with **σ = 4**.

**Distribution of 1,000 individually destroyed chips (slide 31):** a lumpy, multi-peaked, clearly non-normal histogram of individual HALT scores (peaks near 3, 9–10, and 12–13) — this is the *population* distribution, established once by destructively testing 1,000 chips to learn μ and σ.

**Distribution of 50 sample means (slide 32):** 50 different samples of n=20 chips (one sample per day for 50 days), each reduced to its sample mean. Despite the wildly non-normal *individual* distribution above, the histogram of the 50 **sample means** is tightly clustered and roughly bell-shaped, centered near 7. **This is the Central Limit Theorem made visible: averaging normalizes, no matter how weird the underlying data looks.**

### Central Limit Theorem & when you can assume normality (slides 33–36)
- **Benefit of averaging:** the sampling distribution of the mean is approximately normal *regardless of the underlying data's distribution* (CLT). This means you can convert "any weird looking dataset" into a known, well-understood problem just by looking at its mean.
- Sample means are normally distributed if **either**: (a) the individual values are already normally distributed, **or** (b) the sample-size condition is met.
- **Sample size condition (heuristic from the textbook):** n > 10 × |K₄|, where K₄ is **kurtosis** (a measure of how prevalent outliers/heavy tails are in the underlying data; K₄ = 0 for normal data). The bigger the kurtosis (fatter tails, more outliers), the larger a sample you need before CLT reliably kicks in.
- **The kurtosis chart (slide 36):** overlays several distributions with different kurtosis values (labeled D=3 down to U=−1.2) — high-kurtosis curves (like D) are sharply peaked with heavy tails; low-kurtosis curves (like U, a near-uniform/rectangular shape) are flatter with thin tails. Visual point: distributions can look very different from normal and from each other, yet their *sample means* will still converge to normal given enough n.

### Standard Error of the Mean (slides 37–41)
- **Definition:** SE = σ/√n — measures sample-to-sample variability in the sample mean ("how noisy is our statistic").
- **Proportional to σ:** more variable population → more variable sample mean.
- **Inversely proportional to √n:** larger samples → less variable sample mean.
- **Does NOT depend on population size** — this directly answers the recurring exam-style question "does JD Power need a bigger sample in 2024 than in 2009 just because there are more cars on the road?" **No** — SE depends only on σ and n, not on N (population size). This is why a 1,000-person poll can be just as precise for a country of 10 million as for a city of 100,000.
- **Notation example given:** X̄ ~ N(μ=7, σ²/n = 16/20 = 0.8) for the HALT example (n=20 chips/day, σ²=16). Translating: the sample mean HALT score is normally distributed, centered at 7, with variance 0.8 (i.e., SD ≈ 0.89).
- **The point of all of this:** any kind of data — HALT scores, sales figures, coin flips, survey responses — becomes the *same* solvable problem once you look at its mean and check the CLT condition: convert to a Z-score and use the standard normal (Z) table.

### Two types of errors (slides 27–30)
- **Type I Error:** taking action when no action was needed (false alarm).
- **Type II Error:** failing to take action when action *was* needed (missed problem).
- Both have real costs; slides reference external articles on costly Type I errors and costly Type II errors (in bCourses "Articles" — not in this folder), plus other real-world Type I/II tradeoffs: **credit card fraud** detection (block a legitimate purchase vs. miss a fraudulent one) and **car rental/technology** screening.

### Control Limits (slides 43–53)
- **Definition:** a symmetric interval μ − L ≤ X̄ ≤ μ + L. Upper Control Limit (UCL) = μ+L; Lower Control Limit (LCL) = μ−L.
- **Decision rule:** if the sample average falls *outside* the limits → stop/investigate. If it falls *inside* → keep running.
- **Worked example (slides 45–49):** Suppose L=1, so production is halted if mean HALT score < 6 or > 8. Even when everything is working fine, there's still a chance the sample mean randomly lands in the shaded "stop" zones (illustrated with a bell curve with red-shaded tails beyond 6 and 8) — that's a **Type I error / false positive**: everything was fine, but you stopped anyway because of sampling noise. Using Z-scores converts this into a standard-normal lookup:
  > P(X̄ < 6 or X̄ > 8) = NORMDIST(6, 7, 0.89, TRUE) + [1 − NORMDIST(8, 7, 0.89, TRUE)] = **0.27**
  (i.e., a 27% chance of a false alarm with these narrow limits — clearly too aggressive in practice, which sets up the next section on choosing L properly.)
- **Balancing Type I and Type II errors (slide 50):** wide control limits reduce Type I error risk (fewer false alarms) but increase Type II error risk (more likely to miss a real problem); narrow limits do the reverse. **You cannot minimize both simultaneously** — it's always a trade-off. Convention: set Type I error probability (α) at 5% or 1%.
- **Standard z-cutoffs table (slide 51):**

  | α (Type I error prob.) | z-score cutoff (z_{α/2}) |
  |---|---|
  | 0.05 | 1.96 |
  | 0.01 | 2.58 |
  | 0.0027 | 3.00 |

  General formula for control limits: **μ ± z_{α/2} × (σ/√n)**
- **Repeated testing (slide 52):** if you test repeatedly (e.g., every week), companies often use much wider limits (α = 0.0027, i.e., 3σ) because Type I error probability *compounds* across repeated tests: a 5% single-test error rate becomes a **40% chance of at least one false alarm over 10 consecutive tests** (1 − 0.95¹⁰ ≈ 0.40). Since repeated testing gives multiple chances to catch a real problem, companies are willing to accept a higher Type II error risk on any single test.

### Take-aways (slide 53) and Punchline (slide 54)
- Think hard about *which* process attribute to monitor.
- Don't focus on one error type while ignoring the other.
- Don't assume the process has failed just because one value falls outside the limits (it might be the ~α% chance false alarm).
- Don't confuse Type I and Type II errors.
- **Punchline:** decision-making under incomplete information will always produce some mistakes, even in the best process. But because we know sample means are (approximately) normally distributed, we can precisely quantify how likely different outcomes are — letting us set action thresholds with a known, chosen risk of Type I error.

### Bonus example #1: rural counties and kidney cancer (slides 55–57)
Classic Gelman/Nolan illustration: two US maps showing (1) counties with the **lowest** 10% age-standardized kidney-cancer death rates, and (2) counties with the **highest** 10% — and **both maps highlight largely the same set of sparsely-populated, rural counties.** The reveal (scatterplot, slide 57): a plot of age-adjusted cancer rate vs. county population (log scale) fans out dramatically at low population and narrows/converges at high population. **This is pure sampling variability, not a real effect of rural life on kidney cancer** — small-population counties have far fewer cases, so their rate estimates (a "sample mean" of sorts) are much noisier and more likely to land at either extreme (very low *or* very high), while large counties' rates are stable and cluster near the true average. **Moral: don't mistake noise from small samples for a real signal** — the exact same statistical principle as SE = σ/√n (small n ⇒ big variance) applied to a real public-health map that fools people constantly.

### Bonus example #2: "Jimmy Quickfingers" the blackjack dealer (slides 58–65)
**The setup:** Jimmy is a blackjack dealer at Caesars Palace. His table has lost an average of **$12,000/night over the last month**. Is he stealing? Should he be fired?

**Given information:** honest dealers' tables earn a nightly profit with mean **$60,000** and SD **$100,000** (a wide, roughly normal-looking distribution shown in slide 59 spanning roughly −$400,000 to +$400,000). Jimmy works 20 days/month.

**Step 1 — get the distribution of the *monthly average* daily profit (slides 60–61):**
> SE = σ/√n = $100,000/√20 ≈ **$22,360**

So average daily profit over a month is approximately Normal(mean = $60,000, SE = $22,360).

**Step 2 — probability an honest dealer loses $12,000/day or worse over a month (slide 62):**
> P(X̄ ≤ −$12,000) = P(Z ≤ (−12,000 − 60,000)/22,360) = P(Z ≤ **−3.21**) ≈ **0.0007** (less than 1 in 1,000)

This is *extremely* unlikely if Jimmy is honest — strong evidence something is wrong (statistically, but the slide explicitly asks: "So do you fire Jimmy? Are you sure you're right?" — a reminder that even a 1-in-1,000 event **will** happen to someone, and firing is itself a costly, hard-to-reverse action with its own Type I error risk).

**Step 3 — reframe as a control-limit problem (slides 63–65):** Suppose the casino's actual firing rule is: fire any dealer whose monthly average daily profit is below $0 or above $120,000 (note: symmetric around the $60,000 mean, ± $60,000, i.e., roughly ±2.68 SE). What's the Type I error probability under this rule (i.e., the chance an *honest* dealer gets flagged)?
> P(X̄ < $0 or X̄ > $120,000) = 1 − P(−2.68 ≤ Z ≤ 2.68) ≈ **0.008** (a little under 1%)

**Business point of this whole example:** it's a direct, memorable application of everything above — control limits, Type I/II error, and the SE formula — to a high-stakes personnel decision, showing how to turn "does this look suspicious?" into a precise, defensible probability instead of a gut call.

---

## Gulsher questions (along with clarification)

*(none yet — add here when you have follow-up questions on Chapter 14, same as the Chapter 13 notes file)*
