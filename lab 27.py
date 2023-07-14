#victoria dynak
#victoria.dynak61@login.cuny.edu
#october 24 2022
#nyc covid 19 cases

import pandas as pd
import matplotlib.pyplot as plt
file= input("Enter a csv file: ")
borough = input("Enter borough (Bronx, Brooklyn, Queens, Manhattan, Staten Island): ")
newfilename = input("Enter output name: ")

filename = pd.read_csv(file)
bcase = filename[borough]

print("min: {}".format(bcase.min()))#the brackets and the format = placeholders
print("max: {}".format(bcase.max()))
print("mean: {}".format(round(bcase.mean(),3)))
print("median: {}".format(bcase.median()))
print("standard deviation: {}".format(round(bcase.std(),3)))

filename["Fraction"] = bcase/filename["case_count"]
filename.plot(x="date_of_interest",y="Fraction")

fig = plt.gcf()
fig.savefig(newfilename)
