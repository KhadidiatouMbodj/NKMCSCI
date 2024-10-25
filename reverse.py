#name: Ndeye Khadidiatou Mbodj
#email: ndeyekhadidiatou.mbodj48@myhunter.cuny.edu
#date: March 6th, 2024
#this program prints reverse.

msg=input("Enter a message:")
l=len(msg)

for i in range(l-1,-1,-1):
    print(msg[i:i+1],msg[i:i+1])


