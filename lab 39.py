#victoria dynak
#victoria.dynak61@login.cuny.edu
#november 6 2022
#movie locations

import pandas as pd

movies = pd.read_csv("movie_locations.csv")

number = int(input("order of most popular neighborhoods in movies: "))
print(movies['Neighborhood'].value_counts()[:number])

directors = int(input("order of directors/filmmakers making most movies in NYC: "))
print(movies['Director/Filmmaker Name'].value_counts()[:directors])
              
