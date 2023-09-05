from random import randint
from math import pi
from time import time


import time

class FakeTimer:
    def __init__(self):
        self.baseTime = time()

    def getElapsedTime(self):
        return time() - self.baseTime

    def resetBaseTime(self):
        self.baseTime = time()



    def __repr__(self):
        return self.baseTime

class Orbian:
    def __init__(self, name):
        self.__name = name
        self.__bodyHeight = randint(5, 12)
        self.__bodyRadius = randint(3, 8)
        self.__headRadius = randint(2, 5)
        self.__timer = FakeTimer
    def getName(self):
        return self.__name

    def setName(self, name):
         self.__name = name

    def getVolume(self):
        return pi * self.__bodyRadius ** 2 * self.__bodyHeight

    def getBodyRadius(self):
        return self.__bodyRadius

    def getBodyHeight(self):
        return self.__bodyHeight

    def getAge(self):
        return self.__timer

    def getHeadradius(self):
        return self.__headRadius

    def __repr__(self):
        return self.__name

    def snap(self):
        return self.__pop()