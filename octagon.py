#date: FEBRUARY 5, 2024
#This program draws an octagon.

import turtle
wn = turtle.Screen()

mango = turtle.Turtle()
for i in range(8):
    mango.forward(100)
    mango.left(45)

wn.exitclick()
