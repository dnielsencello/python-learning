# David Nielsen
# CS1400 - I01
# Unit 2 task 3

# 1. random modules seed and randint
# 2. import math statement
import math
from random import seed
from random import randint
import time

startTime = time.time()

# 3. assign variables outside the loop
# count the number of fluky numbers
# count the number of iterations
numberOfFlukyNumbers = 0
iterations = 0
theNumber = 1


while numberOfFlukyNumbers < 14:
    # 4. assign variables inside the loop
    # the Number = the iterated number from 1 until the number of fluky numbers equals 14
    # the sum of the possible factors of the number
    # numberOfFactors = the number of factors of the Number
    # generated number = the number that is generated
    # possible factors = a test to see if a number is a factor of the Number
    theNumber += 1
    sum1 = 1
    numberOfFactors = 1
    generatedNumber = int()
    # if the number has a square root
    # set a range limit to search for factorials to the square root of the number
    # otherwise the range limit is the number divided by 2
    if math.sqrt(theNumber) - int(math.sqrt(theNumber)) == 0:
        rangeLimit = int(math.sqrt(theNumber))
        fluff = 0
    else:
        rangeLimit = int(theNumber/2)
    # for loop iterates through each number that is a possible factor of the number from 2 up to the range limit
    # one is accounted for earlier
    # if a number is a factor it is added to a sum
    # keep track of how many factors there are
    for possibleFactor in range(2, rangeLimit + 1):
        iterations += 1
        if theNumber % possibleFactor == 0:
            numberOfFactors += 1
            sum1 += possibleFactor
    # the sum of the factorials becomes the input for the seed function
    seed(sum1)


    # a for loop generates the number produced by the randint function based on the number of factors of the number and the seed
    for i in range(0, numberOfFactors):
        iterations += 1
        generatedNumber = randint(0, theNumber)
    # if the generated number == the number, then we have a fluky number.
    if generatedNumber == theNumber:
        numberOfFlukyNumbers += 1
        print("Fluky Number:" + str(generatedNumber))

#time
totalTime = round(time.time() - startTime, 2)

#print statements
print("Time " + str(totalTime) + " seconds")
print("Total Loops:" + str(iterations))




