# Mapping Affordability BrodySmith11
 Final Project

# Final Project
# Mapping US Rental Affordability

## Purpose

My classmates and I are going to graduate soon, which means careers are on the horizon. I was able to secure a position in Flagstaff Arizona but will not be able to accept due to unrealistic housing costs in the area. Housing prices are on the rise everywhere, so to assist my classmates and myself I sought to create a tool that would map rental affordability by city in the US. 

## Data Procurement

The rental data is collected from the Zumper National Rent Report 2022. It is a list of 100 US cities with data about each cities average monthly rent (1 bedroom), year over year change, month over month change, etc. This file is should be saved as 'rental_data_100_cities.csv'
The rental data does not include location data other than city name, so we need a data set that includes both city name and latitude/longitude to join onto. This can be collected at https://simplemaps.com/data/us-cities where a free csv can be downloaded. This should be saved as uscities.csv
The final file is a shapefile of the US state boundaries. It si downloaded from the US census website.

## Script Explanation
the 'data_join.py' script is a script that joins the latitude and longitude from the 'uscities.csv'. It first cleans the unneeded columns out of the files. It then merged the cleaned files together on the city names, making one file that contains both city rental data and the latitude/longitude to match.

The 'affordability.py' script takes a user input of their yearly post tax income. The script will then break that income into 12 (for months of rent), then create affordability ranges for that user as a percentage of their monthly income. The ranges are low (0-25%), meduium (25-33%), High (33-40%), Extreme (40%+). The cities within the cities list are then assigned one of these categories.

Using a plot, a us state boundary map is created. using this shapefile as a base, the city data is mapped onto the plot using the lat long data. The data that was categorized is matched to the lat long data, and using those categories the city markers are color graduated to show rental affordability. 

The scripts should be run in following order.
 1. data_join.py
 1. affordability.py

 ## additional files

 There are additional files attached to the shapefile of the us boundary.

 ## Results
 There aren't 'results' from this tool, other than showing that many US cities are out of the price range for average income out of grad school. The finished deliverable is a plot/map .png showing a personalized affordability map based on the input income data.