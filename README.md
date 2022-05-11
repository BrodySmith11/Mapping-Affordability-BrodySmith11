# Mapping Affordability BrodySmith11
 Final Project

# Final Project
# Mapping US Rental Affordability

## Summary

US rental prices have been increasing at a dramatic rate since the beginning of the pandemic. It may soon reach a tipping point, but in the meantime, people still need to find housing. This tool will take the user's post-tax yearly income and create a plot that maps US cities using the user's affordability ranges.

## Input Data

There are two input files: **rental_data_100_cities.csv**, data about rental costs in 100 US cities, and **uscities.csv** which contains location data about all us cities. Both files are included in the repository.

## Deliverables

The output will be two plots of the United States with 100 cities mapped by rental affordabililty, shown using gradient dots. The first plot represents current US rental data and is named **City-Rental-Growth-Map.png**. The second maps future growth, price expected in one year, and is named **City-Rental-Growth-Map.png**

## Instructions

### a. data_join.py

1. import pandas as pd

1. import rental data. Set 'raw' to the result of calling 'pd.read_csv' on 'rental_data_100_cities.csv' with dtype = str.

1. Filter out unneeded data. We only need the city name, 1B Price, and Year over year percent change

