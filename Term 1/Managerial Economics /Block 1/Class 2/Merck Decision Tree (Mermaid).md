# Launch Now or Wait? — Merck Version A vs Version B

Solid/thick arrows = the EV-optimal branch at each decision. Dotted arrows = the dominated alternative. Diamonds = calls Merck makes; circles = outcomes nature resolves; rectangles = terminal payoffs ($/dose).

```mermaid
flowchart LR
  ROOT{{"Launch now,<br/>or wait?"}}
  LAUNCH["Launch Version A now<br/><b>$2.85</b><br/><i>certain · dominated</i>"]
  WAITN(("Does B succeed?<br/>EV $3.27"))
  SUCC(("B succeeds<br/>EV $3.44"))
  FAIL(("B fails, refine A<br/>EV $3.10"))
  HIGH["B: high efficacy<br/><b>$5.60</b>"]
  MED{{"Mediocre B:<br/>sell or license?"}}
  SELL["Sell in-house<br/><b>$2.00</b><br/>chosen"]
  LIC["License to generic<br/><b>$1.00</b><br/>protects reputation"]
  WEAK["A improved: weak rivals<br/><b>$3.50</b>"]
  STRONG["A improved: strong rivals<br/><b>$3.00</b>"]
  GOOD["A improved: fair efficacy<br/><b>$2.50</b>"]

  ROOT -.->|launch now| LAUNCH
  ROOT ==>|wait 3 mo.| WAITN
  WAITN -->|p 0.50| SUCC
  WAITN -->|p 0.50| FAIL
  SUCC -->|p 0.40| HIGH
  SUCC -->|p 0.60| MED
  MED ==>|sell| SELL
  MED -.->|license| LIC
  FAIL -->|p 0.40| WEAK
  FAIL -->|p 0.40| STRONG
  FAIL -->|p 0.20| GOOD

  classDef decision fill:#f1e2c4,stroke:#9c6f2b,color:#16211c,stroke-width:1.5px;
  classDef chance fill:#ffffff,stroke:#16211c,color:#16211c,stroke-width:1.5px;
  classDef win fill:#dcece5,stroke:#1f6f5c,color:#144b3f,stroke-width:2.5px;
  classDef lose fill:#ffffff,stroke:#93a396,color:#55645a,stroke-width:1.5px,stroke-dasharray: 4 3;
  classDef neutral fill:#ffffff,stroke:#c4cdc1,color:#16211c,stroke-width:1.5px;

  class ROOT,MED decision
  class WAITN,SUCC,FAIL chance
  class SELL win
  class LAUNCH,LIC lose
  class HIGH,WEAK,STRONG,GOOD neutral
```

**Recommendation:** wait for Version B — EV $3.27/dose vs. $2.85 for launching now, a $0.42 (~15%) edge, after choosing to sell any mediocre B in-house rather than license it.
