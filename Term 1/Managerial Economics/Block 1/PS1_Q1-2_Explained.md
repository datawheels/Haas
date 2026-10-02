# Problem Set #1 — Questions 1 & 2, Explained

XMBA201A, Prof. Steve Tadelis

---

## Question 1: Renting Cloud Storage Capacity

### Setup

- Capacity is sold in units of 10M users.
- Demand: **High** = 20M users (prob = 2/3, needs 2 units) | **Low** = 10M users (prob = 1/3, needs 1 unit).
- Revenue = $1 x min(demand, capacity you bought). Unserved users are simply lost — no penalty.
- **Nile's pricing:**
  - *Advance commitment*: $4M/unit, must buy **before** demand is known, non-refundable if unused.
  - *On-demand*: $5.5M/unit, bought **after** demand is known (no waste risk, but pricier).

This is an "insure now vs. pay a premium to stay flexible" tradeoff.

### a) The decision tree

```
Decision: how many ADVANCE units? (0, 1, or 2)
        |
        +-- 0 advance --+-- Demand High (2/3) --> decide on-demand units to buy
        |                +-- Demand Low  (1/3) --> decide on-demand units to buy
        |
        +-- 1 advance --+-- Demand High (2/3) --> top up with on-demand?
        |                +-- Demand Low  (1/3) --> already covered, no need to buy more
        |
        +-- 2 advance --+-- Demand High (2/3) --> fully covered
                         +-- Demand Low  (1/3) --> 1 unit wasted (sunk, no refund)
```

Solve by folding back from the right: at each demand node, pick the best on-demand top-up, then average those payoffs (weighted 2/3, 1/3) to compare the three upfront choices.

**Strategy: 2 advance units** (cost $8M upfront)
- High: $20M revenue - $8M = **$12M**
- Low: $10M revenue (1 unit wasted) - $8M = **$2M**
- EV = (2/3)(12) + (1/3)(2) = **$8.67M**

**Strategy: 1 advance unit** (cost $4M, top up on-demand only if High)
- Low: exactly covered -> $10M - $4M = **$6M**
- High: buy 1 more on-demand ($5.5M) -> $20M - $4M - $5.5M = **$10.5M**
- EV = (2/3)(10.5) + (1/3)(6) = **$9.0M**

**Strategy: 0 advance units** (buy everything on-demand after learning demand)
- Low: buy 1 on-demand -> $10M - $5.5M = **$4.5M**
- High: buy 2 on-demand -> $20M - $11M = **$9M**
- EV = (2/3)(9) + (1/3)(4.5) = **$7.5M**

**-> Best: lock in 1 advance unit, top up on-demand only if High.** Expected profit ~ **$9.0M**.

(Note: "0 advance" is always worse than "1 advance" — that first unit gets used in *both* demand states, so you should never pay the $5.5M on-demand premium for it.)

### b) Where does the decision flip, as a function of P = probability of High demand?

Redo the EVs generally:

- 2 advance: EV = 12P + 2(1-P) = **2 + 10P**
- 1 advance: EV = 10.5P + 6(1-P) = **6 + 4.5P**
- 0 advance: EV = 9P + 4.5(1-P) = **4.5 + 4.5P** (always $1.5M below "1 advance" — never optimal)

Set the two live candidates equal:

2 + 10P = 6 + 4.5P
5.5P = 4
**P* = 4 / 5.5 = 8/11 ~ 0.727**

- If P < 8/11: buy **1 advance**, top up on-demand if High. (True at P = 2/3 ~ 0.667.)
- If P > 8/11: buy **2 advance** upfront — high demand is likely enough that locking in full capacity outweighs the risk of wasting a unit.

### c) Adding Volga

Volga: always $4.5M/unit, always available immediately, no advance/on-demand split. Since waiting costs nothing, optimal play is: wait, learn demand, buy exactly what's needed.

- Low: 1 unit -> $10M - $4.5M = **$5.5M**
- High: 2 units -> $20M - $9M = **$11M**
- EV = (2/3)(11) + (1/3)(5.5) = **$9.17M**

Compare to Nile's best ($9.0M at P = 2/3): **Volga wins**, narrowly — pick Volga.

---

## Question 2: Research Project (AK Steel)

### Setup

- 3 sequential steps; you learn if step n succeeded before funding step n+1.
- Each step: cost $500K, success probability 0.8 (independent).
- Payoff: $4M **only if all 3 succeed**. Any failure -> project worthless, money spent so far is sunk.
- Risk neutral, interest rate 0.

### a) The tree

