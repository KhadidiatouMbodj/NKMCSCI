#this program prints NYC collision map.

import folium
import pandas as pd
csvfile= input('enter CSV file name:')
output=input('enter output file name:')
file=pd.read_csv(csvfile)

nycMap=folium.Map(location=[40.75, -74.125])
file['LATITUDE']=file['LATITUDE'].fillna(0)
file['LONGITUDE']=file['LONGITUDE'].fillna(0)

for index, row in file.iterrows():
    if row['LATITUDE']!=0 and row['LONGITUDE']!=0:
        folium.Marker([row['LATITUDE'],row['LONGITUDE']]).add_to(nycMap)
nycMap.save(outfile=output)
