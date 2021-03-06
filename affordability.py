# -*- coding: utf-8 -*-
"""
Created on Wed Apr 20 08:06:43 2022

@author: bsmith
"""

import pandas as pd
import geopandas as gpd
import matplotlib.pyplot as plt


data = pd.read_csv('City-Affordability-Data.csv')
states = gpd.read_file('cb_2021_us_state_5m.shp')


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
    elif price >= high_cost_lower and price < high_cost_upper:
        return 'high'
    elif price >= extreme_cost_lower and price < extreme_cost_upper:
        return 'extreme'
        
    
data['Category'] = data['1B Price Cleaned'].apply(assign_category)


data_gdf = gpd.GeoDataFrame(data, geometry = gpd.points_from_xy(data['lng'],data['lat']))

#us_boundary_map = states.boundary.plot(figsize = (10,10), color="Gray")
#data_gdf.plot(ax=us_boundary_map, color='DarkGray')

fig, ax = plt.subplots(figsize = (10,6))
ax.set_xlim(-130,-60)
ax.set_ylim(20,50)
us_boundary_map = states.boundary.plot(figsize = (10,10), color="Gray", ax=ax)
data_gdf.plot('Category', ax=us_boundary_map, cmap='autumn')
fig.savefig("City-Rental-Affordability-Map.png")

fig2, ax = plt.subplots(figsize = (10,6))
ax.set_xlim(-130,-60)
ax.set_ylim(20,50)
us_boundary_map = states.boundary.plot(figsize = (10,10), color="Gray", ax=ax)
data_gdf.plot('1B Y/Y%', ax=us_boundary_map, cmap='autumn')
fig2.savefig("City-Rental-Growth-Map.png")



