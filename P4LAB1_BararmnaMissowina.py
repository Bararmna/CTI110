# Bararmna Missowina
# Date
# P4LAB1
# Use turtle and loops to draw a square and a triangle.


# Import the library
import turtle

#create the turtle window and drawing object

Win = turtle.Screen()
pen = turtle.Turtle()


# set turtle options
pen.pensize (5)
pen.pencolor("blue")
pen.shape("arrow")

# Code to draw the shapes
for side in range(4):
    pen.forward(100)
    pen.left(90)

#While loop that executes 3 times
sides = 3
while sides > 0:
    pen.forward(100)
    pen.left(120)
    sides = sides - 1


             