```
[] Invest Step 1? ($500K)
   |
   +-- No --------------------------------> $0
   |
   +-- Yes (-$500K)
         |
         v
       () Step 1 outcome
         |
         +-- Fail (0.2) ---------------------> $0  (-$500K sunk)
         |
         +-- Success (0.8)
               |
               v
             [] Invest Step 2? ($500K)
               |
               +-- No ------------------------> $0
               |
               +-- Yes (-$500K)
                     |
                     v
                   () Step 2 outcome
                     |
                     +-- Fail (0.2) -----------> $0
                     |
                     +-- Success (0.8)
                           |
                           v
                         [] Invest Step 3? ($500K)
                           |
                           +-- No --------------> $0
                           |
                           +-- Yes (-$500K)
                                 |
                                 v
                               () Step 3 outcome
                                 |
                                 +-- Fail (0.2) --> $0
                                 |
                                 +-- Success (0.8) -> $4,000,000
```

[] = decision node   () = chance node

### b) Probability of full success

0.8^3 = **0.512** (51.2%) — independent successes multiply.

### c) Expected gain if research were costless

**Think of it like a lottery ticket** that pays $4M with 51.2% probability (from part b) and $0 otherwise. Its expected value is just the probability-weighted average:

0.512 x $4,000,000 + 0.488 x $0 = **$2,048,000**

This ignores the real $500K/step costs on purpose — it isolates "how good is the prize" from "how expensive is getting there." Part (d) brings the costs back.

### d) Should the firm begin, given $500K/step?

Solve backward from step 3 (this is the key technique — called "backward induction" or "rolling back the tree"):

**At step 3** (only reached if steps 1 & 2 already succeeded):

V3 = -500K + 0.8($4M) + 0.2($0) = -500K + $3.2M = **$2.70M**

Positive -> always invest in step 3 if you get there.

**At step 2** (continuing is worth V3 if step 2 succeeds, $0 if it fails):

V2 = -500K + 0.8(V3) + 0.2($0) = -500K + 0.8($2.70M) = **$1.66M**

Positive -> always invest in step 2 if you get there.

**At step 1:**

V1 = -500K + 0.8(V2) + 0.2($0) = -500K + 0.8($1.66M) = **$828,000**

**-> Yes, begin the research.** Expected NPV = **$828,000**.

### e) Quit after a success? Continue after a failure?

Pattern: V1 ($828K) < V2 ($1.66M) < V3 ($2.70M) — the value of continuing only *grows* as you get closer to the finish line (fewer steps left standing between you and the $4M).

- **Never quit voluntarily after a success** — continuing is always positive EV, increasingly so.
- **Never continue after a failure** — a failure makes the project worthless outright (no retries), so spending more buys a 0% chance of anything.

### f) The tree after steps 1 & 2 succeed, with the alternate process

Steps 1 & 2 are now sunk — ignore them. New decision: fund step 3 ($500K, 0.8 -> $4M) and/or fund the alternate process ($150K, guaranteed $1M), decided together **before** step 3's outcome is known. They're substitutes — if both pay off, you use the better one ($4M > $1M).

| Strategy | Cost | If Step 3 succeeds (0.8) | If Step 3 fails (0.2) | EV |
|---|---|---|---|---|
| Step 3 only | $500K | use $4M -> net $3.5M | net -$0.5M | **$2.70M** |
| Alternate only | $150K | net $850K (certain either way) | net $850K | **$0.85M** |
| Both | $650K | use $4M -> net $3.35M | use $1M -> net $0.35M | **$2.75M** |

### g) Chance alternate delivers value, given firm continues step 3

Alternate only matters when step 3 **fails** (if step 3 succeeds, $4M beats $1M, so alternate goes unused). That's the 0.2 failure probability -> **20%**.

### h) Expected value of having alternate available, if costless

0.2 x $1,000,000 + 0.8 x $0 = **$200,000**

(No added value when step 3 succeeds — $4M already beats it.)

### i) Step 3 alone, alternate alone, or both?

**-> Pursue both** (from the table in part f: $2.75M > $2.70M > $0.85M).

The alternate is cheap insurance: costs $150K, but only pays off in the 20%-probability failure branch, where it turns a $500K loss into a $850K gain. Marginal value of adding it = -$150K + 0.2($1M) = **$50K** — exactly the gap between $2.75M and $2.70M.

### j) If the firm had known about the alternate from the very start

Doesn't change *whether* to do steps 1-3 (still worth it), but it raises the payoff at the end of the chain, which ripples backward through the tree. Redo the rollback using V3' = $2.75M (step 3 + alternate option) instead of $2.70M:

V2' = -500K + 0.8($2.75M) = **$1.70M**
V1' = -500K + 0.8($1.70M) = **$860,000**

**-> Same qualitative decision** (begin research, continue after every success, pursue the alternate too once you reach that point) — but the venture is worth **$860K, not $828K**. The $32K difference = 0.8 x 0.8 x $50K — the $50K bonus from part (i), discounted by the probability (0.64) of actually reaching that decision point.
