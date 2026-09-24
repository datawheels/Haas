# Class 9 Case Study — In-Depth Notes (Financial Statement Analysis: Valuing Apple)

Source: `Apple valuation - November 2025.xlsx`. Per class.md: *"We will examine the financial statements of several companies and discuss their performance and implications for stock prices — no slides for this class."* This spreadsheet **is** the class material — a full DCF valuation model built on Apple's 20-year (FY2006–FY2025) financial statements, used to tie together every Block 1–4 topic (income statement, balance sheet, ratios, cash flow, cost of capital) into one live valuation exercise. No separate "Theory Notes" exists for this class since there's no lecture deck — these notes work through the model directly.

---

## 1. What this model is actually doing

This is a standard three-statement **DCF (discounted cash flow) valuation**: forecast Apple's income statement and balance sheet forward 7 years (FY2026–FY2032), derive unlevered free cash flow each year, discount it back at the cost of capital (WACC), add a terminal value, and back out an implied share price — then compare that to where the stock actually trades. The workbook has 22 tabs; the ones that matter for understanding the mechanics are: **cost of capital**, **Valuation - base** (the completed model), **Valuation - new product** / **Valuation - lower margins** (sensitivity scenarios), and the historical ratio tabs (**Profitability, Liquidity, Leverage, Efficiency ratios**) that ground the forecast assumptions in 20 years of actual Apple filings.

## 2. Cost of capital (WACC) — built bottom-up via CAPM

| Input | Value | Source note |
|---|---|---|
| Cost of debt | 3.0% | "From Apple 10-K (approximate)" |
| Tax rate | 21% | "Interest payments are in the US" |
| 10Y UST (risk-free rate) | 2.5% | "Estimate — long-term" |
| Market risk premium | 6.0% | "Estimate — long-term" |
| Beta (Apple) | 1.1 | Yahoo Finance |
| Permanent debt weight | 15% | Estimate — target capital structure, *not* today's actual (gross) debt weight, which is only 2.4% given Apple's ~$4T market cap |

**Cost of equity (CAPM):** `r_e = r_f + β × MRP = 2.5% + 1.1 × 6.0% = 9.1%`

**After-tax cost of debt:** `r_d × (1 − tax) = 3.0% × (1 − 0.21) = 2.37%`

**WACC:** `WACC = (E/V) × r_e + (D/V) × r_d(1−t) = 0.85 × 9.1% + 0.15 × 2.37% ≈ 8.09%`

**The key judgment call here:** the model deliberately does *not* use Apple's actual current gross-debt weight (2.4% — trivial, because Apple's equity market cap dwarfs its ~$100B gross debt). Instead it assumes a **15% "permanent" target debt weight**, on the theory that a company's WACC should reflect the capital structure it intends to run *going forward*, not a snapshot dominated by however inflated or deflated the stock price happens to be today. This is a recurring theme across corporate finance: use a *target/normalized* structure for WACC, not today's market-value noise.

## 3. Forecast assumptions — the base case (`Valuation - base` tab)

Starting from FY2025 actuals (Net sales $416.16B, Cost of sales 53.1% of sales, Net income $112.0B):

- **Sales growth** decelerates from 17.1% (2025 actual) → 12.0% → 7.9% → 7% → 6% → 5% → 4% by 2032 — a classic "fade to terminal growth" pattern, since no company sustains double-digit growth forever at Apple's scale.
- **Cost of sales as % of sales improves** from 51% (2026) down to a stable 47% (2028 onward) — the model's note explains this as "going down slightly as a result of higher % of services as % of sales," i.e., Apple's high-margin Services segment (App Store, subscriptions) growing faster than lower-margin hardware, pulling the blended COGS ratio down. This single assumption is one of the biggest single drivers of the whole valuation — worth stress-testing (see the "lower margins" scenario below).
- **Working capital ratios held stable** (AR/sales, Inventory/COGS, AP/COGS, Accrued expenses/COGS all frozen at their 2025 actual levels) — a standard simplifying assumption: rather than modeling AR/AP dynamics from scratch, assume the relationships stay constant and let them scale with sales/COGS.
- **CapEx ramps up** from 3% of next year's sales (historical rate) to 7%, with the explicit note "potential data center needs" — a forward-looking judgment that Apple's capital intensity is about to rise (AI infrastructure), not stay at its historically capital-light hardware-company level.
- **Capital returns to shareholders:** dividends grow 5%/year; **share repurchases = 80% of net income** every year, *plus* additional lump-sum buybacks/dividends in 2026–2029 (funded by "using foreign cash," per the label) of $20B, $20B, $10B, $10B.
- **Terminal growth rate: 3.5%** — the perpetuity growth rate applied to 2032's free cash flow to get a terminal value, roughly in line with long-run nominal GDP growth (a standard sanity-check ceiling for any terminal growth assumption — a company can't outgrow the economy forever without eventually becoming the entire economy).

