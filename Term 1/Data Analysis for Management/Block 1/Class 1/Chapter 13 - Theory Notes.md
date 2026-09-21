# Chapter 13: Samples and Surveys — Theory Notes

Source: Chapter-13.pdf (lecture slides, Prof. Reed Walker, XMBA 200S).
Note: this is a **slide deck**, not a full chapter — it's terse and leaves several questions unanswered for in-class discussion. Below is the deck's content, followed by what's missing/worth adding to actually study from it.

---

## 1. The core framing
Managers rarely have all the data they want (on customers, production, employees) — or if they do, it's too large to be usable. So the two questions this chapter answers:
1. **How should you select a sample** (this chapter)?
2. **What can you say about the population from it, and how precisely** (next chapter — statistical inference)?

## 2. Two crucial issues with any sample
1. **Sampling variation** — your estimate won't be exactly right just by chance, but statistics can quantify *how close* you're likely to be.
2. **Bias** — your estimate may be *systematically* wrong (wrong on average, no matter how much data you collect).

> **This is the single most important distinction in the chapter: variation shrinks with more data; bias does not.** (This is exactly the point the Nature vaccine-uptake paper proves mathematically — see the other notes file.)

## 3. Running example: J.D. Power's Vehicle Dependability Study
- Surveys ~33,000 original owners of 3-year-old vehicles.
- Measures "problems per 100 vehicles" (PP100) across 184 problems in 9 categories.
- Used throughout the deck as the concrete case for illustrating sampling design choices.

## 4. Key definitions
| Term | Definition |
|---|---|
| **Population** | The entire collection of interest |
| **Census** | A comprehensive survey of the *entire* population |
| **Sample** | A subset of the population |
| **Survey** | Posing questions to a sample to learn about the population |
| **Representative** | A sample that reflects the mix of the entire population |
| **Bias** | Systematic error in selecting the sample |
| **Parameter** | A characteristic of the *population* (e.g., population mean μ) |
| **Statistic** | An observed characteristic of a *sample* (e.g., sample mean x̄) |

**Sentence of the day:** "There is one population, but there are many different samples."

### Notation table (slide 23 — "It's all Greek to me")
Population parameters get Greek letters; sample statistics get the Roman-alphabet equivalent:

| Name | Sample Statistic | Population Parameter |
|---|---|---|
| Mean | ȳ | μ (mu, "mew") |
| Standard Deviation | s | σ (sigma) |
| Correlation | r | ρ (rho, "row") |
| Slope of line | b | β (beta) |
| Proportion | p̂ (p-hat) | p |

Memorize this pairing — it's used constantly for the rest of the course (e.g., confidence intervals for μ using x̄, regression slope β estimated by b).

## 5. Eliminating bias: randomization
- A **random sample** is the best way to get a representative sample — it ensures that, *on average*, the sample mimics the population.
- **Simple Random Sample (SRS):** every item in the population has an equal chance of being chosen; the "gold standard" other methods are judged against.
- **Mechanic:** assign each population member a random number from Uniform[0,1]; to get a 10% sample, keep everyone with a number < 0.10.

## 6. Alternatives to SRS
| Method | How it works | When to use it |
|---|---|---|
| **Stratified sample** | Split population into strata (similar-item subgroups), then SRS *within* each stratum | When you want guaranteed representation of subgroups (e.g., by vehicle brand/segment) or need enough sample size in small subgroups — the same logic as NHANES *oversampling* in the Oster reading |
| **Cluster sample** | Split population into geographic (or other) clusters, randomly select *clusters*, then randomly sample *within* selected clusters | When the population is large/spread out and clusters are internally homogeneous — saves cost vs. SRS. Example given: the CPI (Bureau of Labor Statistics) — random markets → random stores within markets → price "basket" |
| **Voluntary response sample** | People self-select to participate | Cheap, but **not representative** — a big red flag method (this is the "who volunteers is not who you want" problem) |

## 7. Biased samples: two main sources
1. **Selection into the sample** — who ends up being asked/measured at all (sampling frame problems, non-random selection, cluster/stratum mis-design).
2. **Problems with the survey design** — question wording, incentive structure, mode (phone/mail/online), etc.

### The polling problem (Nate Silver quote)
> "The foundation of opinion research has historically been the ability to draw a random sample of the population. That's become much harder to do."

**Key question for any sample:** *who is left in; who is left out — and does the excluded group look like the included group?* If yes, you're fine. If no, you have **response bias** (non-random selection into the survey) — regardless of how big your sample is.

## 8. Best practices
**As a data producer:**
- Randomize.
- Match your sampling frame to your actual target population.
- Reduce non-response (e.g., financial incentives).

**As a data consumer:**
- Understand how the sample was selected before trusting it.
- Be skeptical of low response rates.

