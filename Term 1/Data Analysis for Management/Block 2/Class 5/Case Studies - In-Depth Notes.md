# Class 5 Case Study — In-Depth Notes (Chapter 17: Comparisons & Experimental Design)

Source: `Block 2 - Hawthorne Case.pdf` (Davis, Gertler, Thompson, Rodriguez — Berkeley Haas). Chapter 17 slides have since been posted (`Chapter-17.pdf`) — see the companion `Theory Notes.md` in this folder for the full lecture walkthrough, including the chapter's own worked version of this case (its §10). These notes work through the case in more depth on its own, with an eye toward the two-sample comparison / experimental-design machinery Chapter 17 introduces, and (below) extend to the in-class AI Consulting Experiment team assignment.

---

## 1. The setup

**Julian Collins**, Director of Operations at Fresh Taste Inc. (FTI) — the world's largest meat-based packaged-goods company — is under pressure. FTI's Omaha plant has aging equipment, shrinking margins, and labor costs "considerably higher than industry averages" because of a legacy profit-sharing/guaranteed-wage culture dating to the founder. New, non-unionized, automated competitors (some fresh out of bankruptcy with renegotiated, sometimes 50%-lower, wages) are squeezing FTI. Julian has two levers: (a) go back to the union (FLU) and ask for concessions — politically costly, since FLU is still upset about 2018 wage cuts — or (b) find a way to raise *productivity* instead of cutting pay, which doesn't require a fight with labor at all.

**The evidence on the table:** in 2019, engineers at FTI's Hawthorne plant ran an informal experiment — renting portable generators/lights and sporadically supplementing the "antiquated lighting" in three departments over a winter, to see if better lighting speeds workers up. Julian's investment rule: if better lighting raises productivity by **more than 4 units/day**, the capital cost of a permanent lighting upgrade pays for itself. He's reviewing the results (**Exhibit A**) to decide whether to act.

## 2. Exhibit A, read carefully

| | n | Mean (units/day) | SD | Skewness | Kurtosis |
|---|---|---|---|---|---|
| Normal lighting | 320 | 452.2 | 84.4 | −0.18 | 0.09 |
| Improved lighting | 220 | 472.4 | 85.8 | 0.19 | 0.10 |

- **540 total observations**, one per department-day, over a 180-day window across 3 departments (180×3 = 540 — checks out exactly).
- **Raw effect: +20.2 units/day** under improved lighting (472.4 − 452.2) — comfortably above Julian's 4-unit breakeven threshold *on its face*.
- Skewness near 0 and kurtosis far below 3 (excess kurtosis ≈ 0.09–0.10, i.e., actual kurtosis ≈ 3.09–3.10) in both groups — both distributions look close to normal/mesokurtic, no red flags of extreme outliers that would undermine using means/SDs the way we are about to.
- The SDs are nearly identical (84.4 vs. 85.8) — improved lighting didn't obviously change the *spread* of daily output, only (apparently) its center.

## 3. Is +20.2 units/day statistically real, or just noise? (applying Chapter 17's comparison-of-two-means logic)

This is a two-independent-sample comparison — exactly the kind of question Chapter 17 exists to answer, even though the chapter slides themselves aren't posted yet. Treat "normal" and "improved" as two samples drawn from two (possibly identical) populations of daily output, and test whether their means differ by more than sampling noise would produce.

**Standard error of the difference in means:**
```
SE = √(s₁²/n₁ + s₂²/n₂) = √(84.4²/320 + 85.8²/220)
   = √(7,123.36/320 + 7,361.64/220)
   = √(22.26 + 33.46)
   = √55.72 ≈ 7.46
```

**t-statistic:**
```
t = (472.4 − 452.2) / 7.46 = 20.2 / 7.46 ≈ 2.71
```

