# David Nielsen
# CS1400 - I01
# Unit 4 task 3
'''
    This is the starter file. Only fill in the areas indicated.
    Do not modify existing code.
    Replace this file header with the normal file header (name, etc)
'''

#### Add Import Statement(s) as needed ####
import pattern
import random
#### End Add Import Statement(s) ####

def main():
    # Setup pattern
    pattern.setup()
    # Play again loop
    playAgain = True

    while playAgain:
        # Present a menu to the user
        # Let them select mode
        print("Choose a mode")
        print("1) Rectangle Pattern")
        print("2) Circle Pattern")
        print("3) Super Pattern")
        mode = eval(input("Which mode do you want to play? 1, 2 or 3: "))

        # If they choose 'Rectangle Patterns'
        if mode == 1:
            #### Add Input Statement(s) as needed ####
            centerX, centerY = eval(input("What is the center position?: "))
            offset = eval(input("What is the offset?: "))
            height = eval(input("What is the height?: "))
            width = eval(input("What is the width?: "))
            rotation = eval(input("What is the rotation?:"))
            count = eval(input("What is the count?:"))
            #### End Add Inputs Statement(s) ####


            # Draw the rectangle pattern
            pattern.drawRectanglePattern(centerX, centerY, offset, width, height, count, rotation)

        # If they choose 'Circle Patterns'
        elif mode == 2:
            #### Add Input Statement(s) as needed ####
            centerX, centerY = eval(input("Where is the center of the circle?: "))
            offset = eval(input("What is the distance from the center of the circle?: "))
            radius = eval(input("What is the radius of the circle?: "))
            count = eval(input("How many circles are there?: "))

            #### End Add Inputs Statement(s) ####

            # Draw the circle pattern
            pattern.drawCirclePattern(centerX, centerY, offset, radius, count)

        # If they choose 'Super Patterns'
        elif mode == 3:
            #### Add Input Statement(s) as needed ####
            num = input("Number?: ")
            #### End Add Inputs Statement(s) ####
            if num == "":
                pattern.drawSuperPattern(random.randint(1, 10))
            else:
                pattern.drawSuperPattern(eval(num))

        # Play again?
        print("Do you want to play again?")
        print("1) Yes, and keep drawings")
        print("2) Yes, and clear drawings")
        print("3) No, I am all done")
        response = eval(input("Choose 1, 2, or 3: "))

        #### Add Statement(s) to clear drawings and play again ####
        if response == 1:
            continue
        if response == 2:
            pattern.reset()
        if response == 3:
            playAgain = False
        #### End Add Inputs Statement(s) ####

    # print a message saying thank you
    print("Thanks for playing!")
    pattern.done()


main()
