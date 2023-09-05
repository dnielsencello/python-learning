# David Nielsen
# CS1400 - I01
# Unit 4 task 3 pattern
import turtle
from random import randint
import math


# Erase all of the patterns and start over
def reset():
    turtle.reset()
    setup()

# Configure turtle to draw quickly
# Configure turtle to have a window of 1000 x 800
def setup():
    turtle.speed(1000)
    turtle.screensize(1000, 800)

def drawRectanglePattern(centerX, centerY, offset, width, height, count, rotation):
    # Use parameters to define locations of rotation, and offset for each rectangle
    angle = 0
    for i in range(count):
        newX = centerX + offset*math.cos(2*math.pi*i/count)
        newY = centerY + offset*math.sin(2*math.pi*i/count)
        angle += 360 / count
        angle = rotation + 360*i/count
        drawRectangle(newX, newY, width, height, angle)

#useing turtle to draw a rectangle
def drawRectangle(newX, newY, width, height, angle):

    setRandomColor()
    turtle.penup()
    turtle.goto(newX, newY)
    turtle.setheading(angle)
    turtle.pendown()
    turtle.forward(width)
    turtle.setheading(angle + 90)
    turtle.forward(height)
    turtle.setheading(angle + 180)
    turtle.forward(width)
    turtle.setheading(angle + 270)
    turtle.forward(height)

#using parameter to draw all the circles in a pattern
def drawCirclePattern(centerX, centerY, offset, radius, count):
    for i in range(count):
        newX = centerX + offset * math.cos(2*math.pi*i/count)
        newY = centerY + offset * math.sin(2*math.pi*i/count)
        setRandomColor()
        turtle.penup()
        turtle.goto(newX, newY)
        turtle.pendown()
        turtle.circle(radius)

#super pattern using randint to set parameters for either a circle or a rectangle pattern
def drawSuperPattern(num):
    for i in range(num):
        centerY = randint(-300, 300)
        centerX = randint(-400, 400)
        offset = randint(-100, 100)
        count = randint(0, 100)
        type = randint(1, 2)
        if type == 1:
            width = randint(0, 100)
            height = randint(0, 100)
            rotation = randint(0, 360)
            drawRectanglePattern(centerX, centerY, offset, width, height, count, rotation)
        if type == 2:

            radius = randint(0, 100)
            drawCirclePattern(centerX, centerY, offset, radius, count)
#sets a random color
def setRandomColor():
    color = randint(1, 5)
    if color == 1:
        turtle.color('red')
    if color == 2:
        turtle.color('purple')
    if color == 3:
        turtle.color('blue')
    if color == 4:
        turtle.color('green')
    if color == 5:
        turtle.color('orange')
    return
# leaves window open after the user is done.
def done():
    turtle.done()

