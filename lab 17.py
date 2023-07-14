#victoria dynak
#victoria.dynak61@login.cuny.edu
#october 8 2022
#t-shape

import matplotlib.pyplot as plt
import numpy as np

output = input(str("Enter output file name: "))

img = np.ones((30,30,3))#sets grid
imgcopy = img.copy()
imgcopy[:,:,2]=0 #sets back to yellow
imgcopy[5:8,5:25,0]=0 #horizontal to blue
imgcopy[5:8,5:25,1]=0
imgcopy[5:8,5:25,2]=1
imgcopy[8:25,13:16,0]=0 #vertical to green

#plt.imshow(imgcopy)
#plt.show()

plt.imsave(output ,imgcopy)




"""img = np.ones((30,30,3))
img[0:30,0:30,2]=0 #sets background to yellow
img[5:9,5:26,0:2]= 0
img[5:9,5:26,2]= 1
img[8:26,13:17,0]=0
img[8:26,13:17,2]=0
img[8:26,13:17,1]=1
img[8:9,13:17,0]=0
img[8:9,13:17,1]=0
img[8:9,13:17,2]=1
plt.imshow(img)
plt.show()

plt.imsave("shape_t.png", img)



tshape = np.ones((30,30,3))#,(255,255,0))
tshape =[0:31,0:31,3]=0
#tshape[5:9,5:26,0:2]= 0
#tshape[5:9,5:26,2]= 255
#tshape[8:26,13:17,0:1]=1

plt.imshow(tshape)
plt.show()
#plt.imsave("shape_t.png", tshape)
"""
