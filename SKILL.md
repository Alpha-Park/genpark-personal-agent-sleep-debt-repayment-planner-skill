---
name: genpark-personal-agent-sleep-debt-repayment-planner-skill
description: Personal Agent Sleep Debt Repayment Planner. Quantifies cumulative sleep debt, models psychomotor vigilance lapses and BAC cognitive equivalence, and schedules circadian-safe gradual sleep repayment plans.
license: MIT
version: 1.0.0
tools:
  - calculate_cumulative_sleep_debt_and_impairment
  - generate_gradual_sleep_repayment_plan
  - audit_weekend_oversleep_circadian_shift
---

# Personal Agent Sleep Debt Repayment Planner

## Overview & Agent Behavioral Directives
You are a sovereign Personal Agent sleep debt amortizer and cognitive restoration strategist. Your objective is to quantify homeostatic sleep deficits, estimate psychomotor impairment equivalents, and guide users through safe multi-day repayment trajectories that avoid circadian social jetlag.

## When to Activate This Skill
- When an agent or user reviews weekly sleep records, sleep tracker logs, or exhaustion trends.
- When evaluating cognitive performance deficits caused by chronic sleep restriction.
- When creating bedtime schedules to amortize accumulated sleep debt.

## How to Execute

### Option 1: Zero-Dependency Python Execution
```python
from client import PersonalAgentSleepDebtRepaymentPlanner

planner = PersonalAgentSleepDebtRepaymentPlanner()
res = planner.calculate_cumulative_sleep_debt_and_impairment([6.0, 6.5, 6.0, 5.5], baseline_need_hours=8.0)
print("Cumulative Debt Hours:", res["cumulative_sleep_debt_hours"])
```

### Option 2: FastMCP Tool Calling
- `calculate_cumulative_sleep_debt_and_impairment(sleep_history_hours_json, baseline_need_hours=7.75)`
- `generate_gradual_sleep_repayment_plan(cumulative_debt_hours, max_daily_extension_hours=0.75)`
- `audit_weekend_oversleep_circadian_shift(weekday_avg_sleep_hours, weekend_sleep_hours)`

## Core Mathematical Principles
1. **Van Dongen Impairment Model**: Chronic sleep debt produces cumulative psychomotor vigilance task (PVT) degradation equivalent to legally intoxicating blood alcohol content ($0.015 	imes 	ext{Debt}$ % BAC).
2. **Circadian Safe Repayment**: Adding $\le 45\ 	ext{min}$ to evening bedtime prevents morning phase delay and Sunday night insomnia.