**Free cash flow build (unlevered FCF, i.e., FCF to the whole firm before financing):**
```
FCF = EBIT × (1 − tax rate) + Depreciation − CapEx − Increase in Net Working Capital
```
E.g. 2026: `132.77 (NOPAT) + 21.81 (D&A) − 27.26 (CapEx) − 10.19 (net WC increase, sum of the 5 WC line changes) ≈ $117.1B`, rising to **$214.0B by 2032** before the terminal value is added.

**Terminal value (2032):** $4,825.8B, calculated via the Gordon growth perpetuity `FCF₂₀₃₃ / (WACC − g) = FCF₂₀₃₂×1.035 / (0.0809 − 0.035)`. This single number dominates the valuation — it's roughly **95% of the $5,039.9B "Total FCF" figure in the terminal year**, which is completely typical for DCF models (and a standard criticism of DCF: most of the value comes from an assumption about growth *decades* out, not from anything observable today).

**Bridging enterprise value to equity value to share price:**
```
PV of all FCF (2026–2032, including terminal value), discounted at WACC = $3,689.3B
+ Cash and marketable securities on hand                                = $132.4B
− Total debt                                                             = ($98.7B)
= Apple equity (market) value                                           = $3,723.0B
÷ Shares outstanding (14.8B)                                             
= Implied share price                                                    = $251.55
```

## 4. Scenario analysis — the three cases (`Valuation summary` tab)

| Scenario | Implied share price | What's different |
|---|---|---|
| **Base** | **$251.55** | As above |
| **Lower growth, higher costs** | **$154.34** | Sales growth fades faster (10%→3% by 2032 vs. base's 12%→4%); Cost of sales *rises* to 60% by 2029 (vs. base's stable 47%) — narrative: "Price pressure, less services, more regulation, geopolitical [risk]," i.e., tariffs/regulation squeeze margins and Apple can't keep pivoting to high-margin services |
| **Higher growth, higher profit** | **$330.15** | Sales growth *accelerates* to 20% in 2028 before fading to 4%; Cost of sales *falls* to 45% by 2029 — narrative: "New and more services — healthcare, iCloud for business, games, original content revenue" |

**The single most important number in this whole exercise:** moving Cost of sales from 47% (base) to 60% (bear case) — just a 13-point swing in one assumption — cuts the implied share price by **39%** ($251.55 → $154.34), while a comparably-sized *favorable* swing in growth + margins only lifts it by 31% ($251.55 → $330.15). **This asymmetry is worth noticing**: the valuation is far more sensitive to the margin assumption than to the growth assumption, because margin changes flow straight through to every single year of FCF, compounding, whereas growth differences take years to widen the revenue base. The lesson generalizes well beyond Apple: in any DCF, always ask "which assumption is this number *most* sensitive to?" before trusting a single point estimate.

## 5. Grounding the forecast in 20 years of real Apple financials (the ratio tabs)

The `Profitability`, `Liquidity`, `Leverage`, and `Efficiency ratios` tabs pull Apple's actual FY2006–FY2025 income statement and balance sheet figures and compute the standard ratio toolkit from earlier in the course — this is where Blocks 1–3's topics (income statement, balance sheet, AR/inventory, liabilities/equity) get applied to a real company rather than the fictional Coffee Life:

