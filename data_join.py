# -*- coding: utf-8 -*-
"""
Created on Wed Apr 20 05:56:16 2022

@author: bsmith
"""

# input needed modules
import pandas as pd

# import rental data
raw = pd.read_csv('rental_data_100_cities.csv',dtype=str)
print(raw)

# filter data to only needed data
### needed data includes 
### city name, 1 bedroom price and 1 bedroom change Y/Y and M/M

rentals_trimmed = raw.drop(columns='2B Price')
rentals_trimmed = rentals_trimmed.drop(columns='2B M/M%')
rentals_trimmed = rentals_trimmed.drop(columns='2B Y/Y%')
print(rentals_trimmed)

# add location data to cities
uscities = pd.read_csv('uscities.csv',dtype=str)
uscities.drop(['timezone','ranking','zips','id','source','military','incorporated',
                  'population','density','city_ascii','state_id',
                  'state_id','state_name','county_fips','county_name'], axis=1, inplace=True)

merged_left= pd.merge(left=rentals_trimmed,right=uscities,how='left', left_on='City', right_on='city')
print(merged_left)
