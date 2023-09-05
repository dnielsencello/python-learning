# David Nielsen
# CS1400 - I01
# Assignment 2 task 2

import turtle

# User designates diameter of target inner circle and the coordinates of the
# center of the target
diameter = eval(input('What is the diameter of the inner bullseye?: '))
x = eval(input('What is the x coordinate of the target?: '))
y = eval(input('What is the y coordinate of the target?: '))
radius = diameter/2

# This section of code draws the outermost black circle
turtle.penup()
turtle.goto(x, y - 4*radius)
turtle.pendown()
turtle.color('black')
turtle.begin_fill()
turtle.circle(4*radius)
turtle.end_fill()

# This section of code draws the next yellow circle
turtle.penup()
turtle.goto(x, y - 3*radius)
turtle.pendown()
turtle.color('blue')
turtle.begin_fill()
turtle.circle(3*radius)
turtle.end_fill()

# This section of code draws the next red circle
turtle.penup()
turtle.goto(x, y - 2*radius)
turtle.pendown()
turtle.color('red')
turtle.begin_fill()
turtle.circle(2*radius)
turtle.end_fill()

# This section of code draws the innermost yellow circle
turtle.penup()
turtle.goto(x, y - 1*radius)
turtle.pendown()
turtle.color('yellow')
turtle.begin_fill()
turtle.circle(1*radius)
turtle.end_fill()


turtle.hideturtle()
turtle.done()
