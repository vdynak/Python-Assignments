#victoria dynak
#victoria.dynak61@login.cuny.edu
#october 30 2022
#image cropping

import numpy as np
import matplotlib.pyplot as plt

print("Enter 1 to get upper right corner")
print("Enter 2 to get middle portion")
choice = input("Your choice: ")
if choice == '1':
    inputfile = input("Enter input file name: ")
    outputfile = input("Enter output file name: ")
    img = plt.imread(inputfile)
    height = img.shape[0]
    width = img.shape[1]
    img2 = img[:height//2, width//2:]
    plt.imsave(outputfile,img2)
    plt.show()
elif choice == '2':
    inputfile = input("Enter input file name: ")
    outputfile = input("Enter output file name: ")
    img = plt.imread(inputfile)
    height = img.shape[0]
    width = img.shape[1]
    img2 = img[height//4:height//4*3, width//4:width//4*3]
    plt.imsave(outputfile,img2)
    plt.show()
else:
    if choice != '1' and choice != '2':
        print("wrong choice")
        exit()
