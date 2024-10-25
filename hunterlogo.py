#name: Ndeye Khadidiatou Mbodj
#email: ndeyekhadidiatou.mbodj48@myhunter.cuny.edu
#date: March 23rd, 2024
#this program cuts images.
import numpy as np
import matplotlib.pyplot as plt

name=input('Enter image file name:')
output=input('Enter output file:')

img=plt.imread(name)
height=img.shape[0]
width=img.shape[1]
img2=img[height//2:,:width//2]

plt.imsave(output,img2)

