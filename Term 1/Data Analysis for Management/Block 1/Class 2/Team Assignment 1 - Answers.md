# Team Assignment 1 — One Population, Many Samples
Answers (working draft)

Population truth: N = 10,266 tickets, μ = $368.79, σ = $179.72

---

## 1. Spot the biased sample

**a. Which file is the random sample? What was the selection rule behind the other one, and which column gives it away?**

`fares_sample_2.csv` is the (simple) random sample — its mean ($360.23) and SD ($175.34)
land close to the population values, and its `advance` column spans a realistic full range
(0–148 days).

`fares_sample_1.csv` is **not** random. The giveaway column is **`advance`**: every ticket
in it was purchased 7 days or fewer before departure (range 0–7), vs. 0–148 days in the
random sample. The selection rule was essentially *"only include tickets booked within a
week of travel"* — a last-minute-bookings filter.

| Metric | sample_1 (biased) | sample_2 (random) | Population |
|---|---|---|---|
| Fare mean | $511.57 | $360.23 | $368.79 |
| Fare SD | $186.48 | $175.34 | $179.72 |
| Advance-purchase mean (days) | 3.74 | 18.00 | — |
| Advance-purchase range | 0–7 | 0–148 | — |

**b. If you had used the biased sample to estimate the average fare, how far off would you be, and in which direction? What real-world survey mistake is this the same as?**

Using `fares_sample_1.csv`, the estimated average fare would be $511.57 vs. the true
population mean of $368.79 — off by about **$142.78 (≈39%), always too high** (last-minute
fares skew expensive, so restricting to that slice biases upward, not just adding noise).

This is an **undercoverage / non-representative sampling-frame** mistake — the same failure
mode as the 1936 *Literary Digest* poll (sampled only phone/car owners, a wealthier,
non-representative subgroup) or the "Dewey Defeats Truman" telephone poll: the sampling
frame was restricted to a narrow, systematically-different subgroup (last-minute travelers)
and mistaken for the whole population.

---

## 2. How much variability is there in the "sample mean" for tickets?

**c. Using only μ, σ, and n, what should the standard deviation of those 500 sample means be close to? Does the simulation check out?**

Theoretical SE = σ/√n = 179.72/√100 = **$17.97**

Simulation (500 samples, n = 100, drawn from the full population file):
- Mean of the 500 sample means: $368.53 (essentially equal to μ = $368.79)
- Simulated SD of the 500 sample means: **$17.44**

Yes — the simulation checks out; $17.44 is very close to the theoretical $17.97, and the
histogram of the 500 means is roughly bell-shaped and centered on μ, as the Central Limit
Theorem predicts.

**d. Would your answer change if the airline had sold 10 million tickets instead of 10,266? One sentence answer.**

No — the SE formula σ/√n depends only on the population's variability and the sample size,
not on population size, so the SE would stay essentially the same (the tiny finite-population
correction factor here, ~0.995, would just get even closer to 1).

---

## 3. Set your control limits

**e. Set control limits for the weekly audit at an α you choose. Justify the choice in one sentence each on the cost of a false alarm (Type I) and the cost of a missed problem (Type II).**

Choosing **α = 0.05** (z = 1.96, the standard two-sided significance level):

Limits = μ ± 1.96 × SE = $368.79 ± 1.96 × $17.97 = $368.79 ± $35.22
→ **Control band: [$333.57, $404.01]**

- *Cost of a false alarm (Type I):* Low — investigating a flagged week just means an analyst
  pulls that week's fare data and checks the pricing logs, a cheap, fast check, so occasionally
  chasing a false alarm ~5% of the time is tolerable.
- *Cost of a missed problem (Type II):* High — a broken pricing rule (like the $75
  transatlantic-ticket bug mentioned in the prompt) can bleed real revenue every day it runs
  undetected, so it's worth accepting some false alarms in exchange for catching genuine
  drifts quickly rather than waiting for an extreme, rarely-triggered signal.

**f. Investigate this week or not? Note: your answer may legitimately differ from the next team's — explain why in one sentence.**

**Yes, investigate.** $412 is above the upper limit of $404.01
(z = (412 − 368.79)/17.97 ≈ 2.41, two-sided p ≈ 0.016 < 0.05), so it falls outside the
control band.

Other teams may legitimately land elsewhere: the decision hinges entirely on the α each team
picks (e.g., a team using tighter 3σ limits, ±$53.92 → band [$314.87, $422.71], would *not*
flag $412) — it's a judgment call about the relative costs of false alarms vs. missed
problems, not a computational disagreement.

---

## AI-use statement

*TODO*