With df in the hundreds (Welch's approximation lands close to n₁+n₂−2 = 538 here, since the two SDs are so similar), the 5% two-tailed critical value is ≈1.96 and the 1% value is ≈2.58. **t ≈ 2.71 clears both** — the gap is statistically significant at the 1% level, not just the conventional 5% level.

**95% confidence interval for the true mean difference:**
```
20.2 ± 1.96 × 7.46 = 20.2 ± 14.6 = [5.6, 34.8] units/day
```

**Why this interval matters more than the point estimate for Julian's decision:** his breakeven is 4 units/day. The *lower bound* of the 95% CI (5.6) is already above 4 — so even under a pessimistic-but-statistically-plausible read of this data, the lighting upgrade would pay for itself. If the interval's lower bound had fallen *below* 4 (e.g., if SDs were larger or n smaller), Julian couldn't confidently say the investment clears his bar even though the point estimate looked good — this is the whole reason to report a CI/test a hypothesis instead of just eyeballing a 20-unit gap.

## 4. The catch — this was never a randomized experiment (the real point of the case)

Read the methods paragraph again: *"Sporadically during the winter months plant engineers brought in portable generators... Three separate departments... participated... though workers discovered it was easiest to install the portable lights in department 1 and so they were **most often installed there**."*

Two damning phrases for causal inference:
1. **"Sporadically"** — lighting wasn't turned on/off on a random or even fixed schedule; someone (a foreman? the engineers?) chose which days got lights, for reasons we're not told.
2. **"Most often installed [in department 1] because it was easiest"** — treatment assignment was driven by *installation convenience*, not randomization. Department 1 is dramatically over-represented in the "improved lighting" sample by construction.

This means the 452.2 vs. 472.4 comparison is **not** an apples-to-apples comparison of the same workers/process under two lighting conditions — it's contaminated by at least three confounds a rigorous experimental design (the subject of Chapter 17) would control for:

- **Department composition confound:** if department 1 simply produces faster (different product line, newer machinery aside from lighting, different crew) *regardless* of lighting, then "improved lighting" days are mechanically biased toward department 1's naturally higher output, inflating the estimated lighting effect. Fix: compare *within* each department (lit days vs. unlit days for department 1 alone, department 2 alone, etc.) rather than pooling — i.e., add department fixed effects, or at minimum report the breakdown by department that Exhibit A collapses away.
- **Time/selection confound:** if lights tended to go up on days when other things were also different (e.g., a supervisor visit, a rush order, milder weather affecting worker comfort/attendance), the comparison conflates "lighting" with "whatever else was true on the days lighting happened to be installed."
- **The Hawthorne effect itself** — the case's title is not a coincidence. The real-world "Hawthorne effect" (named for a 1920s–30s Western Electric study, which this fictionalized case is clearly modeled on) refers to the finding that workers who *know they are being watched/experimented on* change their behavior — including working harder — independent of whatever the actual experimental treatment is. If workers noticed the portable generators and lights being wheeled in and *knew* they were part of a productivity study, the +20.2 units/day could be partly or entirely an artifact of being observed, not of the lighting itself. This is the single most famous confound in the social-science methods literature, and it's baked directly into this case's name as the intended "aha."

## 5. Discussion questions — answered

**1. Who is Julian Collins? What is his situation?**
Director of Operations at FTI's largest plant (Omaha), facing declining profitability from aging equipment and above-industry labor costs, in an industry where new non-union, automated competitors and post-bankruptcy incumbents have structurally lower costs. He must choose between confronting a still-resentful union for wage concessions, or finding a productivity lever that avoids that fight — which is why the Hawthorne lighting evidence is so attractive to him: it's a "free win" if real.

**2. What were the Hawthorne Experiments?**
An informal, non-randomized field trial at FTI's Hawthorne plant: portable lighting was rented and installed sporadically across three departments over a 180-day winter window (540 department-day observations total), to see whether supplementing the plant's outdated lighting raised daily output. Department 1 received the lighting disproportionately often, for convenience reasons unrelated to the research question.

**3. Describe the results reported in Exhibit A.**
Mean daily output rose from 452.2 units (normal lighting, n=320) to 472.4 units (improved lighting, n=220), a difference of 20.2 units. SDs were nearly identical (~84–86) across both groups, and both distributions look approximately normal (low skew, near-normal kurtosis). A formal two-sample comparison gives t≈2.71 (significant at 1%) and a 95% CI of roughly [5.6, 34.8] units — statistically, the improved-lighting group really did produce more, and even the conservative end of that range clears Julian's 4-unit breakeven.

**4. Do you recommend any additional data analysis? What?**
Yes — the raw comparison is statistically significant but not necessarily *causally* valid, because assignment to "improved lighting" wasn't random (it was concentrated in department 1 "because it was easiest"). Before Julian bets capital on this result, recommend:
- **Break the analysis out by department** (department fixed effects / within-department before-after comparison), since department 1 is over-represented in the treatment group and may simply differ from departments 2–3 in ways unrelated to lighting.
- **Check for time trends** — was output already rising over the 180-day window (e.g., seasonal effects, learning-by-doing) independent of lighting, which would bias a simple pooled comparison?
- **Investigate whether workers knew they were part of a productivity study** — if so, the classic Hawthorne effect (behavioral change from *being observed*, not from the treatment itself) is a live alternative explanation for the entire 20.2-unit gap, and no amount of statistical significance testing on this data can rule it out, because it's a *design* flaw, not a *sample-size* problem.
- **Ideally, re-run this as a proper randomized experiment**: randomly assign which department/days get portable lighting (independent of installation convenience), which is exactly the kind of design Chapter 17 (Comparisons, Experimental Design and Implementation) is about to formalize — this case is the "here's what goes wrong without it" motivating example for that chapter.

---

---

## 6. Team Assignment 4 — The AI Consulting Experiment (BCG, "jagged frontier" data)

**Source:** `Team Assignment 4 - AI Consulting Experiment.docx` (in-class team assignment) + `bcg_frontier.csv` (758 rows, one per consultant). The docx explains this is a **classroom reconstruction, simulated to match the published results**, of a real 2023 Boston Consulting Group field experiment: 758 BCG consultants randomly assigned to work **with** an AI assistant (`treatment = AI`) or **without** one (`treatment = Control`) on realistic consulting tasks (brainstorming, drafting, analysis, persuasion), plus one planted task designed to sit **outside** the AI's actual capability at the time. This is explicitly Chapter 17 material, not Chapter 16: unlike "yesterday's" pilot-vs-last-year's-benchmark comparison (a one-sample test against a fixed historical number, $166/$170/$166 depending on the exercise), today's design has a **concurrent, randomized control group** — the central idea of this whole chapter. All numbers below were computed directly from `bcg_frontier.csv` (n = 758: 379 AI, 379 Control — a clean 50/50 split).

### 6.1 Did the randomization "work"? (the baseline balance check)

Computed group means/shares and two-sample tests on the four pre-treatment covariates the assignment specifies:

| Covariate | AI mean/share | Control mean/share | Difference | se | t or z | p-value |
|---|---|---|---|---|---|---|
| `tenure_years` | 7.44 | 6.95 | 0.48 | 0.234 | t = 2.07 | **0.038** |
| `skill_baseline` | 60.03 | 59.39 | 0.64 | 0.874 | t = 0.73 | 0.467 |
| `female` (share) | 0.433 | 0.427 | 0.005 | 0.036 | z = 0.15 | 0.883 |
| `office` (4 offices: Boston, London, Mumbai, Munich) | within 2–5 pts of each other across all 4 offices (e.g., Boston 28.5% AI vs. 32.5% Control; London 31.1% vs. 26.4%) | | | | | — |

Exactly **one** statistically significant difference at α = 0.05: `tenure_years`, about half a year higher in the AI group (p ≈ 0.038) — this matches the assignment's own stated answer key almost exactly ("about half a year, p ≈ 0.04").

**Is the experiment broken?** No. You ran **four** independent balance checks at α = 0.05. If randomization truly worked (all four null hypotheses of "no difference" are true), the chance of at least one false positive by chance alone is `1 − 0.95⁴ ≈ 18.5%` — not rare at all. This is the *same* mechanism Chapter 17's Theory Notes §7.3 calls out explicitly with 20 outcomes (`1 − 0.95²⁰ = 0.64`): run enough significance tests on things that are truly unrelated to treatment, and some will cross p<0.05 by pure chance. One marginal, half-year tenure gap out of four checks is *exactly* what you'd expect under a working randomization, not evidence it failed — especially since `skill_baseline` (the covariate most directly tied to job performance) and `female` are both comfortably balanced, and the office mix is close across all four locations.

**What could have contaminated yesterday's pilot-vs-benchmark comparison, and why does a control group fix it?** A pilot compared only to last year's $166 benchmark has no way to separate "the pilot program worked" from "anything else changed between last year and now" — e.g., the overall economy, client mix, seasonality, or a general productivity trend unrelated to the pilot. A concurrent, randomized control group fixes this because both groups experience the *same* time period, the *same* macro conditions, and the *same* task pool — by construction (§4 of the Theory Notes), the only systematic difference between the groups is the treatment itself, so whatever else changed this quarter changed equally for both groups and cancels out in the comparison.

### 6.2 Treatment effects on the main consulting tasks

Two-sample t-tests on the three outcomes, computed directly from the CSV (group means match the printed table in the assignment exactly):

| Metric | AI mean | Control mean | Difference | p-value |
|---|---|---|---|---|
| Average task quality (1–8) | 5.62 | 4.01 | **+1.61** | < 0.0001 |
| Tasks completed (of 18) | 13.22 | 11.77 | **+1.45** | < 0.0001 |
| Minutes per task | 66.8 | 87.6 | **−20.8** | < 0.0001 |

All three are significant at any conventional α. In percentage terms: quality is **+40.3%**, tasks completed **+12.3%**, time per task **−23.7%** — strikingly close to the real published BCG study's headline figures (consultants using GPT-4 finished "12.2% more tasks, 25.1% more quickly, 40% higher quality" per the HBR/*One Useful Thing* "Centaurs and Cyborgs on the Jagged Frontier" article cited in this class's `class.md` reading list), confirming this simulated dataset was built to reproduce that real result closely.