## 9. Bridge to inference (next chapter)
- **Statistical inference:** using a sample *statistic* to learn about the population *parameter*.
- **Sampling variability:** "statistics are noisy" — if you ran the same survey 1,000 times, you'd get 1,000 slightly different sample means. This is the *price* of using a sample instead of a census, illustrated with the coin-flip thought experiment (10 flips of a fair coin won't always give exactly 5 heads).

**The JD Power histogram (slide 25):** the deck shows a simulated result of running 1,000 surveys of 100,000 vehicles each from the *same* population, and plotting the 1,000 resulting sample-mean PP100 scores. The result is a bell-shaped histogram centered around ~180, ranging roughly 176–184 — this is the **sampling distribution** made concrete: even with an identical, unbiased sampling process every time, no two survey runs give the exact same sample mean, but the results cluster tightly around the true population value. This is the picture behind "statistics are noisy."

**Bias vs. Variability — the bullseye diagram (slide 28).** This is one of the most important visuals in the deck and is easy to miss since it's image-only. Four dartboard panels:
- **(a) High bias, low variability** — all shots clustered tightly together, but off to one side, away from the bullseye. Consistent, but consistently *wrong*.
- **(b) Low bias, high variability** — shots scattered widely but centered *around* the bullseye on average. Correct on average, but any single shot (survey) could be far off.
- **(c) High bias, high variability** — shots scattered widely *and* off-center. Worst case: neither accurate nor precise.
- **(d) The ideal: low bias, low variability** — shots tightly clustered right on the bullseye.

> **Key takeaway printed on the slide:** "Properly chosen statistics computed from **random samples of sufficient size** will have low bias and low variability."

This diagram is the visual proof of why the chapter separates bias and variation as two *independent* problems: **more data (bigger n) shrinks variability** (moves you from (b)/(c) toward tighter clustering) **but does nothing about bias** (a biased sampling method stays stuck at (a)/(c) no matter how large n gets). This is exactly what the Nature vaccine-uptake paper demonstrates with real numbers — Delphi-Facebook is case (a): huge sample (tight cluster) but way off-target (biased).

- Because of this, later chapters talk in terms of **confidence** rather than certainty — we won't know the true parameter for sure, but unbiased samples let us learn a lot about it anyway.

## 10. The punchline: what to do about a biased sample
1. Run another survey — try to sample better, or reach the people you missed.
2. Statistically adjust your inference to account for bias — techniques like **bounds** or **imputation** (covered later in the course).

## 11. In-class knowledge check (unanswered prompt)
Apple has a firmware update for the iPhone 17.
- How should they deliver it (in-store vs. automatic download)?
- Should they charge for it, and how much?
- Task: design a sample/survey to gather this information.

---

## What's missing from the slide deck (worth adding when you study this)

The deck is built around **discussion prompts it doesn't answer** and terms it doesn't fully explain. Fill these gaps before class:

1. **Answer: "What might be some problems with a simple random sample?"** (posed but left blank in the deck)
   - Needs a full, up-to-date sampling frame (list of the *entire* population) — often doesn't exist or excludes people (e.g., no cell-phone-only households, no unlisted numbers).
   - Can be expensive/slow to contact a scattered random sample (no efficiency gains from geographic clustering).
   - Small subgroups may end up with too few sampled members to say anything precise about them (motivates stratification).
   - Doesn't fix **non-response bias** — random selection ≠ random *response*.

2. **Answer: "Why might J.D. Power want a stratified sample?"** (also left blank)
   - To guarantee enough respondents *per vehicle make/model* (a small-selling model could get zero people in a pure SRS) so they can report reliable PP100 scores at the brand/model level, not just overall.

3. **A worked numerical example of sampling variability** — the deck only gestures at "flip a coin 10 times" and "JD Power ran 1,000 surveys." It would help to actually compute/see a sampling distribution (e.g., simulate sample means from repeated draws) to make "statistics are noisy" concrete before the next chapter's formulas (standard error, margin of error, confidence intervals) — this chapter sets up vocabulary the next chapter operationalizes.

4. **Explicit link between bias types and the four case-study readings** (the deck doesn't reference them, but they're clearly meant to illustrate it):
   - *Voluntary response bias* → none of the readings use this directly, but it's the implicit contrast to NHANES/SFNext/Axios-Ipsos's deliberate random+weighted designs.
   - *Selection/non-response bias* → Oster (NHANES), SFNext crime poll (Asian-violence undercount), Nature paper (Delphi-Facebook/Household Pulse vs. Axios-Ipsos), NYT hidden-Republicans mail experiment.
   - *Sampling frame problems* (a specific selection-bias subtype not named in the deck but present in the readings) → Nature paper's "dominating population size" discussion (Census Household Pulse excludes ~20% of households lacking phone/email on file) and NYT's point that cell-phone-linked voter files skew toward recently-registered voters.
   - *Weighting to fix *observed* imbalance, and its limits* → Oster's clearest contribution; not in this slide deck at all, yet essential to understanding "bias" as more than a binary (present/absent) — worth writing in the margin next to the deck's "Best Practices" slide.

