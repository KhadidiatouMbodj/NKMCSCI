#name: Ndeye Khadidiatou Mbodj
#email: ndeyekhadidiatou.mbodj48@myhunter.cuny.edu
#date: March 23rd, 2024
#this program prints names.

fullname=input("Please enter your list of names:")
print('You entered:')
name=fullname.split('; ')
first=[]
for i in range(len(name)):
    first= first+name[i].split(',')
for i in range (0,len(first),2):
    print(first[i+1],' ',first[i])
print('Thank you for using my name organizer!')
     

