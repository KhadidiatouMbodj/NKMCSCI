#Author:    Katherine St. John
#Date:      August 2014
#A program that uses command strings to control turtle drawing
#Modified by:  Ndeye Khadidiatou Mbodj
#Date: 03/13/2024

import turtle

mango = turtle.Turtle()
mango.shape("turtle")
commands = input("Please enter a command string: ")

for ch in commands:
    
    if ch == 'F':           
        mango.forward(50)
    elif ch == 'L':       
        mango.left(90)
    elif ch == 'R':        
        mango.right(90)
    elif ch == '^':          
        mango.penup()
    elif ch == 'v':          
        mango.pendown()
    elif ch == 'B':            
        mango.backward(50)
    elif ch == 'S':          
        mango.stamp()
    elif ch == 'l':         
        mango.left(45)
    elif ch == 'r':          
        mango.right(45)
    elif ch == 'p':         
        mango.color("purple")
    else:                    
        print("Error: do not know the command:", ch) 
      




