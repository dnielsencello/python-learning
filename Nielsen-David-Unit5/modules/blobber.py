# David Nielsen
# CS1400 - I01
# Unit 5 task 2 bobinator

import math
from time import time

class Blobber:

# Initializes blobber
    def __init__(self, name, color, radius, height):
        newName = ""
        for i in range(len(name)):
            if i == 0:
                newName += name[i].upper()
            else:
               newName += name[i].lower()
        self.__name = newName
        self.__color = color.lower()
        self.__radius = radius
        self.__height = height
        self.baseTime = time()
        self.__shrinkRadius = radius

# Checks vital of blobber
    def vitalsOK(self):
        shrinkTime = time()-self.baseTime
        self.baseTime = time()
        self.__shrinkRadius = self.__shrinkRadius - self.__radius*0.002*shrinkTime
        originalSize = self.__height*math.pi*self.__radius**2
        currentSize =  self.__height*math.pi*self.__shrinkRadius**2
        if 0.9 < currentSize/originalSize < 1.1:
            return currentSize/originalSize, True
        else:
            return currentSize/originalSize, False

# Returns name of blobber
    def getName(self):
        return self.__name

# Sets name of blobber
    def setName(self, name):
        newName = ""
        for i in range(len(name)):
            if i == 0:
                newName += name[i].upper()
            else:
                newName += name[i].lower()
        self.__name = newName

# returns color of blobber
    def getColor(self):
        return self.__color

# sets color of blobber
    def setColor(self, color):
        self.__color = color.lower()

# feeds blobber radius
    def feedBlobber(self, food):
        self.__shrinkRadius += food