- **DuPont ROE decomposition** (`ROE = Net margin × Asset turnover × Equity multiplier`): Apple's ROE has exploded from **28.5% (FY2007) to 171.4% (FY2025)** — an eye-popping number that is *not* driven by profitability improving 6x (net margin only moved from 14.6% to 26.9%) but almost entirely by the **equity multiplier rising from 1.7x to 5.5x**. That's the DuPont framework doing exactly its job: it decomposes what looks like an incredible ROE story into "actually, this is mostly a leverage/buyback story, not an operations story." Apple has been aggressively shrinking its equity book value via buybacks (equity book value peaked at $134B in FY2017 and is *down* to $73.7B in FY2025 despite the company being vastly more profitable) while assets stayed roughly flat — mechanically inflating ROE. **This is exactly the kind of ratio-reading skill Block 4's "team challenges" are testing**: a naive glance at "171% ROE!" without decomposing it would badly mislead you about *why* Apple is so profitable.
- **Liquidity ratios have deteriorated structurally**: current ratio fell from **2.25 (FY2006) to 0.89 (FY2025)** — now *below* 1.0, meaning current liabilities exceed current assets. For most companies this would be a red flag. For Apple it isn't, because of two things this course covered: (1) Apple's negative **working capital days** (−43 days in FY2025 — it collects from customers and gets paid *before* it has to pay its suppliers, a hallmark of immense supplier bargaining power) means it doesn't need a liquidity cushion the way a typical firm does, and (2) Apple sits on enormous marketable-securities and cash balances that aren't always classified as "current" but are trivially liquid. **This is the case-study lesson: ratio benchmarks ("current ratio should be >1") are industry/company-context-dependent, not universal rules.**
- **Leverage went from zero to modest and now back down**: Apple carried *no* debt at all through FY2012 (Debt/Assets = 0 every year C–I), began issuing debt from FY2013 onward specifically to fund buybacks/dividends without repatriating overseas cash at the old higher tax rate, peaked around Debt/Assets ≈ 35% (FY2021), and has been *de-levering* since (down to 27.5% by FY2025). Interest coverage (EBIT/interest) is enormous throughout (17x–360x) — even at its most leveraged, Apple was never at meaningful credit risk; the debt was a tax/capital-structure optimization, not a survival necessity.
- **Days AP (~115 days) vastly exceeds Days AR (~61 days) and Days Inventory (~10.5 days)** — Apple pays suppliers slower than it collects from customers or holds inventory, the working-capital engine behind the negative working-capital-days figure above.

## 6. Discussion takeaways for this class

1. **A DCF's output is only as good as its weakest input, and the model itself hands you the tool to find that input**: run the same model 3 times with different margin/growth assumptions and watch the price swing from $154 to $330 — a ~2.1x range — off a company most people would call "well understood." Before trusting *any* single-point valuation, ask what assumption it's most sensitive to (here: the COGS % assumption) and whether that assumption is well-founded.
2. **Historical ratios ground forward assumptions** — the "stable" working-capital ratios in the forecast aren't invented; they're set equal to FY2025's actual AR/sales, Inventory/COGS, etc. (from the `Efficiency ratios` tab), and the CapEx ramp is explicitly flagged as a *departure* from the historical 3% rate. Good forecasting is "historical baseline + explicitly justified deviations," not a blank-sheet guess.
3. **A ratio in isolation can mislead; decomposition (DuPont) or context (industry/company-specific working capital norms) is what makes it useful** — Apple's 171% ROE and sub-1.0 current ratio both look alarming out of context and both have benign, well-understood explanations once you decompose/contextualize them.
4. **WACC uses a *target* capital structure, not today's snapshot** — using Apple's actual (near-zero) debt weight because its market cap is so enormous would understate the "true" long-run WACC the company should be evaluated against.

---

## Gulsher questions (along with clarification)

*(none yet — add here when you have follow-up questions on this case)*
