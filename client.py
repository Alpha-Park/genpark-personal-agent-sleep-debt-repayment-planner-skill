# -*- coding: utf-8 -*-
"""
Personal Agent Sleep Debt Repayment Planner Client
Zero-dependency cumulative sleep deficit modeler, Van Dongen PVT cognitive
impairment estimator, and circadian-safe sleep repayment scheduler.
"""

import math
from typing import Dict, List, Any, Optional

class PersonalAgentSleepDebtRepaymentPlanner:
    """
    Quantifies homeostatic sleep debt accumulation, models blood-alcohol-equivalent
    cognitive impairment, and schedules gradual, circadian-safe repayment trajectories.
    """

    def calculate_cumulative_sleep_debt_and_impairment(
        self,
        sleep_history_hours: List[float],
        baseline_need_hours: float = 7.75
    ) -> Dict[str, Any]:
        """
        Calculates 14-day cumulative sleep deficit: Debt = sum(max(0, Need - Sleep_i)).
        Van Dongen PVT Lapse Equivalent = 2.4 + 1.15 * Debt.
        BAC Equivalent = min(0.12, 0.015 * Debt).
        """
        if not sleep_history_hours:
            raise ValueError("Sleep history list cannot be empty.")

        need = max(6.0, min(10.0, float(baseline_need_hours)))
        cumulative_debt = 0.0

        for s in sleep_history_hours:
            actual = max(0.0, float(s))
            deficit = max(0.0, need - actual)
            cumulative_debt += deficit

        cumulative_debt = round(cumulative_debt, 2)

        # Cognitive impairment metrics
        pvt_lapses = round(2.4 + 1.15 * cumulative_debt, 1)
        bac_equiv = round(min(0.12, 0.015 * cumulative_debt), 3)

        if cumulative_debt >= 10.0:
            status = "ACUTE_CHRONIC_SLEEP_RESTRICTION (Equivalent to legal intoxication)"
        elif cumulative_debt >= 5.0:
            status = "MODERATE_COGNITIVE_DEFICIT (Slowed reaction time & executive fatigue)"
        elif cumulative_debt >= 2.0:
            status = "MILD_SLEEP_DEBT"
        else:
            status = "OPTIMALLY_RESTED"

        return {
            "days_analyzed": len(sleep_history_hours),
            "baseline_sleep_need_hours": need,
            "cumulative_sleep_debt_hours": cumulative_debt,
            "estimated_pvt_attention_lapses": pvt_lapses,
            "blood_alcohol_cognitive_equivalence": f"{bac_equiv:.3f}% BAC",
            "impairment_status": status,
            "reaction_time_slowdown_pct": round(min(60.0, cumulative_debt * 4.5), 1)
        }

    def generate_gradual_sleep_repayment_plan(
        self,
        cumulative_debt_hours: float,
        max_daily_extension_hours: float = 0.75
    ) -> Dict[str, Any]:
        """
        Schedules gradual repayment (30-45 mins extra per night) to clear debt without phase-delaying circadian clock.
        """
        debt = max(0.0, float(cumulative_debt_hours))
        daily_ext = max(0.25, min(1.5, float(max_daily_extension_hours)))

        if debt <= 0.5:
            return {
                "cumulative_debt_hours": debt,
                "repayment_days_needed": 0,
                "schedule": [],
                "status": "NO_REPAYMENT_NEEDED"
            }

        days_needed = math.ceil(debt / daily_ext)
        plan = []
        remaining = debt

        for d in range(1, days_needed + 1):
            applied = round(min(remaining, daily_ext), 2)
            remaining = round(max(0.0, remaining - applied), 2)
            plan.append({
                "day_number": d,
                "recommended_extra_sleep_minutes": int(applied * 60),
                "remaining_debt_hours": remaining,
                "bedtime_shift": f"Go to bed {int(applied * 60)} minutes earlier"
            })

        return {
            "cumulative_debt_hours": debt,
            "repayment_days_needed": days_needed,
            "daily_extension_minutes": int(daily_ext * 60),
            "repayment_schedule": plan,
            "circadian_safety_rule": "Apply extra sleep via earlier bedtime; do NOT sleep in past 45 mins beyond normal wake time."
        }

    def audit_weekend_oversleep_circadian_shift(
        self,
        weekday_avg_sleep_hours: float,
        weekend_sleep_hours: float
    ) -> Dict[str, Any]:
        """
        Detects 'social jetlag' phase delay caused by massive weekend oversleeping (>2 hours).
        Phase delay = (Weekend_Wake - Weekday_Wake) * 0.45 hours.
        """
        diff = max(0.0, float(weekend_sleep_hours) - float(weekday_avg_sleep_hours))
        phase_shift_h = round(diff * 0.45, 1)

        if diff >= 2.0:
            verdict = "SEVERE_SOCIAL_JETLAG (Sunday night insomnia risk high)"
        elif diff >= 1.0:
            verdict = "MODERATE_WEEKEND_SHIFT"
        else:
            verdict = "HEALTHY_CIRCADIAN_REGULARITY"

        return {
            "weekday_avg_sleep_hours": weekday_avg_sleep_hours,
            "weekend_sleep_hours": weekend_sleep_hours,
            "sleep_duration_delta_hours": round(diff, 1),
            "estimated_circadian_phase_delay_hours": phase_shift_h,
            "social_jetlag_risk": verdict,
            "recommendation": "Limit weekend sleep-in to 45 mins; take a 90-min afternoon nap instead to repay debt safely." if diff >= 1.5 else "Maintains healthy rhythm."
        }
