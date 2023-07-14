#victoria dynak
#victoria.dynak61@login.cuny.edu
#november 13 2022
#after school data

import folium
import pandas as pd

school = pd.read_csv("after_school.csv")
print("Enter 1 for Borough/Community,")
print("2 for Grade Level / Age Group")
user = input("Your choice: ")

schoolm = folium.Map(location=[40.75,-74.125])
if user == "1":
    bc = school.groupby("Borough/Community")
    print(bc.groups.keys())
    bcuser1 = input("Enter Borough/Community name: ")
    for index, row in school.iterrows():
        lat=row["Latitude"]
        lon=row["Longitude"]
        if row["Borough/Community"] == bcuser1:
            name = bc.get_group(bcuser1)
            newMarker = folium.Marker([lat,lon],popup=name)
            newMarker.add_to(schoolm)

if user == "2":
    bc = school.groupby("Grade Level / Age Group")
    print(bc.groups.keys())
    bcuser2 = input("Enter Grade Level / Age Group: ")
    for index, row in school.iterrows():
        lat=row["Latitude"]
        lon=row["Longitude"]
        if row["Grade Level / Age Group"] == bcuser2:
            name = bc.get_group(bcuser2)
            newMarker = folium.Marker([lat,lon],popup=name)
            newMarker.add_to(schoolm)

if user ==  "1":
    outfile_name = bcuser1.lower().replace(' ','_').replace('/','_')
    finaloutput_name = outfile_name + "_after_school.html"
    schoolm.save(outfile = finaloutput_name)

if user ==  "2":
    outfile_name = bcuser2.lower().replace(' ','_').replace('/','_')
    finaloutput_name = outfile_name + "_after_school.html"
    schoolm.save(outfile = finaloutput_name)
