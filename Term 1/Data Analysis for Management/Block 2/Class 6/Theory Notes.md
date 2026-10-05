# Chapters 19 & 20: Linear Patterns & Curved Patterns — Theory Notes

Source: Chapter-19.pdf "Linear Patterns" (33 slides) and Chapter-20.pdf "Curved Patterns" (43 slides), lecture slides, Prof. Reed Walker, XMBA 200S. Confirmed scope directly from the deck title slides and outlines: **Chapter 19 = constructing/interpreting the OLS regression line and the importance of residuals (simple linear regression)**; **Chapter 20 = detecting nonlinearity and fixing it with reciprocal/log transformations, plus a bonus optimal-pricing application** — matching the syllabus's Stine & Foster readings (Ch. 19, 20.1, 20.4).

---

## 1. Where this fits in the course

Both decks open with the identical "Course overview — Part 4: Building regression models" slide: *"You want to build a model to forecast outcomes from data you have. What's the best model you can build?"* This is Block 3/4's throughline. Chapter 19 answers it for the straight-line case; Chapter 20 answers it when a straight line isn't the best model. Future classes extend this to **inference** (is the slope statistically different from zero?) and **multivariate models** (more than one explanatory variable) — this class is purely about **construction and interpretation**, not yet about statistical significance.

---

## 2. Chapter 19 — Linear Patterns

### 2.1 Running example: Diamond pricing
Setup: a sample of several hundred emerald-cut, slightly "included" diamonds. Three business questions drive the whole chapter:
1. What is the relationship between price and weight?
2. What is the average price of diamonds that weigh 0.4 carat?
3. How much more do diamonds that weigh 0.5 carat cost?

The scatterplot of **Cost ($)** vs. **Weight (carats)**, restricted to the 0.3–0.5 carat range, shows a clear upward, roughly linear, positively-sloped cloud — motivating a linear model.

