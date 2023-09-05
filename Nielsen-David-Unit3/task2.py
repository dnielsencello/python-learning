# David Nielsen
# CS1400 - I01
# Unit 2 task 2

# THE SOCIAL SITUATION ANALYZER

# USER INPUTS INFORMATION ABOUT PERSONAL BUBBLES AND SPACE FOR PERSON ONE
print("Welcome to the Social Situation Analyzer System")
print("Person One")
name1 = input("Enter your name: ")
x1, y1 = eval(input("   Enter your position (x, y): "))
r1 = eval(input("   Enter your personal space radius: "))

# USER INPUTS INFORMATION ABOUT PERSONAL BUBBLES AND SPACE FOR PERSON TWO
print("\nWelcome to the Social Situation Analyzer System")
print("Person Two")
name2 = input("Enter your name: ")
x2, y2 = eval(input("   Enter your position (x, y): "))
r2 = eval(input("   Enter your personal space radius: "))

# Calculations
# Person 1 to Person 2 distance
d = ((x1 - x2)**2 + (y1 - y2)**2)**0.5


# START OF CONSOLE MESSAGE
msg = "\nSocial Situation Analysis Results\n"

# DECISION TREE FROM SOFTWARE DEVELOPMENT PLAN
if d < r1 and d < r2:
    msg += name1 + " and " + name2 + " are in each other's space \n"
    if r2 + d <= r1:
        msg += name1 + "'s personal space is entirely inside" + name2 + "'s personal space"
    elif r1 + d <= r2:
        msg += name2 + "'s personal space is entirely inside" + name1 + "'s personal space"
    else:
        msg += name1 + "'s and " + name2 + "'s space overlap"
elif d < r1 and d > r2:
    msg += name2 + " is in " + name1 + "'s personal space\n"
    if r2 + d <= r1:
        msg += name2 + "'s personal space is entirely inside" + name1 + "'s personal space"
    else:
        msg += name1 + "'s and " + name2 + "'s space overlap"
elif d > r1 and d < r2:
    msg += name1 + " is in " + name2 + "'s personal space\n"
    if r1 + d <= r2:
        msg += name1 + "'s personal space is entirely inside" + name2 + "'s personal space"
    else:
        msg += name1 + "'s and " + name2 + "'s space overlap"
elif d <= r1 + r2:
    msg += "Neither " + name1 + " nor " + name2 + " is in the other's personal space\n"
    msg += name1 + " and " + name2 + "'s personal spaces overlap"
elif d > r1 + r2:
    msg += "Neither " + name1 + " nor " + name2 + " is in the other's personal space\n"
    msg += name1 + " and " + name2 + "'s personal spaces do not overlap"

