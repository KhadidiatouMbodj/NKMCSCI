#Date: 03/21/2024
#A program that plots shelter census.

import pandas as pd
import matplotlib.pyplot as plt


shelter=input("Enter name of input file:")
output=input("Enter name of output file:")
homeless = pd.read_csv(shelter)

homeless["Fraction Children"]= homeless["Total Children in Shelter"] / homeless["Total Individuals in Shelter"]
homeless.plot(x = "Date of Census", y = "Fraction Children")


fig = plt.gcf()
fig.savefig(output)