### 2.2 What makes a good model?
Many lines could be drawn through a cloud of points. A good one must:
1. **Not be systematically wrong in one direction** (errors shouldn't all be positive or all negative in some region)
2. **Keep the distance between prediction and actual small**

### 2.3 The OLS regression line — setup
Any linear model takes the form:
```
Estimated Price = b0 + b1 × Weight        (general form: ŷ = b0 + b1x)
```
**Residuals** are the vertical deviations from each data point to the fitted line: **e = y − ŷ**. The **Ordinary Least Squares (OLS)** line is the one specific line whose intercept b0 and slope b1 **minimize the sum of squared residuals** ("least squares") — this operationalizes both criteria in §2.2 simultaneously (squaring removes the sign, so you can't cancel a big positive error with a big negative one, and keeps distances small).

### 2.4 The least-squares formulas
```
b1 = r × (sy / sx)          [slope = correlation × ratio of the two SDs]
b0 = ȳ − b1 × x̄             [intercept = mean(y) − slope × mean(x)]
```

### 2.5 Worked example: fitting the diamond line

**Summary statistics (n = 93 diamonds, 0.3–0.5 carat range):**

| Quantity | Price ($) | Weight (carats) |
|---|---|---|
| Mean | 1,119.6 | 0.4094 |
| Median | 1,080 | 0.41 |
| Std. Deviation | 205.5273 | 0.05434 |
| Kurtosis | −0.598 | −1.0039 |
| Skewness | 0.360 | 0.0346 |
| Minimum | 714 | 0.31 |
| Maximum | 1,609 | 0.5 |
| Count | 93 | 93 |

**Correlation(Price, Weight) = r = 0.7131**

**Calculating the fitted line:**
```
b1 = r × (sy/sx) = 0.7131 × (205.5273 / 0.05434) = 0.7131 × 3,782.6 = 2,697

b0 = ȳ − b1×x̄ = 1,119.6 − (2,697)(0.4094) = 1,119.6 − 1,104.4 = 15

Estimated Price = 15 + 2,697 × Weight
```

### 2.6 Interpreting the intercept, b0
- The intercept is the portion of y present for **all** values of x — here, read loosely as a "fixed cost" of $15 per diamond.
- Formally: the intercept estimates the average response when x = 0 (where the line crosses the y-axis).
- **Caution:** the sample has no diamonds anywhere near zero weight (range is 0.31–0.5 carats), so b0 = $15 is an **extrapolation** and should be interpreted cautiously — it's a mathematical artifact of the fitted line, not a claim that a 0-carat "diamond" costs $15.

### 2.7 Interpreting the slope, b1
- The slope is the **predicted change in y for a 1-unit change in x** ("change in y over change in x"). Here: a **1-carat increase in weight is associated with a $2,697 increase in price**.
- To find the effect of a change other than 1 unit, multiply b1 by the fraction/multiple: a **0.2-carat** change ⇒ 0.2 × 2,697 = **$539**.
- The slope can be read as a **marginal cost** ($2,697/carat) in this example, but **it is not correct to call it causal** — "the slope is an association, not a change *caused* by changing x."

### 2.8 Worked example: prediction
```
Predicted price at 0.4 carat:
Estimated Price = 15 + 2,697(0.4) = 15 + 1,078.8 = $1,094

Predicted price at 0.5 carat:
Estimated Price = 15 + 2,697(0.5) = 15 + 1,348.5 = $1,363.5

Difference (price premium for 0.5 vs 0.4 carat) ≈ $270 more, on average
```
(Consistent with slide 29's direct answer: "$270 more, on average" — matches 0.1 × 2,697 = $269.7 ≈ $270.)

### 2.9 Properties of residuals
- Residuals show the variation that **remains after accounting for the linear relationship** — they should be plotted against x to check for patterns.
- **If the linear model is appropriate**, a plot of residuals vs. x should "stretch out horizontally with consistent vertical scatter" — no visible pattern (the slides call this a "visual test for association" checking for the *absence* of a pattern). The diamond residual plot does show this: scatter is centered on 0 across the full weight range with no systematic curve or funnel shape.
- **Standard Deviation of Residuals, sₑ** measures how much residuals vary around the fitted line (Excel calls this the "standard error of the regression"). For the diamond example: **sₑ = 145**. Residuals should also be checked for approximate normality (histogram of residuals).

### 2.10 R-squared (r²)
- The residuals are what the model **fails** to explain; **r²** — literally the square of the correlation between x and y — measures what the model **does** explain: *the fraction of the variation in y accounted for by the least-squares line.*
- Diamond example: **r² = 0.7131² = 0.509** → the fitted line explains **50.9%** of the variation in price.
- **r² alone never tells you whether you have a good model.** Two specific failure modes the slides flag explicitly:
  1. **It doesn't tell you the relationship is linear.** Two scatterplot pairs are shown side by side: one (Sales vs. Promotion) looks genuinely linear; the other (Profit vs. Year) has a visibly curved/bowed pattern, yet a naive r² calculation wouldn't distinguish "a line explains most of the variation" from "this specific line is the right shape." **"Don't trust summaries like r² without looking at plots."**
  2. **It doesn't tell you the relationship is causal.** Two paired examples: a **high r² that is not causal** (Nicolas Cage movies released per year & drownings — the canonical spurious-correlation example) vs. a **low r² that is still causal** (smoking on life expectancy — a real causal effect that explains only a small share of the variance in life expectancy because so many other factors matter). Lesson: r² tells you how much variation is explained, nothing about mechanism, and "some things are harder to predict than others."

### 2.11 Anscombe's Quartet & "Plot Your Data!"
- **Anscombe's Quartet**: four different (x,y) datasets that share the identical fitted regression line, yet look completely different when plotted — one is genuinely linear, one is a clean curve, one is linear-plus-one-outlier, one is a vertical stack with a single leverage point driving the whole fit. The punchline: **identical summary statistics can hide wildly different underlying patterns.**
- A companion slide ("Plot Your Data!," citing Matejka & Fitzmaurice, Autodesk Research, "Same Stats, Different Graphs") takes this further: a grid of a dozen scatterplots — scattershot, parallel lines, an X, a star, concentric circles, diagonal stripes — **all share the same mean, SD, and Pearson correlation to two decimal places.** This is the most extreme possible illustration of why you always look at the scatterplot before trusting any numeric summary.

### 2.12 Checklist for simple regression (end of Ch. 19)
1. **Always look at the scatterplot.**
2. **Describe the intercept and slope using the units of the data** (not abstract "b0/b1").
3. **Limit predictions to the range of observed conditions** (don't extrapolate — see §2.6).
4. **Can you think of any lurking variable?** Use intuition/context to evaluate other explanatory variables that might actually be driving the association between x and y.
5. **Is the relationship linear?** Use the scatterplot to see if the pattern resembles a straight line.
6. **Is the residual variation random?** Use the residual plot to make sure no pattern exists.

---

## 3. Chapter 20 — Curved Patterns

### 3.1 Motivating quick poll: fuel economy is *not* linear in MPG
Setup: a fleet manager's salespeople each drive 25,000 miles/year. Which upgrade saves more fuel: replacing a 25 MPG car with a 35 MPG car, or a 12 MPG car with a 14 MPG car? Intuition says the first (bigger MPG jump); **the correct answer is (b)**, because gallons used is the reciprocal of MPG, not linear in it:
```
25 mpg → 25,000/25 = 1,000 gallons        12 mpg → 25,000/12 = 2,083 gallons
35 mpg → 25,000/35 =   714 gallons        14 mpg → 25,000/14 = 1,786 gallons
                      ───────────                                ───────────
          286 gallons saved                           297 gallons saved
```
**Why this matters:** MPG is a ratio (miles *per* gallon), and ratios behave nonlinearly — this single counterintuitive result is the deck's motivation for the entire reciprocal-transformation section that follows.

### 3.2 Detecting nonlinear patterns: vehicle weight & fuel efficiency
Data: 303 vehicle models sold in the US; **MPG** vs. **Weight** (in thousands of pounds). The naive linear fit:
```
Predicted MPG = 43.3 − 5.19 × Weight        r² = 0.70, sₑ = 2.9 MPG
```
The scatterplot (MPG vs. Weight) shows the fitted line visibly failing to track the cloud's curvature at both ends — it overshoots light vehicles and undershoots the heaviest ones. **The residual plot is the real diagnostic**: residuals form a **bowl/arc shape** (positive at the low and high ends of weight, negative in the middle) rather than a random horizontal band — a textbook sign that the true relationship curves and a straight line is systematically wrong in different directions across the x-range (violating Ch.19's "good model" criterion #1, §2.2).

### 3.3 Transformations — definition and the two key tools
A **transformation** is the re-expression of a variable by applying a function to each observation, which lets ordinary (linear) regression describe a curved pattern. **Two transformations especially useful in business applications: the reciprocal and the logarithm.**

**Choosing a transformation — the "bulging rule" (circle diagram):** match the scatterplot's curve shape to a quadrant of a circle and read off the suggested re-expression:
- Upper-left quadrant (curving like ⌐, concave, bending down-right): try `log x`, `1/x`
- Upper-right quadrant (curving like ⌐ reversed, convex increasing): try `y²`, `x²`
- Lower-right quadrant (convex decreasing, our MPG/weight and pricing cases): try `log y`, `1/y`
- Lower-left quadrant: try `log y, 1/y` together with `log x, 1/x`

### 3.4 Reciprocal transformation — worked example
The reciprocal transform is useful whenever the variable is naturally expressed as a **ratio** — MPG (miles per gallon) is the running example; other business ratios: equity/debt, sales/employee, price/assets. Applying 1/MPG and multiplying by 100 converts "miles per gallon" into **"gallons per 100 miles"** — a quantity that *adds up linearly* with distance driven (unlike MPG itself, which is why the §3.1 poll was counterintuitive).

```
Gallons Per 100 Miles = −0.11 + 1.20 × Weight        r² = 0.71, sₑ = 0.667
```
The new residual plot is **much more randomly scattered** around zero across the weight range — confirming the reciprocal transform straightened the curve. Overlaying both fitted curves back on the original MPG-vs-Weight axes (orange = untransformed line, green = reciprocal fit converted back) shows the green curve tracks the data's bend far better, especially at the low-weight end.

**Worked interpretation:** since the transformed relationship is linear in gallons/100mi, a 200-lb (0.2-unit) weight increase has a **constant** effect regardless of starting weight:
```
Δ(Gallons per 100 Miles) = 0.2 × 1.20 = 0.24 gallons per 100 miles
```
"This relationship is the same at all weight levels" — that constancy (not true of the original MPG scale) is exactly the point of transforming.

### 3.5 The logarithm — properties
- Useful for *any* nonlinear relationship, not just ratios. **Changes in (natural) logs are approximately equal to percentage changes**, which makes logs easy to interpret. Log models are also **much less sensitive to outliers** (because log compresses large values).
- Business applications almost always use the **natural log** (base e ≈ 2.7): "the natural log of x is the exponent to which e must be raised to produce x."
  ```
  log(1) = 0        because e^0 = 1
  log(2.7) = 1       because e^1 = 2.7
  log(10) ≈ 2.3      because e^2.3 ≈ 10
  ```
- **Percentage-change property, demonstrated numerically:**

  | x | log(x) |
  |---|---|
  | 1 | 0.0 |
  | 10 | 2.3 |
  | 11 | 2.4 |
  | 100 | 4.6 |
  | 110 | 4.7 |
  | 1,000 | 6.9 |
  | 1,100 | 7.0 |

  10 → 11 is a 10% increase, and log(10) → log(11) changes by 0.1. 100 → 110 is *also* a 10% increase, and log(100) → log(110) *also* changes by 0.1 — the log-difference is scale-invariant and tracks the percentage change, not the absolute change.

### 3.6 Worked example: pet food sales and price (the log transformation in action)
Data: ~104 weeks of **Sales Volume** and **Average Price** for a pet food product.

**Step 1 — naive linear fit (Sales Volume on Price):**
```
Sales Volume = 190,480 − 125,190 × Price        r² = 0.83
```
The scatterplot (steep convex-decreasing cloud) and its residual plot (a clear **curved, bowl-shaped** pattern, with two large positive outliers at the lowest prices) both show the line is systematically wrong — overpredicting in the middle price range and badly underpredicting at the very low-price end.

**Step 2 — log-log fit:**
```
Log Sales Volume = 11.0 − 2.44 × Log Price        r² = 0.96
```
r² jumps from 0.83 to 0.96, and the residual plot after the log transform is far more randomly scattered — strong evidence the log-log form is the right functional shape. Overlaying the two fitted curves (green = log-log model converted back to levels, orange = original linear fit) on the original Sales-vs-Price scatter shows the green curve tracking the data's bend closely across the whole price range, while the orange line misses badly at the extremes.

### 3.7 Interpreting logs — elasticity
When **both** variables are logged, the estimated slope is interpretable directly as an **elasticity**: *the percentage change in y associated with a 1% change in x.*

**Worked example:** slope = −2.44 ⟹ **a 1% increase in price is associated with a 2.44% decrease in quantity** (own-price elasticity of demand = −2.44, i.e. elastic demand).

### 3.8 When to use logs
- **Use your eyes:** extreme values of the explanatory variable (very big or very small), or an obvious "bend" in the scatterplot.
- **Use your intuition:** whenever you believe **percentage changes matter, not changes in the level** of a variable — classic business examples: prices & quantity demanded, wages/income, measuring profits and productivity.

### 3.9 Three types of log models — the interpretation rules to memorize

| Model | Equation | Interpretation of b1 |
|---|---|---|
| **Log-log** | log(y) = b0 + b1·log(x) | A **1% change in x** is associated with a **b1 percent change in y** (this is the **elasticity** — "perhaps the most important of the three") |
| **Logs on levels** | log(y) = b0 + b1·x | A **1-unit change in x** is associated with a **100×b1 percent change in y** |
| **Levels on logs** | y = b0 + b1·log(x) | A **1% change in x** is associated with a **b1/100-unit change in y** |

### 3.10 Best practices (end of Ch. 20's main section)
- Anticipate whether the association between y and x is linear *before* fitting.
- Plot your data.
- Don't forget about lurking variables.
- Interpret the slope carefully (units depend on which of the §3.9 model types you used).
- **Don't compare r² between models with different responses** — e.g. you cannot directly compare the r² of "Sales on Price" (§3.6 Step 1, r²=0.83) to "log(Sales) on log(Price)" (§3.6 Step 2, r²=0.96) as if they measure the same thing, because transforming y changes what variance is even being explained. The *jump* in r² here is suggestive, but the formal comparison tool is the residual plot, not the r² values themselves.

### 3.11 Bonus example: optimal pricing via elasticity
**The core formula**, derived from profit maximization under constant elasticity demand:
```
Optimal Price = Cost × [ Elasticity / (Elasticity + 1) ]
             = Cost × γ / (1 + γ)        (γ = elasticity, a negative number for normal demand)
```

**Worked example 1 — pet food (continuing §3.6):** cost = $0.60/unit, elasticity γ = −2.44.
```
Optimal Price = 0.60 × [ −2.44 / (−2.44 + 1) ] = 0.60 × (−2.44 / −1.44) = 0.60 × 1.6944 = $1.017
```
"Estimated profit is maximized at this price."

**Worked example 2 — orange juice (independent motivating example):** a convenience-store chain wants to price a half-gallon of orange juice that costs $1 to stock and sell. The chain collected sales data across 50 store locations, each charging a different price.
```
Estimated log Sales = 4.81 − 1.75 × log Price        [elasticity γ = −1.75]
```
"A 1% increase in price leads to a 1.75% decline in sales." Residual plot vs. log price shows random scatter — "all conditions satisfied."
```
Optimal Price = cγ / (1 + γ) = $1 × (−1.75) / (1 + (−1.75)) = −1.75 / −0.75 = $2.33
```
At $2.33, each store is expected to sell **28 cartons**, for an estimated profit of **$37.24**. **Message: the chain would make higher profits by *decreasing* the price of a half-gallon of orange juice from its current $3.00 to $2.33** — i.e. the current price is above the profit-maximizing point on an elastic demand curve, so cutting price more than pays for itself in extra volume.

**Why this belongs at the end of the curved-patterns chapter:** it's the business payoff of everything above — you can't compute an elasticity (and therefore can't solve for an optimal price) without first recognizing that price/quantity relationships are curved, fitting the right transformation (log-log), and checking that the transformed residuals behave.

---

## 4. Cross-cutting themes (Chapters 19 & 20 together)
1. **A regression line is only as good as the shape you check it against.** Chapter 19's entire back half (residuals, r², Anscombe's Quartet, the "Same Stats, Different Graphs" collection) exists to prevent you from trusting a fitted line — or a single summary number like r² — without looking at the scatterplot and the residual plot first.
2. **Curvature shows up in the residual plot before it shows up anywhere else.** The MPG/Weight example (§3.2) and the pet-food Sales/Price example (§3.6) both follow the identical diagnostic sequence: fit linear → residuals form a bowl/curve → transform → residuals randomize → r² improves. This is the operational version of Ch. 19's checklist item "is the residual variation random?"
3. **Two transformations cover most business curvature:** reciprocal (for anything that's naturally a ratio: MPG, equity/debt, sales/employee) and logarithm (for anything where percentage changes matter more than level changes: prices, wages, profits). The "bulging rule" circle is a fast way to pick between them from the scatterplot's shape alone.
4. **Log-log slopes are elasticities, and elasticities are directly actionable** — the chapter closes by turning a statistical tool (a regression coefficient) into a pricing decision (Optimal Price = Cost×γ/(1+γ)), which is exactly the calculation worked through for the Ridgeline Jacket case (see companion "Case Studies - In-Depth Notes.md").
5. **Correlation/r² ≠ causation, in both directions** — a high r² (Nicolas Cage movies & drownings) can be pure coincidence, and a low r² (smoking & life expectancy) can still reflect a real, important causal effect. Don't let a regression's explanatory power stand in for a judgment about mechanism.

---

## Gulsher questions (along with clarification)

*(none yet — add here when you have follow-up questions on this chapter)*
