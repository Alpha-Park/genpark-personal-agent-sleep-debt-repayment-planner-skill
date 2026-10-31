# -*- coding: utf-8 -*-
"""
Personal Agent Sleep Debt Repayment Planner FastMCP Server
"""

import json
from typing import Dict, List, Any, Optional
from mcp.server.fastmcp import FastMCP
from client import PersonalAgentSleepDebtRepaymentPlanner

mcp = FastMCP("genpark-personal-agent-sleep-debt-repayment-planner-skill")
planner = PersonalAgentSleepDebtRepaymentPlanner()

@mcp.tool()
def calculate_cumulative_sleep_debt_and_impairment(
    sleep_history_hours_json: str,
    baseline_need_hours: float = 7.75
) -> str:
    """
    Quantifies cumulative sleep deficit and estimates cognitive impairment and BAC equivalence.
    """
    history = json.loads(sleep_history_hours_json)
    res = planner.calculate_cumulative_sleep_debt_and_impairment(history, baseline_need_hours)
    return json.dumps(res, indent=2)

@mcp.tool()
def generate_gradual_sleep_repayment_plan(
    cumulative_debt_hours: float,
    max_daily_extension_hours: float = 0.75
) -> str:
    """
    Generates multi-day sleep repayment schedule avoiding circadian disruption.
    """
    res = planner.generate_gradual_sleep_repayment_plan(cumulative_debt_hours, max_daily_extension_hours)
    return json.dumps(res, indent=2)

@mcp.tool()
def audit_weekend_oversleep_circadian_shift(
    weekday_avg_sleep_hours: float,
    weekend_sleep_hours: float
) -> str:
    """
    Audits weekend social jetlag phase delay caused by irregular oversleeping.
    """
    res = planner.audit_weekend_oversleep_circadian_shift(weekday_avg_sleep_hours, weekend_sleep_hours)
    return json.dumps(res, indent=2)

def main():
    print("Testing Sleep Debt Repayment Planner FastMCP Server:")
    print(calculate_cumulative_sleep_debt_and_impairment("[6.0, 6.5, 5.5, 7.0, 6.0]", 7.75))

if __name__ == "__main__":
    main()
