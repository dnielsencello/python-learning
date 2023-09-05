# David Nielsen
# CS1400 - I01
# Unit 7 memorycard

class MemoryCard:

    def __init__(self, idNumber):
        self.__idNumber = idNumber
        self.__cardValue = chr(33 + idNumber//2)
        self.__flipped = False

    def getValue(self):
        return self.__idNumber

    def toggleFlipped(self):
        if self.__flipped == False:
            self.__flipped = True
        else:
            self.__flipped = False

    def displayCard(self):
        if self.__flipped == False:
            return " "
        else:
            return self.__cardValue

    def isFlipped(self):
        if self.__flipped == False:
            return False
        else:
            return True

    def __repr__(self):
        return self.__cardValue
