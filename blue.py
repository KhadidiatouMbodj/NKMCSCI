#name: Ndeye Khadidiatou Mbodj
#email: ndeyekhadidiatou.mbodj48@myhunter.cuny.edu
#date: February 12, 2024
#this program prints blue.

import turtle
turtle.colormode(255)
mango=turtle.Turtle()
mango.backward(100)
for i in range(0,255,10):
    mango.forward(10)
    mango.pensize(i)
    mango.color(0,0,i)
    
