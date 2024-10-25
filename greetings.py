#this program prints greetings.

hour=int(input('Enter hour (in 24 hour time):'))
if hour<12:
         print('Good Morning')
if hour>=12 and hour<17:
          print('Good Afternoon')
        
elif hour>=17:
        print ('Good Evening')
