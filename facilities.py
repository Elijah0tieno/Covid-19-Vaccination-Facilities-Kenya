import csv

import folium as folium
from folium.plugins import FastMarkerCluster
from opencage.geocoder import OpenCageGeocode
from typing_extensions import final

key = "25a85e34ca9d48f68cfd017eec357d12"
geocoder = OpenCageGeocode(key)

import pandas as pd
data = pd.read_csv('covax.csv')


# print(data.head(5))

# convert the health facility column name to list to easily loop through
# create empty lists to store latitudes and longitudes
# create a loop which gives latitudes and longitudes for all the facilities

addresses = data["Health Facility Name"].values.tolist()
key = "25a85e34ca9d48f68cfd017eec357d12"
geocoder = OpenCageGeocode(key)
latitudes = []
longitudes = []



for address in addresses:
    result = geocoder.geocode(address, no_annotations="1")

    if result and len(result):
        longitude = result[0]["geometry"]["lng"]
        latitude = result[0]["geometry"]["lat"]
    else:
        longitude = "N/A"
        latitude = "N/A"

    latitudes.append(latitude)
    longitudes.append(longitude)


data["latitudes"] = latitudes
data["longitudes"] = longitudes

data.to_csv("locations.csv", index=False)
print(data.head(10))


