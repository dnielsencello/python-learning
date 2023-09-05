from modules.orbian import Orbian
from time import sleep
from random import randint # Hint hint
from random import shuffle # Hint hint


def main():
    print("WELCOME TO ORBIAN FAMILY")
    print()

    family = []
    input("Hit Enter to Create the First Four Orbians")

    for i in range(0, 4):
        name = input("\tEnter a name for Orbian " + str(i) + ": ")
        family.append(Orbian(name)) # Fill in with an anonymous object

    print("\tCreating your Orbian Family", end="")
    thinking()

    done = False

    while not done:
        print()
        print("Menu")
        print("\t1) Meet Orbian Family")
        print("\t2) Compare Orbians")
        print("\t3) Orbian Info")
        print("\t4) Create Orbian Baby")
        print("\t5) Send Orbian to Pasture")
        print("\t6) Orbian Thanos")
        print("\t7) Quit")
        choice = int(input("Choose an option: "))
        print()

        if choice == 1:
            for i in range(len(family)):
                print("I am Orbian ", family[i])
        elif choice == 2:
            cmprOrbian(family)
        elif choice == 3:
            orbianInfo(family)
        
        elif choice == 4:
            newBaby(family)
'''            
        elif choice == 5:
            <Fill-In>
        elif choice == 6:
            <Fill-In> # This function call should return something
        elif choice == 7:
            <Fill-In> # Do not use break

    print("Thanks for playing Orbian Family!!!")
'''
def thinking():
    for i in range(5):
        print(".", end="")
        sleep(0.5)
    print()

def selectOrbian(family, selected=-1):
    for i in range(len(family)):
        print("\t" + str(i + 1) + ") " + family[i].getName(), end="")
        if i == selected:
            print(" (already selected)")
        else:
            print()

    return int(input("Select an Orbian: ")) - 1

def cmprOrbian(family):
    orb1 = selectOrbian(family)
    orb2 = selectOrbian(family, orb1)

    if family[orb1].getVolume() < family[orb2].getVolume():
        print(family[orb2].getName() + " has greater volume than " + family[orb1].getName())
    else:
        print(family[orb1].getName() + " has greater volume than " + family[orb2].getName())

def orbianInfo(family):
    orb = selectOrbian(family)
    print("I am " + family[orb].getAge()) + "zongz old"
    #print("I am ", int(family[orb].getAge())*5, "zongs old")
#Add all required functions below


def newBaby(family):
    orb1 = selectOrbian(family)
    orb2 = selectOrbian(family, orb1)
    headRadius = (family[orb1].getHeadRadius + family[orb2].getHeadRadius)
    bodyHeight = (family[orb1].getBodyHeight + family[orb2].getBodyHeight)
    bodyRadius = (family[orb1].getBodyRadius + family[orb2].getBodyRadius)

    print(headRadius)
    print(bodyHeight)
    print(bodyRadius)

main()