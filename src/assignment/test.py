import numpy as mp
import pandas as pd
from math import sin, cos, sqrt, atan2, radians


# Solution from: https://stackoverflow.com/questions/19412462/getting-distance-between-two-points-based-on-latitude-longitude
def calcKm(startLat, startLon, endLat, endLon):
    # approximate radius of earth in km
    R = 6373.0

    lat1 = radians(startLat)
    lon1 = radians(startLon)
    lat2 = radians(endLat)
    lon2 = radians(endLon)

    dlon = lon2 - lon1
    dlat = lat2 - lat1

    a = sin(dlat / 2) ** 2 + cos(lat1) * cos(lat2) * sin(dlon / 2) ** 2
    c = 2 * atan2(sqrt(a), sqrt(1 - a))

    return R * c

# Load the metro.csv file as DataFrame
x = pd.read_csv('../../resources/metro.csv')


# Print to console how many null values are detected.
print(x.isna().values.any())
print(x.isna().sum())

print("----------------------------------------")

# Count the null columns
nullColumns = x.columns[x.isnull().any()]
print(x.isnull().any())
print(x[nullColumns].isnull().sum())


print("----------------------------------------")
# Start lat and start lon
# end lat and end lon
# These are the values in the dataframe that are null
# Up to 1838 values that are null

print(x.start_lat.isna())

print("-------------------")

print("Entries with null start_lat")
print(x[x.start_lat.isna()])

print("----------------------------")

print(x.foot())


