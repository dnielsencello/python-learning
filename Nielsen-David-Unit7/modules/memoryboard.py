# David Nielsen
# CS1400 - I01
# Unit 7 memoryboard
from modules.memorycard import MemoryCard
from random import shuffle

# bug found naming of class
class MemoryBoard:

    def __init__(self, columns, rows):
        self.__rows = rows
        self.__columns = columns
        self.__deck = [MemoryCard(i) for i in range(rows*columns)]
        shuffle(self.__deck)
        self.__board = [[self.__deck.pop() for j in range(columns)] for i in range(rows)]

    def getBoard(self):
        board = "  |"
        for i in range(self.__columns):
            board += " " + str(i + 1) + " |"
        board += "\n"
        rowLength = len(board)-1
        for i in range(self.__rows):
            board += "-" * rowLength + "\n"
            board += str(i + 1) + " |"
            for j in range(self.__columns):
                board += " " + MemoryCard.displayCard(self.__board[i][j]) + " |"
            board += "\n"
        board += "-" * rowLength + "\n"
        return board
    def flipCard(self, xpos, ypos):
        MemoryCard.toggleFlipped(self.__board[ypos - 1][xpos - 1])

    def isCardFlipped(self, xpos, ypos):
        return MemoryCard.isFlipped(self.__board[ypos - 1][xpos - 1])

    def isMatch(self, pos1, pos2):
        if str(self.__board[pos1[1]-1][pos1[0]-1]) == str(self.__board[pos2[1]-1][pos2[0]-1]):
            return True
        else:
            return False



