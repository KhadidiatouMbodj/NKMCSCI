#this program prints CORNFLOWER BLUE PENTAGON.

import turtle
mango=turtle.Turtle()
mango.shape("turtle")
mango.color("cornflowerblue")
for i in range (5):
    mango.forward(100)
    mango.stamp()
    mango.left(360/5)
