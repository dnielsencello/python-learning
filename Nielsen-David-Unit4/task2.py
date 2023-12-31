# David Nielsen
# CS1400 - I01
# Unit 4 task 2
'''
    This is the starter file. Only fill in the areas indicated.
    Do not modify existing code.
    Replace this file header with the normal file header (name, etc)
'''
#### Add Import Statement(s) as needed ####
from chessboard import drawChessboard
#### End Add Import Statement(s) ####

def main():

    #### Add Code to get input from user ####
    startX, startY = eval(input("Enter start positions: "))
    width = input("Enter the width: ")
    height = input("Enter the height: ")
    #### End Add Code to get input from user ####

    if width == "" and height == "":
        drawChessboard(startX, startY)
    elif height == "":
        drawChessboard(startX, startY, width=eval(width))
    elif width == "":
        drawChessboard(startX, startY, height=eval(height))
    else:
        drawChessboard(startX, startY, eval(width), eval(height))


main()