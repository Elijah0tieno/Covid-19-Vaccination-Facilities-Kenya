import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import csv

import geopy
from geopy import location
from geopy.geocoders import Nominatim
from opencage.geocoder import OpenCageGeocode
key = "7b5bb52f9f6846078a6b91156242a48f"
geocoder = OpenCageGeocode(key)


covax = pd.read_csv('covax.csv', low_memory=False)
output = pd.read_csv('output.csv')
# REMOVE THE FIRST TWO COLUMNS AND REMAIN ONLY WITH THE HOSPITALS

cols_to_drop = [0,1]
cols_to_drop = sorted(cols_to_drop, reverse=True) #reverse so we remove end first
row_count = 0

with open('covax.csv', "r") as source:
    reader = csv.reader(source)
    with open('output.csv', "w", newline='') as result:
        writer = csv.writer(result)
        for row in reader:
            row_count += 1
            # print('\r{0}'.format(row_count), end='')
            for col_index in cols_to_drop:
                del row[col_index]
            writer.writerow(row)



# print(output.head())

geolocator = Nominatim(user_agent='locations.py')
# location = geolocator.geocode("Multimedia University of Kenya")
# print((location.latitude, location.longitude))

with open('output.csv') as csv_file:
    csv_reader = csv.reader(csv_file)
    rows = list(csv_reader)

    # location = geolocator.geocode("Kamwingi")
    # print((location.latitude, location.longitude))
    # print(rows[1])
    # print(rows[2])

latitude = []
longitude = []
location = []

for row in rows:
    place = geolocator.geocode(row)
    if not None:
        long = place.longitude
        lat = place.latitude

        latitude.append(lat)
        longitude.append(long)
        location.append(row)

df = pd.DataFrame()
df['location'] = location
df['longitude'] = longitude
df['latitude'] = latitude
df.to_csv('centers.csv', index=False)