**Why "caused" is now a defensible word.** Chapter 16's pilot-vs-benchmark exercise never licensed causal language — a pilot beating a fixed historical number could reflect dozens of confounds (§6.1). Here, AI-vs-Control assignment was **randomized**, so — per Chapter 17's Theory Notes §4 — the only systematic average difference between the two groups is the treatment itself; any surviving gap in outcomes can be attributed to the AI, subject only to normal sampling noise (which the p-values already account for).

**The CIO's memo — "AI causes a 40% quality improvement... roll it out for all consulting work immediately."** The experiment *does* license the first clause: the ~40% average quality gain is a defensible, randomization-backed causal estimate, for the mix of tasks actually tested (brainstorming, drafting, analysis, persuasion). It does **not** license "for all consulting work" or "immediately" — those words generalize beyond what was tested, in two ways: (1) external validity — does a 40% gain at BCG, on these four task types, generalize to other firms, other task types, or tasks that look superficially similar but aren't? (2) as §6.3 shows, the experiment's *own* data already contains a task type where the sign of the effect **flips** — "all consulting work" is contradicted by the very dataset the memo is citing.

### 6.3 Stepping outside the frontier

The planted task — superficially a standard spreadsheet analysis, but requiring the analyst to combine the spreadsheet with details buried in separate interview notes — was designed to sit outside the AI's capability at the time; a confident AI reading of the spreadsheet alone gave the wrong answer. Comparing `outside_correct` between groups:

