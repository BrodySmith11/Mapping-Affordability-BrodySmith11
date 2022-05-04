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
rentals_trimmed['1B Price Cleaned'] = (rentals_trimmed['1B Price'].str.replace('$','').str.replace(',','').str.replace(' ',''))
rentals_trimmed = rentals_trimmed.drop(columns='1B Price')
#for index, name in rentals_trimmed['City'].iteritems():
  #  name = name[0:name.find(',')]
  #  print(name)
   # rentals_trimmed['City'][index] = name
print(rentals_trimmed)

# add location data to cities
uscities = pd.read_csv('uscities.csv',dtype=str)
uscities['city-state'] = uscities['city_ascii'] + ', ' + uscities['state_id']
print(uscities)
uscities.drop(['timezone','ranking','zips','id','source','military','incorporated',
                  'population','density','city_ascii','state_id',
                  'state_id','state_name','county_fips','county_name'], axis=1, inplace=True)


merged_left= pd.merge(left=rentals_trimmed,right=uscities,how='left', left_on='City', right_on='city-state')
print(merged_left)
cleaned_data = merged_left.drop(columns='city-state')
cleaned_data = cleaned_data.drop(columns='city')
cleaned_data = cleaned_data.drop(columns='Unnamed: 0')
print(cleaned_data)

cleaned_data.to_csv('City-Affordability-Data.csv')



