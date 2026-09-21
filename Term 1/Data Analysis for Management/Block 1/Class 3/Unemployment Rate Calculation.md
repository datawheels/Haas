# Unemployment Rate Calculation — CPS.xlsx (March 2019)

**Dataset:** 139,931 civilian, non-institutionalized adults, March 2019 Current Population Survey.

## Step 1: The seven Employment Status categories

| Employment status | Count | Classification |
|---|---:|---|
| At work | 80,730 | **Employed** |
| Has job, not at work last week | 2,829 | **Employed** |
| Unemployed, experienced worker | 3,241 | **Unemployed** |
| Unemployed, new worker | 338 | **Unemployed** |
| NILF, retired | 22,801 | Excluded (not in labor force) |
| NILF, other | 22,726 | Excluded (not in labor force) |
| NILF, unable to work | 7,266 | Excluded (not in labor force) |
| **Total** | **139,931** | |

- **Employed** = "At work" + "Has job, not at work last week" = 80,730 + 2,829 = **83,559**
- **Unemployed** = "Unemployed, experienced worker" + "Unemployed, new worker" = 3,241 + 338 = **3,579**
- **Not in labor force (excluded from denominator)** = the three "NILF, …" categories = 22,801 + 22,726 + 7,266 = **52,793**

This mapping was cross-checked against the dataset's `Labor force status` column (Yes, in the labor force / No, not in the labor force) and matches it exactly — every "Employed" or "Unemployed" row is flagged "Yes, in the labor force"; every "NILF, …" row is flagged "No, not in the labor force."

## Step 2: Denominator

The denominator is the **civilian labor force**, not the full sample:

```
Labor force = Employed + Unemployed = 83,559 + 3,579 = 87,138
```

People who are retired, unable to work, or otherwise not seeking work (NILF categories, 52,793 people) are **excluded** from the denominator — they are neither employed nor counted as unemployed, because the unemployment rate only measures the share of people *participating in the labor market* who lack a job.

## Step 3: Unemployment rate

```
Unemployment rate = Unemployed / Labor force
                   = 3,579 / 87,138
                   = 4.107%
```

## Step 4: 95% confidence interval

Treating the rate as a sample proportion (Wald/normal approximation):

```
p  = 0.04107
SE = sqrt[ p(1-p) / n ],  n = 87,138 (labor force size)
SE = 0.000672  (0.0672 percentage points)

95% CI = p ± 1.96 × SE
        = 4.107% ± 0.132 pts
        = [3.98%, 4.24%]
```

**Result: Unemployment rate = 4.11%, 95% CI = [3.98%, 4.24%].**

## Why 3,579 ÷ 139,931 = 2.6% is *not* the unemployment rate

That calculation divides the unemployed count by the **entire sample** (139,931), including 52,793 retirees and others who aren't looking for work and were never job-seekers. Diluting the unemployed count by a denominator full of people outside the labor market makes joblessness look artificially small — it answers "what share of *all adults* are unemployed," not "what share of *people trying to work* can't find a job," which is what the unemployment rate is designed to measure. The correct denominator (87,138, the labor force) gives 4.11%, not 2.6%.
