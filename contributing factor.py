#this program prints contributing factors.

import pandas as pd
csvfile=input('Enter CSV file name:')
tickets=pd.read_csv(csvfile)
print("Top three contributing factors for collisions:")
print(tickets['CONTRIBUTING FACTOR VEHICLE 1'].value_counts()[:3])

