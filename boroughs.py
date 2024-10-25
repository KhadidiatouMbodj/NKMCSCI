#Name: Ndeye Khadidiatou Mbodj
#Email: ndeyekhadidiatou.mbodj48@myhunter.cuny.edu
#Date: 03/21/2024
#A program that prints borough stats.

import pandas as pd
import matplotlib.pyplot as plt

pop = pd.read_csv('nycHistPop.csv',skiprows=5)

borough=input("Enter a borough:")
print("Average population:",pop[borough].mean())
print("Maximum population:",pop[borough].max())
