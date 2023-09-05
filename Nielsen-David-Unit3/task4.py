# David Nielsen
# CS1400 - I01
# Unit 2 task 4

# 1. Import statements
from random import randint


done = False
# 2. the program will ultimately ask the user if they would like to
# to continue, therefore it will be in a while loop

while not done:
    elephantInStall = 0
    bothElephatsInStall = 0
    # 3. we will check to see what stall each elephant will enter each night
    # for loop from 1 to 10000
    # elephant one will enter a stall
    # elephant two will enter a stall
    # zookeeper will check a stall
    for i in range(100000):
        elephant1 = randint(1, 6)
        elephant2 = randint(1, 6)
        zookeeper = randint(1, 6)
        # Nested if statement
        # if the zookeeper sees elephant1 or elephant2 in a stall we will count
        # add it to a total
        # if the zookeeper sees that both elephants are in the stall we
        # will add it to a seperate total.
        if zookeeper == elephant1 or zookeeper == elephant2:
            elephantInStall += 1
            if elephant1 == elephant2:
                bothElephatsInStall += 1
    # 4. doing math
    occurance1 = round(elephantInStall*100/100000, 2)
    occurance2 = round(bothElephatsInStall*100/elephantInStall, 2)
    # Printing of the results to console

    print("The zookeeper saw an elephant inside a stall " + str(occurance1) + '% of the time.')
    print("The zookeeper saw both elephants inside a stall " + str(occurance2) + '% of the time')
    print("The custodian is right")

    # Prompt user if they would like to continue
    keepGoing = input("Would you like to continue? (Yes/No): ").lower()

    if keepGoing == "yes":
        done = False
    else:
        done = True


