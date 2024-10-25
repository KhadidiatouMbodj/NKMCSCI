#date: March 6th, 2024
#this program prints stripes.
import matplotlib.pyplot as plt
import numpy as np

size=int(input('Enter a size:'))
file=input('Enter output file:')

img=np.ones((size,size,3))
img[::2,:,1]=0
img[1::2,:,2]=0

    
plt.imsave(file,img)
