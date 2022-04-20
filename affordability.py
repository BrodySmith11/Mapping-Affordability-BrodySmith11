# -*- coding: utf-8 -*-
"""
Created on Wed Apr 20 08:06:43 2022

@author: bsmith
"""

import pandas as pd

income = int(input('Enter Yearly Income:'))
print(income)
monthly_income = income/12
print(monthly_income)
monthly_minus_taxes = monthly_income * .73
