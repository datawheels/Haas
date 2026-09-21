# Class 1 Case Studies — In-Depth Notes (Chapter 13: Where Data Comes From)

## Suggested study order
1. Class-Introduction.pdf / Class Introduction - eBay - handout.pdf
2. Chapter-13.pdf (core theory)
3. Emily Oster — "Where Does Data Come From"
4. SFNext poll methodology + "victim of a crime" article
5. Vaccination Rates (Nature, Bradley et al.)
6. NYT "Are the Polls Still Missing Hidden Republicans"
7. NYT "Polling Averages Can Be Useful..."
8. Chapter 13 Knowledge Check → KC1_solutions.pdf

---

## 1. Emily Oster — "Where Does Data Come From" (ParentData)

**Core question:** How do we know "42% of Americans are obese"? Who got weighed, and how do you go from measuring some people to a statement about everyone?

**Key points:**
- The ideal (infeasible) measurement: weigh every American daily. Real proxies (medical records, apps, fitness trackers, DMV records) are convenient but **not representative** — people who see doctors, use fitness trackers, or renew licenses differ systematically from the general population.
- The actual source for obesity data is **NHANES** (National Health and Nutrition Examination Survey): ~5,000 people/year since the 1960s (current form since 1999), with two parts — (1) a survey on demographics/diet/health, and (2) a physical **examination** (weight, blood pressure, labs) done in mobile exam units.
- NHANES sampling: randomly picks ~15 counties/year, then random households, then random individuals — a multi-stage random sample, not a national simple random sample (that would be logistically impossible).
- **The core problem: non-response.** Only ~half of contacted people agree to be surveyed, fewer agree to the physical exam. Refusal is **not random** — Black individuals are less likely to opt in (linked to historical mistreatment by the medical system), more-educated and richer people are more likely to participate.
- **The fix: reweighting.** Undersampled groups (e.g., a Black respondent in a sample that has too few Black people relative to the population) get counted with a higher weight; oversampled groups get downweighted. NHANES also deliberately **oversamples** small subgroups upfront to have enough people to weight properly.
- **Two subtleties/limits of weighting:**
  1. You need enough people in each subgroup to weight meaningfully.
  2. **You can only weight on things you observe.** Unobservable differences (e.g., who happens to own a fitness watch, or subtler traits driving non-response) can't be corrected for — bias from these is invisible and unfixable.
