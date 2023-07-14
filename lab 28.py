#victoria dynak
#victoria.dynak61@login.cuny.edu
#october 24 2022
#children/lead/pandas
import pandas as pd
import matplotlib.pyplot as plt

lead = pd.read_csv("children_lead.csv")

option = input("""Enter a choice:
a.group by borough
b.group by year
 """)
print("average number of affected children by borough")
if (option == "a"):
    groupedData = lead.groupby("borough")
    print(groupedData['affected_children'].mean())
    bb = input("Enter a borough: ")
    boroin = groupedData.get_group(bb)
    print ("average number of affected children in ", bb, " is " , boroin['affected_children'].mean())
    print ("max number of affected children in ", bb, " is " , boroin['affected_children'].min())
    print ("min number of affected children in ", bb, " is " , boroin['affected_children'].max())            
elif(option == "b"):
    groupedData = lead.groupby("year")
    print(groupedData['affected_children'].mean())
    yeari = input("Enter a year (2005-2016): ")
    yearin = groupedData.get_group(int(yeari))
    print ("average number of affected children in ", yeari, " is " , yearin['affected_children'].mean())
    print ("min number of affected children in ", yeari, " is " , yearin['affected_children'].min())
    print ("max number of affected children in ", yeari, " is " , yearin['affected_children'].max())
else:
    print("wrong choice")
    
