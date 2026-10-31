# -*- coding: utf-8 -*-
import json
from client import PersonalAgentSleepDebtRepaymentPlanner

planner = PersonalAgentSleepDebtRepaymentPlanner()

print("=" * 64)
print("DEMO: Personal Sleep Debt & Circadian Repayment Planner")
print("=" * 64)

# 1. Calculate cumulative sleep debt
history = [6.0, 6.2, 5.8, 7.0, 6.5, 5.5, 6.0]
debt = planner.calculate_cumulative_sleep_debt_and_impairment(history, baseline_need_hours=7.75)
print(f"\n1. Sleep Debt Audit ({debt['days_analyzed']} Days Analyzed):")
print(f"   Cumulative Debt: {debt['cumulative_sleep_debt_hours']} hours")
print(f"   Cognitive BAC Equivalent: {debt['blood_alcohol_cognitive_equivalence']}")
print(f"   Status: {debt['impairment_status']} (Reaction Slowdown: {debt['reaction_time_slowdown_pct']}%)")

# 2. Gradual Repayment Schedule
plan = planner.generate_gradual_sleep_repayment_plan(debt["cumulative_sleep_debt_hours"], max_daily_extension_hours=0.75)
print(f"\n2. Gradual Repayment Plan ({plan['repayment_days_needed']} Days Needed):")
for day in plan["repayment_schedule"][:4]:
    print(f"   Day {day['day_number']}: +{day['recommended_extra_sleep_minutes']} min sleep -> {day['bedtime_shift']} (Remaining Debt: {day['remaining_debt_hours']}h)")

# 3. Weekend Social Jetlag Audit
jetlag = planner.audit_weekend_oversleep_circadian_shift(weekday_avg_sleep_hours=6.0, weekend_sleep_hours=9.5)
print(f"\n3. Weekend Social Jetlag Audit (+3.5h Delta):")
print(f"   Phase Delay: +{jetlag['estimated_circadian_phase_delay_hours']} hours ({jetlag['social_jetlag_risk']})")
print(f"   Guidance: {jetlag['recommendation']}")