5. **Definitions the deck uses without defining:** "sampling frame" (the list/mechanism used to reach the population — distinct from the population itself) and "response bias" (used once, undefined) — both are load-bearing terms in the discussion questions and should be defined before the knowledge check.

6. **A concrete stratified vs. cluster comparison table** — the deck presents them as parallel bullet lists but doesn't contrast *why* you'd pick one over the other (stratified = guarantee subgroup representation & precision; cluster = save cost/logistics when population is geographically dispersed, accepting some precision loss from within-cluster homogeneity). Worth drawing out explicitly since exam/knowledge-check questions likely hinge on picking the right method for a given scenario.

7. **"Bounds" and "Imputation"** are name-dropped as bias-correction tools with a "link on bCourses" — that linked material isn't in this folder; check bCourses for it, since the deck treats it as required follow-up reading, not optional.

---

## Gulsher questions (along with clarification)

**Q: I'm confused about Stratified sample and Cluster sample, need example.**

A: Same scenario, two different designs — J.D. Power surveying car owners across the US.

**Stratified Sample** — split the population into groups (strata) based on a characteristic *you care about* (e.g., car brand: Toyota, Ford, Tesla...), then randomly sample **within every group**. You survey people from **every** stratum — nothing is skipped. Guarantees even small groups (e.g., Tesla owners, only 2% of the population) get enough respondents to say something reliable about them.

**Cluster Sample** — split the population into groups (clusters) based on **convenience/geography** (e.g., cities: Chicago, Denver, Atlanta...), randomly pick a **few whole clusters**, then only sample within those chosen clusters. You **never visit the other clusters at all**. Saves cost/logistics when it's expensive to spread surveyors everywhere, and clusters are similar enough to each other that a random handful represents the rest.

| | Stratified | Cluster |
|---|---|---|
| Groups based on | A trait relevant to your question (brand, income, age) | Convenience/geography |
| Which groups get surveyed | **All** of them | Only a **random subset** of them |
| Within a group | Sample randomly | Sample randomly (only in chosen groups) |
| Goal | Guarantee representation of every subgroup | Save cost/logistics |
| Precision | Higher (no group is left out) | Lower (whole regions are missing) |

**Memory trick:** Stratified = "sample from **every** slice of the pie." Cluster = "pick a **few** slices of pie, then eat all of those slices."

The CPI example from the slides is a clean cluster case: BLS randomly picks a handful of *cities* (clusters), then randomly picks *stores* within those cities — it never visits every city in America, trusting that the randomly chosen cities are representative enough of "cities in general."

---

**Q: "If you draw a potentially-biased sample, what can you do? … 'Bounds' or 'Imputation' (link on bCourses)" — explain with example.**

A: These are the two standard tools for handling a biased/non-representative sample when you're stuck with the data you have and can't just re-survey.

**Bounds (a.k.a. worst-case/Manski bounds)**
Idea: instead of guessing the missing values, calculate the **full range** the true answer could fall in, given only what you're certain of — no assumptions about who didn't respond.

Example: Census Household Pulse gets a 20% response rate; of those who respond, 50% say they're vaccinated. You have no idea about the other 80%. Instead of reporting "50% vaccinated" (which assumes non-respondents look just like respondents), compute two extremes:
- Lower bound: assume every non-respondent is unvaccinated → 0.20×50% + 0.80×0% = **10%**
- Upper bound: assume every non-respondent is vaccinated → 0.20×50% + 0.80×100% = **90%**

Honest, assumption-free statement: the true rate is somewhere between 10% and 90%. Wide and unsatisfying, but *guaranteed correct* given only the response rate. You can narrow it by adding weaker, more defensible assumptions (e.g., "non-respondents are vaccinated at no more than the county average"), trading some certainty for a tighter range.

**Imputation**
Idea: instead of leaving gaps blank or dropping non-respondents, **predict** a plausible value for each missing data point using other information you have about that person, then analyze the "completed" dataset as if it were real.

Example: 1,000 survey respondents, but 100 skip the income question (skipping is itself often correlated with income, so just dropping them biases the average). Instead:
1. Build a model using the 900 who did report income, predicting income from things observed for everyone (education, job title, zip code, age).
2. Use that model to impute a predicted income for each of the 100 non-responders.
3. Compute the average income using all 1,000 people (900 real + 100 imputed).

This doesn't recover the true individual values, but it uses the correlational structure in the data to make a much better guess than "ignore them" or "assume they're average."

**Contrast:** Bounds give an honest *range* with minimal assumptions (good for a defensible worst-case answer). Imputation gives a single *point estimate* by leaning on a model (good when you need one number to act on, but only as good as the imputation model's assumptions).
