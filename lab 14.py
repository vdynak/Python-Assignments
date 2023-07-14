#victoria dynak
#victoria.dynak61@login.cuny.edu
#september 25, 2022

import matplotlib.pyplot as plt
import numpy as np

userinput = input("Enter name of the input file: ")
useroutput = input("Enter name of the output file: ")
    
img = plt.imread(userinput)   

img2 = img.copy()        
img2[:,:,0] = 0         

plt.imsave(useroutput, img2)
