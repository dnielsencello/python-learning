# David Nielsen
# CS1400 - I01
# Unit 2 task 1


#RANDOM STATEMENT
#1. import random
#2. set a random number to be guessed

import random
print("Welcome to the Guessing Game")
number = random.randint(1, 11)
print("The computer has picked a number between 1 and 10. What is the number?")

#USER INPUT
#1. user inputs an integer number to guess.
guess = eval(input("What number do you choose (1-10)?:"))



#IF, ELIF, ELSE logic
#1. Start with if the user guesses exaclty
#   and work from either side of that value
#   that way msg will only ever be set to
#   one string value. Assign proper responses.

if guess == number:
    msg = "Exact Match: Honored to play with you, Master."
elif guess == (number + 1) or guess == (number - 1):
    msg = "Off by 1: You are a worthy opponent, Knight."
elif guess == (number + 2) or guess == (number -2):
    msg = "Off by 2: You have much to learn, Padawan."
elif guess == (number + 3) or guess == (number - 3):
    msg = "Off by 3: Youngling, your time will come."
else:
    msg = "Off by 4+: Keep working hard in the Service Corps."

# PRINT STATEMENT
print(msg)
