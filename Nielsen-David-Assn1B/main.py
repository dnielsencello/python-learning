import turtle
#bottom circle
turtle.penup()
turtle.goto(0,-80)
turtle.pendown()
turtle.circle(50)
#middle circle
turtle.penup()
turtle.goto(0,0)
turtle.pendown
turtle.begin_fill()
turtle.color("white")
turtle.circle(40)
turtle.end_fill()
turtle.pencolor("black")
turtle.pendown()
turtle.circle(40)

#top circle
turtle.penup()
turtle.goto(0,70)
turtle.pendown()
turtle.begin_fill()
turtle.color("white")
turtle.circle(30)
turtle.end_fill()
turtle.pencolor("black")
turtle.circle(30)

#left eye
turtle.penup()
turtle.goto(-15,95)
turtle.pendown()
turtle.begin_fill()
turtle.color("black")
turtle.circle(5)
turtle.end_fill()


#right eye

turtle.penup()
turtle.goto(15,95)
turtle.pendown()
turtle.begin_fill()
turtle.color("black")
turtle.circle(5)
turtle.end_fill()


#mouth#

turtle.penup()
turtle.goto(-15,85)
turtle.pendown()
turtle.pencolor("orange")
turtle.setheading(360-30)
turtle.width(5)
turtle.circle(30,60)


#buttons
#top
turtle.penup()
turtle.goto(0,50)
turtle.pendown()
turtle.begin_fill()
turtle.color("purple")
turtle.circle(3)
turtle.end_fill()
#middle
turtle.penup()
turtle.goto(0,35)
turtle.pendown()
turtle.begin_fill()
turtle.color("purple")
turtle.circle(3)
turtle.end_fill()

#bottom
turtle.penup()
turtle.goto(0,20)
turtle.pendown()
turtle.begin_fill()
turtle.color("purple")
turtle.circle(3)
turtle.end_fill()


# left arm
turtle.penup()
turtle.goto(-35,35)
turtle.pendown()
turtle.pencolor("Brown")
turtle.setheading(180+35)
turtle.goto(-60,60)
turtle.goto(-60,75)
turtle.goto(-60,60)
turtle.goto(-75,60)
turtle.goto(-60,60)
turtle.goto(-70,70)

#right arm
turtle.penup()
turtle.goto(35,35)
turtle.pendown()
turtle.pencolor("Brown")
turtle.setheading(180+35)
turtle.goto(60,60)
turtle.goto(60,75)
turtle.goto(60,60)
turtle.goto(75,60)
turtle.goto(60,60)
turtle.goto(70,70)

turtle.penup()
turtle.goto(0,115)
turtle.pendown()
turtle.pencolor("black")
turtle.begin_fill()
turtle.goto(-50,115)
turtle.goto(-50,125)
turtle.goto(-25,125)
turtle.goto(-25,180)
turtle.goto(25,180)
turtle.goto(25,125)
turtle.goto(50,125)
turtle.goto(50,115)
turtle.goto(0,115)
turtle.color("red")
turtle.end_fill()
turtle.done