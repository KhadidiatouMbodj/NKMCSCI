#Date: 03/13/2024
#This program loads an image, counts the number of pixels that are nearly white as an estimate for snow pack.


import matplotlib.pyplot as plt
import numpy as np


img=input("Enter file name:")
ca=plt.imread(img)
countsnow=0
t=0.75
for i in range(ca.shape[0]):
    for j in range(ca.shape[1]):
        if(ca[i,j,0]>t and (ca[i,j,1] > t) and (ca[i,j,2] > t)):
           countsnow=countsnow + 1

print(countsnow)
           
           
