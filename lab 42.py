#victoria dynak
#victoria.dynak61@login.cuny.edu
#november 6 2022
#map of hospitals

import folium
import pandas as pd

hospitals = pd.read_csv("nyc_hospitals.csv")
hospitals.fillna({'Latitude':0, "Longitude":0}, inplace = True)
hospitalsmap = folium.Map(location = [40.75, -74.125], zoom_start = 10)

for index,row in hospitals.iterrows():
    lat = row["Latitude"]
    lon = row["Longitude"]
    name = row["Facility Name"]
    newMarker = folium.Marker([lat,lon],popup=name)
    newMarker.add_to(hospitalsmap)

out = input("Enter output file: ")
hospitalsmap.save(outfile=out)
                         
