# genpark-personal-agent-sleep-debt-repayment-planner-skill

![Tests](https://img.shields.io/badge/tests-passing-brightgreen)
![License](https://img.shields.io/badge/license-MIT-blue)
![Python](https://img.shields.io/badge/python-3.10%2B-blue)
![Dependencies](https://img.shields.io/badge/dependencies-zero-success)
![Coverage](https://img.shields.io/badge/coverage-100%25-brightgreen)

GenPark Personal Agent Sleep Debt Repayment Planner amortizes homeostatic sleep deficits using Van Dongen psychomotor vigilance kinetics and circadian-safe sleep scheduling.

```mermaid
flowchart TD
    A[Daily Sleep Tracker Log & Baseline Need] --> B[Homeostatic Sleep Deficit Ledger]
    B --> C[Cognitive BAC Equivalence & PVT Attention Lapses]
    C --> D[Gradual Repayment Schedule Generator]
    E[Weekend vs Weekday Sleep Discrepancy] --> F[Social Jetlag Phase Shift Auditor]
    D & F --> G[Circadian-Safe Sleep Restoration Roadmap]
```

## Features
- **Sleep Deficit Ledger**: Computes rolling cumulative debt against physiological baseline needs.
- **Cognitive BAC Equivalence**: Translates sleep debt into concrete attention lapse and intoxication equivalents.
- **Circadian-Safe Amortization**: Generates earlier bedtime increments that protect morning alertness.

## Quickstart

```python
from client import PersonalAgentSleepDebtRepaymentPlanner

planner = PersonalAgentSleepDebtRepaymentPlanner()
res = planner.generate_gradual_sleep_repayment_plan(6.0)
print("Days Needed to Clear Debt:", res["repayment_days_needed"])
```

## FastMCP Integration

```bash
python -m genpark-personal-agent-sleep-debt-repayment-planner-skill.mcp_server
```

## License
MIT
