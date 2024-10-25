#name: Ndeye Khadidiatou Mbodj
#email: ndeyekhadidiatou.mbodj48@myhunter.cuny.edu
#date: March 23rd, 2024
#this program prints NYC map.

import folium
nycMap=folium.Map(location=[40.75, -74.125])
folium.Marker(location = [40.768731, -73.964915], popup = "Hunter College").add_to(nycMap)
nycMap.save(outfile='nycMap.html')
