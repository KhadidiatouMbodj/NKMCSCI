#Name: Ndeye Khadidiatou Mbodj
#Email: ndeyekhadidiatou.mbodj48@myhunter.cuny.edu
#Date: 03/21/2024
#A program that plots borough fractions.

import pandas as pd
import matplotlib.pyplot as plt

pop = pd.read_csv('nycHistPop.csv',skiprows=5)

borough=input("Enter a borough name:")
filename=input("Enter output file name:")

pop['Fraction'] = pop[borough]/pop['Total']
pop.plot(x = 'Year', y = 'Fraction')

fig = plt.gcf()
fig.savefig(filename)
