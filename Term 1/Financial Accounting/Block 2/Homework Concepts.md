# Homework Concepts

## Allowance for doubtful accounts — rollforward

The allowance for doubtful accounts (a contra-asset to AR) moves each period according to:

**Beginning allowance + Bad debt expense (provision) − Write-offs = Ending allowance**

- **Provision** (bad debt expense) is an estimate booked to the income statement; it builds up the allowance without reference to any specific customer.
- **Write-offs** remove a specific, now-confirmed-uncollectible receivable from both AR and the allowance (Dr. Allowance / Cr. AR). This does **not** hit the income statement again — the expense was already recognized via the provision.
- Because write-offs are usually not separately disclosed, they can often be backed into as the only unknown in the rollforward identity above, given beginning/ending allowance and the provision.

## CECL — forward-looking allowance estimates

Under the current expected credit loss (CECL) model, the allowance ratio (allowance ÷ gross or net receivables) is not just a trailing average of realized losses. It blends:
- **Historical loss experience** (what write-off rates have actually looked like), with
- **Forward-looking macroeconomic assumptions** (unemployment, rates, spending, sector-specific risk, etc.)

This is why an allowance ratio can stay flat or even rise even when realized write-offs are improving — management may be pricing in future risk that hasn't shown up in the loss data yet. Conversely, a short improving trend (e.g., only 1-2 years of data) is a weak basis for a large reserve cut, since it may not yet reflect a forward-looking risk picture.

## Working capital cycle — DSO, DIO, DPO, NWC

**Net Working Capital (NWC) = Accounts Receivable + Inventory − Accounts Payable**

The three "days" ratios measure how long cash is tied up (or deferred) in each leg of the operating cycle:

- **Days Sales Outstanding (DSO) = Average AR / Daily Sales** — how many days, on average, it takes to collect a sale after it's made.
- **Days Inventory Outstanding (DIO) = Average Inventory / Daily COGS** — how many days, on average, inventory sits before being sold (converted to COGS).
- **Days Payable Outstanding (DPO) = Average AP / Daily COGS** — how many days, on average, the company takes to pay its suppliers.

("Daily" = annual figure ÷ 365; equivalently, Average balance / Annual figure × 365 — same result, different order of operations.)

Intuition: lower DSO/DIO is more efficient (cash comes back faster / inventory moves faster), while *higher* DPO is more efficient from the company's perspective (it holds onto cash longer before paying suppliers). Together, DSO + DIO − DPO ≈ the cash conversion cycle.

If a problem says to treat the balance-sheet figure itself as the average (rather than averaging beginning/ending balances), that's a simplification to look out for — it changes what you plug into the "Average X" part of each formula.

## CapEx vs. OpEx, and depreciation

- **OpEx** (operating expense) hits the income statement immediately in the period incurred.
- **CapEx** (capital expenditure) is spent on a long-lived asset and is *not* expensed immediately. It's capitalized onto the balance sheet (as PP&E) and then expensed gradually over the asset's estimated useful life via **depreciation** (commonly straight-line: Cost ÷ Useful life = Annual depreciation expense).

The assumed useful life directly drives the annual depreciation expense for a given capex amount: a shorter assumed life spreads the same dollar amount over fewer years, producing a bigger annual expense (and bigger hit to reported profit) than a longer assumed life would, even though the total amount capitalized doesn't change.
