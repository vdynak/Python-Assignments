#victoria dynak
#victoria.dynak61@login.cuny.edu
#october 8 2022
#blue and green vertical stripes 

import matplotlib.pyplot as plt
import numpy as np

number = int(input("Enter the size: "))
name = str(input("Enter output file: "))

img = np.ones((number,number,3))
imgcopy=img.copy()
imgcopy[::,::,0:2]=0
imgcopy[::,1::2,0:3]=0
imgcopy[::,1::2,1]=1

#plt.imshow(imgcopy)
#plt.show()
plt.imsave(name, imgcopy)