```
AI:      246/379 correct = 64.9%
Control: 318/379 correct = 83.9%
Difference = −19.0 percentage points, p < 0.0001
```

**One sentence for the managing partner:** *"On the planted task that required synthesizing information the AI could not see in the spreadsheet alone, consultants using AI assistance were right significantly less often than those working without it (65% vs. 84% correct) — the same tool that raised quality by 40% on everyday tasks measurably hurt accuracy on a task outside its competence, and consultants could not tell which kind of task they were on."*

**Reconciling "the AI helps" and "the AI hurts" from the same experiment:** a randomized experiment estimates an **average treatment effect — for the population and task mix actually randomized.** It does not estimate one universal effect of "using AI." The AI's effect was strongly positive, averaged over ordinary brainstorming/drafting/analysis/persuasion tasks, and strongly negative, averaged over the one outside-frontier task — both are real, internally valid causal estimates of the *same* intervention, just conditioned on different task types. Pooling everything into one number (as the CIO's memo implicitly does) would average these two effects together and obscure exactly the heterogeneity that matters most for the rollout decision — directly analogous to how Chapter 17's Credit Indemnity experiment (Theory Notes §9) found that different letter features moved demand differently, and how the ITT/LATE distinction (Theory Notes §12) exists precisely because one pooled average can hide very different effects on different subgroups.

**Recommendation to the firm:** neither "give AI to everyone" nor "block it" — both ignore that consultants could not distinguish in-frontier from out-of-frontier tasks in real time. The data instead supports a **task-type-contingent rollout**: encourage/incentivize AI use for the task categories actually tested and shown to help (brainstorming, drafting, routine analysis, persuasion drafting), while building a verification or "second opinion" step for tasks that resemble the planted outside-frontier case — i.e., anything requiring synthesis of information outside what's visible in a single input (here, interview notes the spreadsheet didn't contain). The open research/management question the memo skips entirely: how do you reliably flag, in real time, which side of the frontier a given task is on, if the consultants themselves couldn't tell?

---

## Cross-cutting themes
1. A statistically significant, comfortably-above-breakeven effect size is **necessary but not sufficient** for a causal business decision. The t-test and CI in Section 3 answer "is 20.2 units real, or could it be sampling noise?" — and the answer is clearly *real*. But Section 4's design critique answers a different, more important question the statistics alone can't touch: "real effect of *what*, exactly?" A convenience-based, non-randomized rollout can produce a rock-solid statistical result that is nonetheless the wrong causal story (department composition, time trends, or the Hawthorne effect itself) — which is precisely why experimental design (randomization) matters as much as, or more than, the hypothesis-testing mechanics once you have the data in hand.
2. **A single average treatment effect can hide a sign flip.** The Hawthorne case warns that a real effect can be mis-attributed to the wrong cause (department composition, not lighting); the AI Consulting Experiment (Section 6) shows the complementary danger even inside a *perfectly randomized* design — the same intervention can have a strongly positive effect on one task type and a strongly negative effect on another, and a single pooled "AI improves quality by 40%" headline, however statistically solid, licenses a much narrower rollout decision than a memo-writer might assume.

## Gulsher questions (along with clarification)

*(none yet — add here when you have follow-up questions on this case)*
