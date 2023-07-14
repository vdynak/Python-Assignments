#victoria dynak
#victoria.dynak61@login.cuny.edu
#october 29 2022
#internet plans in each continental region

import pandas as pd
import matplotlib.pyplot as plt

file = pd.read_csv("country_internet.csv")
continental = file.groupby('Continental region')
average = continental.mean()
print(average['NO. OF Internet Plans'])
print()
print("possible regions are", continental.groups.keys())
print(continental.groups.keys())

region = input("choose a region: ")
print("In the region", region)
subgroup = continental.get_group(region)
print("number of countries: ", file['Country'].count())

internetplans = subgroup['NO. OF Internet Plans']
print("maximum number of internet plans: ", internetplans.max())
print("minimum number of interner plans: ", internetplans.min())
output = input("Please enter output file name: ")

subgroup.plot.bar('Country','NO. OF Internet Plans')
plt.gcf().subplots_adjust(bottom =0.25)
plt.xlabel(f"Country in [h]")
plt.ylabel("NO. OF Internet Plans")
imgsave = plt.gcf()
imgsave.savefig(output)
