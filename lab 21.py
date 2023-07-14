#victoria dynak
#victoria.dynak61@login.cuny.edu
#october 9 2022
#This program loads an image, counts the number of pixels that are
#    nearly white as an estimate for snow pack.


import matplotlib.pyplot as plt
import numpy as np

filename = input("Enter file name: ")
t = float(input("Enter threshold: "))

vimage = plt.imread(filename)  
countwhite = 0           #Number of pixels that are almost white
counttotal = 0
               
#For every pixel:
for i in range(vimage.shape[0]):
     for j in range(vimage.shape[1]):
          counttotal +=1
          #Check if red, green, and blue are > t:
          if (vimage[i,j,0] > t) and (vimage[i,j,1] > t) and (vimage[i,j,2] > t):
               countwhite = countwhite + 1

               
percentage = (countwhite/counttotal)*100

print("number of white pixels:" + str(countwhite))
print("percent of white pixels:" + str(round(percentage,2)),"%")
