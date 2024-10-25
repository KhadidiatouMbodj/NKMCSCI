#Date: 03/13/2024
#This program prints plurals

msg=input('Enter nouns:')
x=msg.count(' ')+1
s=0
check=msg.endswith('s')

if (check==True):
    y=msg.count('s ')+1
if (check==False):
    y=msg.count('s ')
   
   
print('Number of words:',x)
print('Fraction of your list that is plural',y/x)

