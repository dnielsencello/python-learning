import random
from math import pi
from random import shuffle # Hint hint
from random import randint
import time

class Orbian:
    # DO NOT MODIFY THE CONSTRUCTOR
    def __init__(self, name, headRadius, bodyRadius, bodyHeight):
        # NOTE: These are constants
        self.__HEAD_RADIUS = headRadius
        self.__BODY_RADIUS = bodyRadius
        self.__BODY_HEIGHT = bodyHeight
        self.__NAME = name
        self.__BIRTH_TIME = time.time()

        # This is the only variable
        self.__adult = False


    def __getHeadVolume(self):
        return 4 / 3 * pi * self.__getHeadRadius() ** 3

    def __getBodyVolume(self):
        return pi * self.__getBodyRadius() ** 2 * self.__getBodyHeight()

    def __ageCheck(self):
        # Become an adult at 2
        if self.getAge() >= 2:
            if not self.__adult:
                self.__HEAD_RADIUS *= 2
                self.__BODY_RADIUS *= 2
                self.__BODY_HEIGHT *= 4
            self.__adult = True

    ####### ADD OTHER REQUIRED METHODS BELOW. SEE THE ASSIGNMENT DESCRIPTION AND OTHER STARTER CODE FOR INSIGHT ######
    def __getHeadRadius(self):
        self.__ageCheck()
        return self.__HEAD_RADIUS

    def __getBodyRadius(self):
        self.__ageCheck()
        return self.__BODY_HEIGHT

    def __getBodyHeight(self):
        self.__ageCheck()
        return self.__BODY_HEIGHT

    def getAge(self):
        return round((time.time() - self.__BIRTH_TIME)/5, 2)

    def getName(self):
        return self.__NAME

    def getVolume(self):
        return round(self.__getHeadVolume() + self.__getBodyVolume(), 2)

    def __add__(self, other):
        self.__ageCheck()
        other.__ageCheck()
        newName = ''
        newNameTemp = [i for i in (self.__NAME + other.getName())]
        random.shuffle(newNameTemp)

        for i in range(int(len(newNameTemp)/2)):
            if i == 0:
                newName += newNameTemp[i].upper()
            else:
                newName += newNameTemp[i].lower()
        heightOfBaby = int(0.125 * (self.__BODY_HEIGHT + other.__getBodyHeight()))
        bodyRadiusOfBaby = int(0.25 * (self.__BODY_RADIUS + other.__getBodyRadius()))
        headRadiusOfBaby = int(0.25 * (self.__HEAD_RADIUS + other.__getHeadRadius()))

        return Orbian(newName, headRadiusOfBaby, bodyRadiusOfBaby, heightOfBaby)

    def __eq__(self, other):
        self.__ageCheck()
        theyAreTheSameVolume = self.__getHeadVolume() + self.__getBodyVolume() == other.__getHeadVolume() + other.__getBodyVolume()
        return theyAreTheSameVolume

    def __gt__(self, other):
        self.__ageCheck()
        orb1IsBiggerThanOrb2 = self.__getHeadVolume() + self.__getBodyVolume() > other.__getHeadVolume() + other.__getBodyVolume()
        return orb1IsBiggerThanOrb2

    def __len__(self):
        return self.__BODY_HEIGHT + self.__HEAD_RADIUS*2

    def __str__(self):
        return "I am Orbain " + self.__NAME





