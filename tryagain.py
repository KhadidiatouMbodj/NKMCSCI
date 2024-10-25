#Date: 04/15/2024
#A program that asks user for a string.

string=input('Enter a non-empty string:')
while string=="":
    print('That was empty. Try again')
    string=input('Enter a non-empty string:')
print('You entered:',string)
