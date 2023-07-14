#victoria dynak
#victoria.dynak61@login.cuny.edu
#november 6 2022
#central park map

import folium
mapnyc = folium.Map(location = [40.75, -74.125],zoom_start = 10)
folium.Marker(location = [40.7812, -73.9665], popup = "Central Park").add_to(mapnyc)
mapnyc.save(outfile = "nyc_Central_Park.html")         
