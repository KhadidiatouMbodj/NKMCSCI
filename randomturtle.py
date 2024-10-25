#Name: Ndeye Khadidiatou Mbodj
#Email: ndeyekhadidiatou.mbodj48@myhunter.cuny.edu
#Date: 04/15/2024
#A program that prints a random turtle.

import turtle
import random

mango = turtle.Turtle()
mango.speed(10)

for i in range(100):
  mango.forward(10)
  a = random.randrange(0,360,1)
  mango.right(a)