- **Takeaway:** Even best-practice, professionally designed representative sampling (NHANES) still has unresolved representativeness gaps due to non-response. This is the same core issue in political polling (people who don't answer polls differ from those who do) — "where does data come from" and "who's missing" matter as much as measurement itself.

---

## 2. SFNext Poll methodology ("How the SFNext poll was conducted")

**What it is:** A SF Chronicle-commissioned poll of San Francisco residents' attitudes on city life, government performance, safety, etc.

**Methodology facts:**
- Random sample of **1,653** SF residents, age 18+.
- Conducted **June 27 – July 11, 2022** — notably right after DA Chesa Boudin's recall (June 7) and just before new DA Brooke Jenkins was sworn in (July 8) — timing matters for interpreting results.
- Mixed mode: online questionnaires **and** telephone interviews.
- Designed by Jon Krosnick (Stanford, nationally recognized survey methodologist) with Chronicle editors; fielded by research firm SSRS.
- Respondents were paid a **$20 gift card** incentive.
- Data was **statistically weighted** to match Census demographics (race, education) — same reweighting logic as NHANES/Oster's piece.
- Available in **English and Cantonese** (92 respondents used Cantonese) — a deliberate step to reduce language-based non-response bias, though the linked crime article shows this still didn't fully solve representativeness concerns for Asian immigrant subgroups.

**Why it's a good case study:** shows a real, contemporary example of the "ideal vs. actual" sampling problem from Oster's piece — random sampling + weighting + multilingual outreach — and it's the raw methodology behind the "victim of a crime" article below.

---

## 3. SF Chronicle — "Here's how many San Franciscans say they've been the victim of a crime"

**Headline findings (SFNext poll, n=1,653):**
- **45%** of respondents said they'd had an item stolen in the last 5 years; **24%** said they'd been threatened or physically attacked.
- Only **18%** rated SF police as good/excellent; **41%** rated them poor/very poor.
- Racial breakdown of theft victimization: Black 54%, mixed-race 55%, Hispanic 50%, White 43%, Asian 43%.
- Racial breakdown of violence: Hispanic/mixed-race highest (36%), Asian **lowest** (19%) — this *conflicts* with other reporting (e.g., Stop AAPI Hate documenting 11,500+ anti-Asian incidents nationally 2020–2022) suggesting a wave of anti-Asian violence.

**The methodological lesson (this is the point of assigning it alongside the methodology piece):**
- Poll participants who identified as Asian (Stan Zhang, Victoria Ku) themselves questioned the 19% figure, raising **selection bias**: the poll may not have reached older, monolingual Asian immigrants (who rely on Chinese-language media, not Chronicle outreach).
- Cultural reluctance to report victimization ("people tend to shelter themselves") and distrust of institutions/pollsters (noted also by a former city supervisor) may suppress self-reported rates independent of true incidence.
- **Even with a "random sample" and a Cantonese-language option, real bias can persist** — this is a concrete, real-world instance of Oster's "you can only weight on what you observe" problem: the poll weighted on demographics it *measured*, but couldn't correct for unmeasured factors like language comfort, immigration-related distrust, or cultural reporting norms.
- Good discussion question: is the 19% figure *wrong*, or does it reflect real variation you should not assume matches anecdotal/media narratives? The article deliberately doesn't resolve this — it's an exercise in interpreting a data anomaly.

---

## 4. Bradley, Kuriwaki, Isakov, Sejdinovic, Meng & Flaxman — "Unrepresentative Big Surveys Significantly Overestimated US Vaccine Uptake" (*Nature*, 2021)

**This is the most rigorous/technical reading — the theoretical backbone of the whole class.**

**The "Big Data Paradox":** bigger sample size shrinks your *confidence interval* but does nothing to fix *bias* — and if your sample is unrepresentative, more data makes you **more confidently wrong**, not less wrong.

**The three surveys compared (all measuring US COVID-19 first-dose vaccine uptake, Jan–May 2021):**

| Survey | Sample size | Recruitment | Accuracy vs. CDC benchmark |
|---|---|---|---|
| Delphi–Facebook | ~250,000/week | Facebook active users | Overestimated uptake by **17 points** by May 2021 |
| Census Household Pulse | ~75,000/wave | Households with phone/email on file | Overestimated by **14 points** |
| Axios–Ipsos | ~1,000/wave | Address-based probability panel (KnowledgePanel), incl. offline households given internet access | Tracked CDC closely (within a few points); 95% CIs contained the true value in 10/11 waves |

**Key finding:** Despite being **250x smaller**, Axios–Ipsos was far more accurate than Delphi–Facebook because it was recruited via a better (probability-based, representative) sampling frame — proving **data quality beats data quantity**.

**The math (their error decomposition):**
> Total Error = Data Defect Correlation (bias) × √(Data Scarcity) × Inherent Problem Difficulty

- **Data defect correlation (ddc):** correlation between "did this person respond" and "what their true answer is." If people who got vaccinated are more likely to respond, uptake gets overestimated. This is the single most important term — even a *tiny* ddc, multiplied by a huge population, produces large absolute error.
- They show Delphi–Facebook's 250,000-person survey had a **"bias-adjusted effective sample size" of under 10** by April 2021 — i.e., mathematically no more informative than a random sample of 10 people, once you account for its bias.
- Why the bias existed: Delphi–Facebook didn't weight by education or race/ethnicity, so it overrepresented white, college-educated respondents (who were more likely to be vaccinated) by wide margins (Table 2 in the paper).

**Why this pairs with the other readings:** it's the mathematical formalization of exactly what Oster and the SFNext crime article show anecdotally — random sampling design + honest accounting for who's missing matters more than sheer scale. Good to read *last* among the case studies since it gives you the vocabulary (ddc, data scarcity, bias-adjusted effective sample size) to name what you saw informally in the other pieces.

---

## 5. NYT (Nate Cohn) — "Are the Polls Still Missing 'Hidden' Republicans? We're Going to Find Out."

**The experiment:** Ahead of the 2022 Wisconsin midterms, NYT/Siena partnered with Ipsos to test whether **paying people more** to respond fixes non-response bias.
- Standard NYT/Siena phone poll: ~2% response rate.
- New mail survey: households were mailed $2 up front + promise of $25 more for completing it (online or by mail) → **~24% response rate** (~12x higher).
- A parallel online probability panel (Ipsos KnowledgePanel) was also run for comparison.

**Hypothesis being tested:** polls have systematically underestimated Republicans/Trump support in 2016/2018/2020 because Trump-leaning voters are less likely to respond to pollsters ("non-response bias"). Would a **much higher response rate** capture more of these "hidden" respondents and shift results?

**What they found (surprising/nuanced result):**
- The high-incentive mail survey and the standard low-incentive phone poll landed on **similar topline numbers** (Senate race roughly tied in both) — no dramatic "unlocking" of a hidden Republican vote.
- But there **were** real compositional differences in *who* responded:
  - Mail respondents were more politically **moderate and disengaged**, less likely to say they'd definitely vote.
  - Mail respondents were more likely to have "No Trespassing" signs, less likely to want a people-facing job, more supportive of deporting undocumented immigrants, more likely to be married/lifelong Wisconsin residents.
  - Phone respondents skewed toward political engagement and were reachable partly *because* cell numbers on voter files systematically favor people who registered more recently (a subtle sampling-frame artifact).
- **Lesson:** raising response rate doesn't automatically fix bias — it can surface a *different* kind of non-response bias (reaching disengaged moderates rather than "hidden partisans"). Also illustrates that **mode of survey** (mail vs. phone) and **incentive design** both shape who answers, independent of the underlying opinions you're trying to measure.

---

## 6. NYT (Nate Cohn) — "Polling Averages Can Be Useful, but What's Underneath Has Changed"

**Context:** 2022 midterms, discussing NYT's polling average methodology.

**Core argument:** A polling average is only as good as the *pollsters* feeding it, and **the mix of pollsters changed dramatically in 2022**:
- Traditional, transparent pollsters (Monmouth, Quinnipiac, ABC/WaPo, CNN/SSRS, Fox News, NYT/Siena, Marist) conducted far fewer polls than usual, some none at all in battleground states.
- A wave of **partisan/Republican-leaning firms** (Trafalgar Group, Rasmussen, Insider Advantage) filled the gap — none adhering to industry transparency/data-collection standards, and producing systematically more Republican-friendly numbers.
- Result: in some states, nearly all recent polls came from one "camp," so the average could swing wildly week to week depending on **which kind of pollster happened to publish most recently** — not necessarily real movement in voter opinion.
- Concrete example: Pennsylvania — four Republican-leaning firms showed Oz ahead one week; four traditional pollsters showed Fetterman tied/ahead the next week; the "average" landed near a tie, but that tie is really just an artifact of *whose polls got averaged*.

**Why it belongs in this set:** it's a real-time illustration of a distinct data-quality problem from the others — not sampling bias *within* one survey, but **selection/composition bias in which surveys get included in an aggregate**, and how a supposedly neutral tool (weighted averaging by recency) can encode hidden bias if its inputs aren't representative of "all polling approaches." Complements the ddc/representativeness lens from the Nature paper by showing it at the level of aggregating *multiple* surveys rather than one.

---

## Cross-cutting themes to review before the Knowledge Check
1. **Representativeness ≠ sample size.** A small, well-designed sample (NHANES, Axios–Ipsos) beats a huge, poorly-recruited one (Delphi–Facebook, Trafalgar-style polls).
2. **Non-response is never random.** Who refuses to answer correlates with the very thing you're measuring (vaccination status, crime victimization, political preference) — this is the "data defect correlation" idea.
3. **Weighting only fixes what you can observe.** Unmeasured differences between respondents and non-respondents remain a permanent, unresolvable source of bias.
4. **More data can make bias worse, not better** — the Big Data Paradox: huge N produces tiny (falsely confident) confidence intervals around a biased number.
5. **Aggregation (polling averages) inherits the biases of its inputs** — an average isn't automatically more trustworthy than its constituent parts.
