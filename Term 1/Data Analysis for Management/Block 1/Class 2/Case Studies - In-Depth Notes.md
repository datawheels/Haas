# Class 2 Case Studies — In-Depth Notes (Chapter 14: Sampling Variation and Quality)

## Suggested study order
1. Chapter-14.pdf (core theory — see companion "Chapter 14 - Theory Notes.md")
2. Z and t Tables.pdf (reference — needed to actually compute the probabilities the chapter teaches)
3. Block1-CancerScreening.pdf + FiveThirtyEight "Science Won't Settle The Mammogram Debate" (base rates, absolute vs. relative risk, lead-time bias, overdiagnosis — a self-contained mini-course in why "the test caught more cancer" doesn't mean "the test saved lives")
4. Block1 - WorstCaseBounds.pdf (deep dive on Mitigation #5 from the slides)
5. Block1 - SurveyWeightingExample.pdf (deep dive on Mitigation #4 from the slides — a fully worked reweighting example)
6. Chapter 14 - PG&E WSJ article (real-world case of trusting/distrusting an internal effectiveness claim before a multi-billion-dollar decision)
7. Team Assignment 1 (One Population, Many Samples) — apply everything above to a simulated airline-fares dataset (see "Team Assignment 1 - Answers.md" for worked solutions)

---

## 1. Block1-CancerScreening.pdf + FiveThirtyEight Mammogram Debate

**Together these two readings are the best worked example in the course of "the data can be right and the conclusion can still be misleading."**

### Six lessons from the cancer-screening note
1. **A positive test usually does not mean cancer (base rates).** Among women in their 40s: ~1% actually have cancer; the test catches 90% of real cases but also falsely flags 9% of healthy women. Out of 1,000 screened: 10 have cancer, 9 test positive; of the 990 healthy women, ~89 also test positive. So **98 people get a scary call, and only 9 (≈1 in 10) actually have cancer.** When the underlying condition is rare, most positives are false positives *no matter how good the test is*. Business analogue: fraud alerts, resume screens, quality inspections — any detector aimed at a rare event.
2. **"Cuts deaths by 20%" and "saves 1 life per 1,000+ screened" are the same fact, stated two ways.** Relative risk (20% reduction) sounds dramatic; absolute risk (1 in 1,000+) tells you what it actually means for one person. Always ask "percent of what?"
3. **Better survival ≠ fewer deaths (lead-time bias).** Screening finds cancer earlier, which starts the "survival clock" sooner — five-year survival can improve even if no one lives a single day longer, because patients just spend more of their remaining time "counted" as survivors. This is why serious evaluations score screening on death *rates*, never survival rates. Business analogue: any metric that changes just because you started measuring earlier (e.g., "time-to-resolution improved" after logging tickets sooner).
4. **Finding more cancer isn't automatically good (overdiagnosis).** Some screen-detected tumors would never have caused harm, but every one found gets treated — and every treated patient sincerely credits screening with saving their life. Individually true testimonials can add up to a misleading aggregate picture.
5. **Guidelines flip-flop because the trade-off is close, not because the science is shaky.** Same underlying trial data, different institutions (USPSTF vs. ACS) weigh "one averted death" against "hundreds of false positives and some overdiagnosis" differently. Same data, different values/loss functions → different recommendations.
6. **What is the population of interest?** The trials behind the mortality estimates are from the 1960s–90s, when cancer treatment was far worse than today. The "population of interest" (a woman screened in 2026, under modern therapy) differs from the trial population along a dimension — treatment era — that **no reweighting can fix**, because it isn't something you can observe/match on. (This directly echoes the Nature vaccine-uptake paper from Class 1: bias on an unobservable dimension is unfixable.)

### The FiveThirtyEight article: concrete numbers behind lesson 2 and 5
- Lifetime risk of dying from breast cancer without screening: **2.7%**. Following USPSTF guidelines (biennial, 50–74): drops to **2.0%**. Following ACS guidelines (annual from 45): drops to **1.8–1.9%**. The gain from the more aggressive ACS protocol over USPSTF is only a few tenths of a percentage point.
- Cost of that marginal gain: USPSTF's program requires 13 mammograms in a lifetime; ACS's requires 20.
- False-alarm rate: **61%** of women who get annual mammograms, and **42%** of women who get them every other year, will be called back at least once for a false positive.
- Per 1,000 women following USPSTF advice (biennial, 50–74): **146 unnecessary biopsies** and **18 overdiagnosed/overtreated cancers** that would never have caused harm.
- **Why guidelines disagree:** ACS gave more weight to observational studies (which show 20–40% mortality reduction) than USPSTF did; randomized controlled trials (the gold standard) show only ~15% reduction, and a 25-year follow-up of two Canadian RCTs (~90,000 women, the only trial run in the era of modern therapy) found **mammography didn't reduce breast cancer deaths at all**. Two expert panels, same evidence, different judgment calls about which studies to trust and how to weigh benefit vs. harm — "a value judgment, not a scientific one."
- **Takeaway line worth remembering:** the article's core thesis is that this debate looks like a scientific disagreement but is actually a disagreement about *values* (how much false-positive harm is worth trading for how much averted-death benefit) — the numbers are agreed on; the trade-off isn't.

### Discussion questions to prep
- If you ran a company deploying a rare-event detector (fraud, defect, churn-risk), how would you decide the acceptable false-positive rate, given lesson 1's base-rate math?
- Can you think of a metric at your own job that might be secretly affected by lead-time bias (lesson 3)?

---

## 2. Block1 - WorstCaseBounds.pdf

Direct elaboration of the deck's "Mitigation #5" slide. See also the equivalent Q&A already written up in Class 1's Chapter 13 notes (bounds vs. imputation) — this document formalizes it with real math.

**The formal setup:** Let r = response rate, ȳ_R = average outcome among respondents, ȳ_N = average among (unobserved) non-respondents, and let outcomes live between y_min and y_max. Then:

> truth = r·ȳ_R + (1−r)·ȳ_N ∈ [ r·ȳ_R + (1−r)·y_min , r·ȳ_R + (1−r)·y_max ]

**The width of this interval is (1−r)(y_max − y_min) — your ignorance is exactly proportional to the non-response rate, no matter how large your sample is.** This is the single most important line in the document: it formally proves that bias (non-response) doesn't shrink with sample size, only variance does — same lesson as the bias-vs-variability bullseye diagram in the theory deck.

**Worked polling example:** Contact 1,250 voters; 1,000 respond (r = 0.8); 60% of respondents support candidate A.
> Support ∈ [0.8×60% + 0.2×0%, 0.8×60% + 0.2×100%] = **[48%, 68%]**

Compare this to the "familiar ±3% margin of error" reported in the news — that margin is only correct **if non-respondents vote exactly like respondents**, an assumption that's probably false. The honest, assumption-free bound is ±10 points around 58%, dramatically wider.

**Crucial point: more data does not help.** Contacting 12.5 million voters at the same 80% response rate still gives you [48%, 68%] — sample size only affects the *respondent* estimate's precision, not the width contributed by non-response. At a realistic modern poll response rate of **2.5%**, the bounds blow up to **[1.5%, 99%]** — meaning virtually all of a modern poll's reported precision comes from the pollster's *modeling assumptions* (weighting, likely-voter models), not from the raw data itself.

**Buying precision with assumptions ("the law of decreasing credibility," per Manski):** if you're not willing to assume non-respondents behave identically to respondents, but you *are* willing to assume their support falls between 40–80%, then:
> support ∈ 0.8×60% + 0.2×[40%, 80%] = **[56%, 64%]**

Stronger assumptions → sharper (narrower) conclusions, but conclusions fewer people will believe. A good analyst states assumptions explicitly rather than hiding them inside a single reported number.

**Business examples given:**
- **NPS/customer satisfaction:** a 20% response rate means a reported "NPS of 62" has enormous worst-case bounds; angry and delighted customers often respond at different rates than neutral ones.
- **Employee engagement:** "85% engaged" from a 60% response rate is consistent with true engagement as low as 51% (0.6 × 85%) — disengaged employees are exactly the ones who skip the survey.
- **Churn/win-loss analysis:** you only interview customers who *agree* to an exit interview — the ones most likely to leave quietly and never respond are missing.
- **Credit & hiring ("reject inference"):** you only observe default rates for *approved* applicants and performance for *hired* candidates — the rejected/not-hired population's true outcomes are structurally unobservable.
- **Clinical trials:** regulators increasingly require these bounds as a sensitivity check on patient dropout.

**Honest caveat in the document itself:** bounds are appealingly assumption-free and transparent, but are "often so large as to be uninformative" — which is itself useful information (it tells you how much your conclusion is really coming from assumptions vs. data).

---

## 3. Block1 - SurveyWeightingExample.pdf

Direct elaboration of "Mitigation #4: Reweighting" — a fully worked numerical example, useful because it shows the *mechanics* Oster's NHANES discussion (Class 1) only described in words.

**Setup:** 100,000 app users emailed an in-app spending survey; 1,364 self-selected respondents (a **1.4% response rate**). Three observable variables are known for both the sample and the population: gender × age group × education. Question of interest: average monthly spend per user.

**The sample doesn't look like the population:** young, college-educated users answered; older users didn't.
- Population age 18–34 share: 30.0% → sample share: 55.7%
- Population age 55+ share: 36.0% → sample share: 13.3%
- Unweighted sample mean spend: **$92.25**

**Why this is a problem, not just noise:** response is voluntary, and the people most likely to respond (young, college-educated, heavy users) also tend to spend the most. **Selection into the sample is correlated with the outcome you're measuring — that's the definition of bias, not sampling variability.**

**The fix — post-stratification weighting (no model, no regression, just arithmetic):**
1. Partition both sample and population into cells by the observables: gender × age × education → 12 cells.
2. For each cell c: **weight = (population share of cell c) ÷ (sample share of cell c)**. Equivalently, weight ∝ 1/Pr(respond | cell c) — if your group responded at one-fifth the average rate, each respondent in that group counts five times over.
3. By construction, the weighted sample's cell shares now match the population exactly. Weighted mean: x̄_w = Σwᵢxᵢ / Σwᵢ.

**Concrete weight table (selected rows):**
| Gender | Age | Education | Pop. share | Sample share | Weight |
|---|---|---|---|---|---|
| Female | 18–34 | College | 5.81% | 14.81% | 0.39 |
| Female | 55+ | No college | 12.85% | 3.67% | **3.51** |
| Male | 55+ | No college | 12.35% | 3.74% | 3.30 |

Reading the extreme row: women 55+ without a college degree are 12.85% of the population but only 3.67% of respondents (12.85 ÷ 3.67 = 3.51) — each such respondent in the data has to statistically "stand in for" 3.5 average respondents to fix the imbalance. Weights average to 1 across the full sample (some cells get upweighted >1, some downweighted <1).

**Result after reweighting:**
- Unweighted sample mean spend: $92.25
- **Weighted sample mean spend: $76.12**
- True population mean (known here because this is a simulated/made-up example): $76.41

Reweighting closed almost the entire gap ($92.25 → $76.12, vs. true $76.41) — a huge correction from three simple observable variables. It works on other outcomes too: share who'd recommend the app fell from 66.1% (unweighted) to 60.6% (weighted).

**The fine print — the same limit Oster's reading flagged:** weighting fixes selection bias **only on the observables you weighted on**. If heavy spenders respond more often than light spenders *within every single cell* (i.e., bias on an unobservable trait, not just demographics), the weighted mean is still biased — reweighting can't fix that, no matter how many cells you use. And critically: **in real life you rarely know the true population mean to check your work against** — this example only "proves" reweighting worked because it's simulated.

---

## 4. PG&E WSJ Article — "PG&E Scraps Tree-Trimming Program Once Seen as Key to Fire Prevention"

**The story:** PG&E spent ~$2.5 billion over several years on "enhanced vegetation management" (12 feet of clearance around power lines, well beyond the 4-foot regulatory minimum) to prevent wildfires after its equipment caused fires that killed 100+ people in 2017–18. PG&E's own internal analysis concluded the program produced only a **13% reduction in ignitions** during peak fire season (7% across a full year) — and the company is **discontinuing the program entirely**, betting instead on new power lines that shut off within 0.1 seconds of contact (which alone produced a **68% reduction in ignitions** where deployed in 2022).

**Why this belongs in a sampling/quality-control chapter — the discussion isn't really about wildfires, it's about trusting a single internal effectiveness estimate before a huge, hard-to-reverse decision:**
- There's no control group or randomized comparison mentioned — PG&E's "13%/7% reduction" claim is a **before/after or correlational estimate**, not from a randomized trial. Regulators immediately questioned it: the state's Office of Energy Infrastructure Safety director said **"I was astonished at that number"** and is now independently reviewing the data underlying PG&E's claim, and a third-party consultant (Filsinger) requested more detail and a third-party review that hadn't yet been granted.
- PG&E's own COO admitted a confound: the program's estimate of "hazardous trees" *increased* over time as inspection improved — meaning the denominator/target kept shifting, which muddies any before/after comparison of ignition rates.
- **The decision stakes are asymmetric and hard to reverse:** PG&E is betting ~$1B+ in reallocated spending (and leaving 385,000 identified hazardous trees untrimmed for up to 9 years) on the new line-shutoff technology being sufficient — a Type II-error-like risk (missing a real fire risk) with potentially catastrophic, irreversible consequences (more fires, more deaths) if the internal analysis was wrong or optimistic.
- This is a real-world instance of the chapter's core theme applied to **causal effectiveness claims** rather than sampling: "13% reduction" is a *statistic* being used to justify walking away from a costly intervention — exactly the kind of number a manager should interrogate the way the chapter teaches (What's the underlying data? Is it representative/causal? What's the cost of being wrong in each direction — continuing an ineffective program (Type I-like, wasted spend) vs. abandoning an effective one (Type II-like, fire risk)?).

**Discussion questions to prep:**
- What additional data would you want to see before believing PG&E's 13%/7% number (e.g., a comparison to circuits that didn't get the tree-trimming treatment)?
- Given the asymmetric cost of a missed fire risk vs. wasted tree-trimming spend, was PG&E's board right to make this bet based on an internal, unreviewed analysis?

---

## Cross-cutting themes across all four case studies
1. **Bias from non-response/self-selection persists no matter how much data you collect** (WorstCaseBounds' bound-width formula makes this mathematically explicit; the survey weighting example shows the same thing empirically).
2. **Reweighting/bounds only fix what you can observe** — an unobservable correlation between the outcome and who responds/survives/gets treated remains unfixable (cancer screening's "population of interest" problem; the weighting example's fine print; echoes Oster/NHANES from Class 1).
3. **A single summary statistic ("13% reduction," "NPS of 62," "annual mammograms cut deaths 20%") can hide the assumptions and trade-offs that produced it** — always ask what population, what comparison group, and what values went into producing that number before acting on it.
4. **Relative vs. absolute framing changes how "big" an effect looks** — always ask "percent of what?" (mammogram lesson 2; also relevant to PG&E's "13%/7%" reduction — 13% of *what* base ignition rate?).
