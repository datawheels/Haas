# Class 3 Case Studies — In-Depth Notes (Chapter 15: Confidence Intervals)

## Suggested study order
1. Chapter-15.pdf (core theory — see companion "Chapter 15 - Theory Notes.md")
2. NYT — "How the Polls Got It So Wrong in Wisconsin" (the real-world failure that motivates "Caution: Margin of Error w/ Non-Response")
3. `Chapter 15 (beyond) - TotalMarginOfError_calculator.xlsx` (the formal fix for exactly the Wisconsin problem — builds directly on Chapter 14's worst-case bounds)
4. Team Assignment 2 — Unemployment Rate (apply everything to CPS data; see "Unemployment Rate Calculation.md" for worked answers to the first two questions)

---

## 1. NYT — "How the Polls Got It So Wrong in Wisconsin"

**The story:** In Wisconsin's 2026 Democratic gubernatorial primary, polls for months showed Francesca Hong (a democratic socialist) as the dominant front-runner — as recently as the final week, she led David Crowley by **18 points** in his own campaign's internal poll and by **22 points** in a State Navigate poll. Crowley won anyway, by less than half a percentage point (~4,000 votes). A similar polling miss happened the same week in Michigan's Senate primary (Dr. Abdul El-Sayed underperformed his polls).

**The twist that makes this a great case study — the polls weren't wrong about Hong, they were wrong about Crowley:**
- Most surveys predicted Hong would win ~40% of the vote; she actually won **39%** — essentially spot-on.
- What the polls missed entirely was **Crowley's support**: he outperformed the Marquette poll's estimate for him by **more than 30 points**. The polls' error wasn't in overestimating the leader — it was in almost completely failing to capture where the *other* votes would go.

**Five explanations pollsters/journalists offered — each maps onto a concept from this course:**

1. **A genuinely volatile, late-moving race** — Crowley suspended his campaign, then re-entered it just a month before the election; Hong faced last-minute negative press (resurfaced old social-media posts). Polls taken weeks earlier were measuring a race that had since changed. This isn't a *statistical* error at all — it's the reminder that a confidence interval only describes uncertainty *at the moment of sampling*, not future changes in the underlying population.

2. **Late-deciding, undecided voters broke disproportionately for one candidate.** As many as **one-third of voters** told pollsters they were undecided heading into election day — in primaries especially, voters often don't tune in until the final days. When such a large "undecided" block exists, the poll's *reported* margin of error (which only describes sampling noise around the decided respondents) radically understates the true uncertainty in the final outcome.

3. **Non-response bias (the same concept as Chapter 14's Mitigation #5 and this chapter's "Caution" slide), stated explicitly by name in the article:** a State Navigate pollster said plainly, *"One candidate's supporters were just more eager to answer the poll."* Hong's younger, more online, more enthusiastic base may have simply been more likely to respond to surveys — inflating her measured support relative to her true support, independent of any sampling error. The Michigan pollster used almost identical language: "more enthusiasm does not necessarily equal more votes."

4. **A flawed likely-voter model overrepresenting young voters.** Crowley's own campaign manager pointed out (in a memo before the election) that Wisconsin surveys expected roughly *twice* as many young voters (18–45) as had actually shown up in 2018 and 2022 — and Hong polled strongest among young voters. This is a **sampling-frame problem** (Chapter 14, mitigation category #1): the *frame* pollsters modeled ("likely primary voters") didn't match the true electorate that showed up.

5. **Open-primary uncertainty about partisan turnout.** Wisconsin and Michigan have open primaries with no party registration, so pollsters must *guess* what share of Republicans/independents will vote in a Democratic primary — a structural modeling assumption baked into every "likely voter" estimate, invisible in the reported margin of error.

**Why this article is the perfect companion to slide 29's "Caution: Margin of Error w/ Non-Response":** every single explanation above is a source of error that a standard, textbook 95%-CI or margin-of-error calculation **completely ignores** — MoE = 2×SE only quantifies *random sampling noise*, not late shifts in opinion, non-response, frame mismatch, or turnout-model error. A poll can report "±3 points" with great apparent precision while being off by 20+ points on a candidate, because nearly all of the real uncertainty was never in the reported number to begin with.

---

## 2. The Total Margin of Error (TME) Calculator

`Chapter 15 (beyond) - TotalMarginOfError_calculator.xlsx` operationalizes the fix for exactly the Wisconsin problem, based on **Dominitz & Manski (2025), "Using Total Margin of Error to Account for Non-Sampling Error in Election Polls,"** *JASA Applications & Case Studies*. It's the direct successor to Chapter 14's worst-case-bounds mitigation, now combined formally with ordinary sampling error.

### Sheet 1: TME Calculator — the core method

**Inputs:** 1,250 voters contacted, 1,000 completed responses (r = 0.8), 60% of respondents support Candidate A. You also set an assumed min/max support among *non*-respondents (default: 0% to 100%, i.e., pure worst-case bounds — same as Chapter 14's WorstCaseBounds.pdf).

**Step 1 — response rate and the known piece:**
- Response rate r = completed/contacted = 1000/1250 = **0.80**
- Known component = r × respondent share = 0.80 × 0.60 = 0.48

**Step 2 — the identified interval (the worst-case bounds, exactly as in Chapter 14):**
- Lower bound = r×share + (1−r)×min = 0.48 + 0.20×0 = **48%**
- Upper bound = r×share + (1−r)×max = 0.48 + 0.20×1 = **68%**
- Interval width = 68% − 48% = 20 percentage points (= the nonresponse rate, when the assumption band is 0–100%)

**Step 3 — two different point estimates:**
- **Conventional** point estimate = 60% (just the respondent share, ignoring non-response entirely — what a normal poll reports)
- **Midpoint** estimate = (48%+68%)/2 = **58%** (the center of the honest bound)
- **Worst-case bias** = the maximum distance from your chosen point estimate to either bound. For the conventional estimate (60%): max(60−48, 68−60) = 12 points. For the midpoint (58%): (68−48)/2 = 10 points.

**Step 4 — combining sampling error with non-response bias into one number (the actual innovation):**
- Sampling SE = √[p̂(1−p̂)/n] = √(0.6×0.4/1000) ≈ **1.5%**
- Conventional reported MoE = 1.96 × SE ≈ **3.0%** — this is the number a normal poll would publish: "60% ± 3%"
- **TME = √(worst-case bias² + SE²)** — combines the *bias* from non-response with the *variance* from sampling into a single margin, analogous to how total error = bias² + variance² in general statistical theory
  - Using the midpoint estimate: TME = √(10² + 1.5²) ≈ **10.1%**
- **Share of TME² coming from non-response (not sampling)** — in this example, the vast majority of total uncertainty comes from the bias term, not the sampling term, because 20% of contacted voters never responded at all.

**The "honest headline" the spreadsheet generates:**
> Reported: 60.0% ± 3.0% (sampling error only)
> Honest: somewhere between 48.0% and 68.0% — midpoint 58.0% ± 10.1% (TME)

The gap between these two lines *is* the entire lesson: the number that gets published is dramatically more precise-looking than what the data can actually support once non-response is honestly accounted for.

### Sheet 2: Response Rate Scenarios — historical decline in poll quality
Holds respondent share (60%) and n (1,000) fixed, and varies only the **response rate**, to show how much of a poll's *true* uncertainty comes from response rate alone — not sample size:

| Scenario | Response rate | Lower bound | Upper bound | Width | Reported MoE (unchanged) |
|---|---|---|---|---|---|
| 1990s phone poll | 80% | 48% | 68% | 20 pts | ~3.0% |
| Good panel today | 50% | 30% | 80% | 50 pts | ~3.0% |
| Typical online panel | 20% | 12% | 92% | 80 pts | ~3.0% |
| Modern phone poll | 5% | 3% | 98% | 95 pts | ~3.0% |

**The discussion prompt built into the spreadsheet is the entire point:** *"The reported MoE never moves. Which column actually describes what we know?"* As response rates have collapsed industry-wide (from ~80% in the 1990s to often under 10% today for phone polls), the *reported* margin of error — a fixed function of n alone — has stayed roughly the same, while the *true* uncertainty (the bound width) has exploded. This is precisely the mechanism behind headline-grabbing polling misses like Wisconsin 2026.

### Sheet 3: NPS Example — the same math in a business setting
8,000 customers emailed an NPS-style survey; 2,000 respond (25% response rate); 42% of respondents are "promoters" (rate 9–10).
- Worst-case bounds on the *true* promoter share (among all 8,000, not just respondents): [0.25×42%, 0.25×42% + 0.75] = **[10.5%, 85.5%]**
- Sampling SE (the only thing a typical dashboard would report, if anything) is tiny by comparison.
- **Built-in business decision question:** if this quarter's NPS reads 4 points lower than last quarter on the exact same instrument, is that a real drop or just noise from who happened to respond this time? What assumption about non-respondents (e.g., "unhappy customers respond at the same rate as delighted ones") would you need to defend before reacting to a 4-point move — and is that assumption actually plausible?

---

## Cross-cutting themes
1. **A margin of error / confidence interval built from SE = σ/√n only ever describes sampling noise** — it is silent about non-response, frame mismatch, late opinion shifts, or measurement bias. The Wisconsin race shows all four failure modes stacking on top of each other in one real election.
2. **Response rate — not sample size — is usually the dominant source of real-world uncertainty in modern polling and surveys.** The TME calculator's Response Rate Scenarios sheet makes this numerically explicit: reported MoE stays ~3% regardless of response rate, while the true (worst-case) bound width scales almost linearly with the non-response rate.
3. **Choosing a confidence level (or which assumptions to bake into a bound) is itself a decision that can be made in bad faith** — the Philip Morris v. EPA case (in the Theory Notes) shows a real legal/regulatory fight over exactly this: 90% vs. 95% confidence changed whether the interval crossed zero.
4. **The fix costs you something.** Every method that "corrects" a naive estimate — reweighting (Class 2), worst-case bounds (Class 2/3), or TME (this class) — either widens your reported uncertainty or requires you to state an assumption explicitly. There's no way to get both a *narrow* and an *honest* interval when non-response is severe; the honest move is to show the wide interval and say so, not to quietly report only the sampling-error component.
