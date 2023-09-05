# David Nielsen
# CS1400 - I01
# Unit 4 task 2 chessboard
import turtle

#draw chessboard outline, calls drawAllRectangles
def drawChessboard(startX, startY, width = 250, height = 250):
    turtle.penup()
    turtle.goto(startX, startY)
    turtle.pendown()
    turtle.goto(startX + width, startY)
    turtle.goto(startX + width, startY + height)
    turtle.goto(startX, startY + height)
    turtle.goto(startX, startY)
    drawAllRectangles(startX, startY, width, height)
    turtle.hideturtle()
    turtle.done()

#determines postions, height, and width for all rectangles in chessboard
def drawAllRectangles(startX, startY, width, height):
    width2 = width/8
    height2 = height/8

    for i in range(0, 8, 2):
        startY2 = startY + i * height2
        for j in range(0, 8, 2):
            startX2 = startX + j * width2
            drawRectangle(startX2, startY2, width2, height2)
    startY += height/8
    startX += width/8
    for i in range(0, 8, 2):
        startY2 = startY + i * height2
        for j in range(0, 8, 2):
            startX2 = startX + j * width2
            drawRectangle(startX2, startY2, width2, height2)

#draws rectangles
def drawRectangle(startX, startY, width, height):
    turtle.penup()
    turtle.goto(startX, startY)
    turtle.pendown()
    turtle.begin_fill()
    turtle.goto(startX + width, startY)
    turtle.goto(startX + width, startY + height)
    turtle.goto(startX, startY + height)
    turtle.goto(startX, startY)
    turtle.end_fill()

