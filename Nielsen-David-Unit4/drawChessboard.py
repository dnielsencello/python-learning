import turtle


def drawChessboard(startX, startY, width = 250, height = 250):
    turtle.penup()
    turtle.goto(startX, startY)
    turtle.pendown()
    turtle.goto(startX+width, startY)
    turtle.goto(startX+width, startY+height)
    turtle.goto(startX, startY+height)
    turtle.goto(startX, startY)
    sX = startX
    sY = startY
    width = width/8
    height = height/8
    turtle.fillcolor("black")
    for j in range(1, 5):
        for i in range(1,5):

            turtle.begin_fill()
            turtle.penup()
            turtle.goto(sX+width, sY)
            turtle.pendown()
            turtle.goto(sX+2*width, sY)
            turtle.goto(sX+2*width, sY+height)
            turtle.goto(sX + width, sY + height)
            turtle.goto(sX+width, sY)
            sX = sX+2*width
            turtle.end_fill()
        sX = startX
        sY = sY+2*height
    sY = startY+height
    for j in range(1,5):
        for i in range(1,5):
            turtle.begin_fill()
            turtle.penup()
            turtle.goto(sX , sY)
            turtle.pendown()
            turtle.goto(sX + width, sY)
            turtle.goto(sX + width, sY + height)
            turtle.goto(sX, sY + height)
            turtle.goto(sX, sY)
            sX = sX + 2 * width
            turtle.end_fill()
        sX = startX
        sY = sY+2*height
    turtle.hideturtle()
    turtle.done()

