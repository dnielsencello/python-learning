# David Nielsen
# CS1400 - I01
# Assignment 1B


# bottom circle
import turtle
turtle.speed(100)
turtle.penup()
turtle.goto(0, -90)
turtle.pendown()
turtle.circle(55)

# middle circle
turtle.penup()
turtle.goto(0, 0)
turtle.pendown()
turtle.begin_fill()
turtle.color('white')
turtle.pencolor('black')
turtle.circle(40)
turtle.end_fill()
turtle.pendown()


# top circle
turtle.penup()
turtle.goto(0, 65)
turtle.pendown()
turtle.begin_fill()
turtle.color('white')
turtle.pencolor('black')
turtle.circle(35)
turtle.end_fill()
turtle.pendown()

# left eye
turtle.penup()
turtle.goto(-15, 95)
turtle.pendown()
turtle.begin_fill()
turtle.color('black')
turtle.circle(6)
turtle.end_fill()

# right eye
turtle.penup()
turtle.goto(15, 95)
turtle.pendown()
turtle.begin_fill()
turtle.color('black')
turtle.circle(6)
turtle.end_fill()

# mouth
turtle.penup()
turtle.goto(-15, 85)
turtle.pendown()
turtle.pencolor('orange')
turtle.setheading(360-30)
turtle.width(5)
turtle.circle(30, 60)

# buttons
# top
turtle.penup()
turtle.goto(0, 50)
turtle.pendown()
turtle.begin_fill()
turtle.color('purple')
turtle.circle(3)
turtle.end_fill()

# middle
turtle.penup()
turtle.goto(0, 35)
turtle.pendown()
turtle.begin_fill()
turtle.color('blue')
turtle.circle(4)
turtle.end_fill()

# bottom
turtle.penup()
turtle.goto(0, 20)
turtle.pendown()
turtle.begin_fill()
turtle.color('red')
turtle.circle(4)
turtle.end_fill()

# left arm
turtle.penup()
turtle.goto(-35, 35)
turtle.pendown()
turtle.pencolor('brown')
turtle.setheading(180 + 35)
turtle.goto(-60, 60)
turtle.goto(-60, 75)
turtle.goto(-60, 60)
turtle.goto(-75, 60)
turtle.goto(-60, 60)
turtle.goto(-70, 70)

# right arm
turtle.penup()
turtle.goto(35, 35)
turtle.pendown()
turtle.pencolor('brown')
turtle.setheading(180+35)
turtle.goto(60, 60)
turtle.goto(60, 75)
turtle.goto(60, 60)
turtle.goto(75, 60)
turtle.goto(60, 60)
turtle.goto(70, 70)

# top hat
turtle.penup()
turtle.goto(0, 115)
turtle.pendown()
turtle.begin_fill()
turtle.goto(-35, 115)
turtle.goto(-35, 125)
turtle.goto(-35, 140)
turtle.goto(35, 140)
turtle.goto(35, 120)
turtle.goto(70, 120)
turtle.goto(70, 115)
turtle.goto(0, 115)
turtle.color('red')
turtle.end_fill()

# other stuff
turtle.penup()
turtle.begin_fill()
turtle.goto(15, 85)
turtle.pencolor('black')
turtle.pensize(5)
turtle.pendown()
turtle.goto(45, 75)
turtle.goto(45, 85)
turtle.goto(15, 85)
turtle.color('brown')
turtle.end_fill()
turtle.hideturtle()
turtle.done()
