#name: Ndeye Khadidiatou Mbodj
#email: ndeyekhadidiatou.mbodj48@myhunter.cuny.edu
#date: March 23rd, 2024
#this program prints worst offenders.

import pandas as pd
csvfile= input('Enter CSV file name:')
attribute= input('Enter attribute:')
tickets=pd.read_csv(csvfile)
print("The worst 10 offenders are:")
print(tickets[attribute].value_counts()[:10])
