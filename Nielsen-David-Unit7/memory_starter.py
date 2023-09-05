# David Nielsen
# CS1400 - I01
# Unit 7 memorystarter
from modules.memoryboard import MemoryBoard

# This import gives some funcitonality if your run the program from the commandline. See the video in the assignment
# for instructions. Running in the terminal makes the game board play more like a game instead of scrolling and
# printing a new board every time.
# You'll need to comment a line down below in the printGameBoard() function if using PyCharm
import os

def main():
    playerTurn = 0 # Keep track of whose turn it is

    print("Welcome to Memory\n")

    # Get the Board Size
    cols = int(input("Enter the number of columns on the board: "))
    rows = int(input("Enter the number of rows on the board: "))

    # Get the number of players
    playerCount = int(input("Enter the number of players: "))
    scores = [0] * playerCount

    # Create the MemoryBoard object
    memoryBoard = MemoryBoard(rows, cols)

    # Game loop
    winner = False
    while not winner:
        selectedCards = [] # Track the cards the current player selected
        printGameBoard(scores, memoryBoard.getBoard())

        # Each turn is two card flips
        #changed to a while loop the exits when the number of flipped cards is 2
        flippedCards = 0
        while flippedCards < 2:
            xPos, yPos = eval(input("Player " + str(playerTurn + 1) + " choose a card to flip: "))
            # BUG added this line of code to append to selected cards

            if not memoryBoard.isCardFlipped(xPos, yPos):
                selectedCards.append([xPos, yPos])
                memoryBoard.flipCard(xPos, yPos)
                flippedCards += 1
            else:
                input("That card has been flipped. Hit Enter to try again")

            printGameBoard(scores, memoryBoard.getBoard())

        # Player goes again if they get a match
        if memoryBoard.isMatch(selectedCards[0], selectedCards[1]):
            print("You got a match!")
            # BUG score can't be added to player 3 for score player 2 earned
            scores[playerTurn] += 1
            # BUG change / to //
            winner = sum(scores) == cols * rows // 2

            # If the game is over show a different message
            # BUG Added continue
            if winner:
                input("Hit Enter to Continue")
            else:
                #BUG added 1 to the playerTurn value
                # BUG added continue
                input("Player " + str(playerTurn + 1) + " hit Enter to go again.")
                continue
        else:
            #BUG flip back proper card add continue statement
            memoryBoard.flipCard(selectedCards[0][0], selectedCards[0][1])
            memoryBoard.flipCard(selectedCards[1][0], selectedCards[1][1])
            print("No Match")
            #BUG start over if there are no more players and no one has won
            if playerTurn + 1 == playerCount:
                playerTurn = 0
            else:
                playerTurn += 1
            input("Hit Enter for Player " + str(playerTurn + 1))
            continue


    # Find the winning score value
    highScore = max(scores)

    # Check for a tie/winner
    # Bug, must print out who tied
    if scores.count(highScore) > 1:
        print("The following players tied: ", end="")
        for i in range(len(scores)):
            if scores[i] == highScore:
                print(i + 1, end=" ")
    else:
        print("The winner is player " + str(scores.index(highScore) + 1))


# Print the scoreboard and gameboard
def printGameBoard(scores, board):
    os.system('cls||clear') # Comment this out if running in PyCharm
    for i in range(len(scores)):
        print("Player " + str(i + 1) + ": " + str(scores[i]))
    print()
    print(board)


main()