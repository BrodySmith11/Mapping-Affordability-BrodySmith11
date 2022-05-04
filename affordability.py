# -*- coding: utf-8 -*-
"""
Created on Wed Apr 20 08:06:43 2022

@author: bsmith
"""

import pandas as pd


data = pd.read_csv('City-Affordability-Data.csv')

income = int(input('Enter Post-Tax Yearly Income:\n$'))
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
extreme_cost_lower = monthly_income * .40
extreme_cost_upper = monthly_income

def assign_category(price_string):
    price = float(price_string)
    if price >= low_cost_lower and price < low_cost_upper:
        return 'low'
    elif price >= med_cost_lower and price < med_cost_upper:
        return 'medium'
    else:
        return 'high'
    
data['Category'] = data['1B Price Cleaned'].apply(assign_category)
print(data)


