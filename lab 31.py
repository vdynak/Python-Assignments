#victoria dynak
#victoria.dynak61@login.cuny.edu
#october 30, 2022
#percentages of internet users/population

import pandas as pd
import matplotlib.pyplot as plt

foutput = input("Enter output file name: ")


file = pd.read_csv("country_internet.csv")
file['Percentage'] = ((file['Internet users']/file['Population'])*100)
file.plot(x='Country',y='Percentage')
vmax = file['Percentage'].idxmax()
print(("maximum percentage of all countries: "), file['Country'][vmax],round(file['Percentage'][vmax],2), "%")
result = plt.gcf()
result.savefig(foutput)
