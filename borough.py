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
