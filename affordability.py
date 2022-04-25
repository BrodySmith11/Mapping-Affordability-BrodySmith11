# -*- coding: utf-8 -*-
"""
Created on Wed Apr 20 08:06:43 2022

@author: bsmith
"""

import pandas as pd

income = int(input('Enter Post-Tax Yearly Income:\60n$'))
print(income)
monthly_income = income/12
print(monthly_income)

# Want to take monthly income and create ranges based off percentage of income to be spent on rent
# ranges are <25%, 25-33%, 33-40%, 40%<.
# names of Low Cost, Medium Cost, High Cost, Extreme.
low_cost_lower = 0
low_cost_upper = monthly_income * .25
med_cost_lower = monthly_income * .25
med_cost_upper = monthly_income * .33
high_cost_lower = monthly_income * .33
high_cost_upper = monthly_income * .40
extreme_lower = monthly_income * .40
extreme_upper = monthly_income

