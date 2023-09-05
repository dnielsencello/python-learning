from drawChessboard import drawChessboard
startX, startY = eval(input("Enter start positions: "))
width = input("Enter the width: ")
height = input("Enter the height: ")

def main():
    if width == "" and height == "":
        drawChessboard(startX, startY)
    elif height == "":
        drawChessboard(startX, startY, width=eval(width))
    elif width == "":
        drawChessboard(startX, startY, height=eval(height))
    else:
        drawChessboard(startX, startY, eval(width), eval(height))
main()

