# David Nielsen
# CS1400 - I01
# Unit 5 task 3

from modules.bobinator import Bobinator

def main():
    print("Welcome to the Bobinator")
    name1 = input("Enter the first name: ")
    age1 = int(input("Enter the first age: "))
    name2 = input("Enter the second name: ")
    age2 = int(input("Enter the second age: "))

    bobinator1 = Bobinator(name1, age1)
    bobinator2 = Bobinator(name2, age2)

    done = False

    while not done:
        print()
        print("Menu")
        print("\t1) First Bob")
        print("\t2) Big Bob")
        print("\t3) Little Bob")
        print("\t4) Bob Factor")
        print("\t5) Mix Bobs")
        print("\t6) Middle Bob")
        print("\t7) Back Bob Sliced")
        print("\t8) Back Bob Manual")
        print("\t9) Quit")
        mode = int(input("Enter Selection: "))
        print()

        if mode == 1:
            firstBob(bobinator1, bobinator2)
        elif mode == 2:
            bigBob(bobinator1, bobinator2)
        elif mode == 3:
            littleBob(bobinator1, bobinator2)
        elif mode == 4:
            bobFactor(bobinator1, bobinator2)
        elif mode == 5:
            mixBob(bobinator1, bobinator2)
        elif mode == 6:
            midBob(bobinator1, bobinator2)
        elif mode == 7:
            backBobSlice(bobinator1, bobinator2)
        elif mode == 8:
            backBobManual(bobinator1, bobinator2)
        elif mode == 9:
            done = True

def firstBob(bobinator1, bobinator2):
    print("The first Bob is", min(bobinator1, bobinator2))

def bigBob(bobinator1, bobinator2):
    bob = bobinator1 + bobinator2
    print("The Big Bob is", bob)
    print("Data type:", type(bob))

def littleBob(bobinator1, bobinator2):
    bob = bobinator1 - bobinator2
    print("The Little Bob is", bob)
    print("Data type:", type(bob))

def bobFactor(bobinator1, bobinator2):
    factor = int(input("Enter an integer factor: "))
    bob1 = bobinator1 * factor
    bob2 = bobinator2 * factor
    print("Bob factor one is", bob1)
    print("Bob factor two is", bob2)
    print("Data type:", type(bob1), type(bob2))

def mixBob(bobinator1, bobinator2):
    bob = bobinator1 / bobinator2
    print("The mixed bob is", bobinator1 / bobinator2)
    print("Data type:", type(bob))

def midBob(bobinator1, bobinator2):
    bob = bobinator1 % bobinator2
    print("Midbob is", bob)
    print("Data type:", type(bob))

def backBobSlice(bobinator1, bobinator2):
    bob1 = bobinator1.backBobSlice()
    bob2 = bobinator2.backBobSlice()
    print("Back Bob Slice one is", bob1)
    print("Back Bob Slice two is", bob2)
    print("Data type:", type(bob1), type(bob2))

def backBobManual(bobinator1, bobinator2):
    bob1 = bobinator1.backBobManual()
    bob2 = bobinator2.backBobManual()
    print("Back Bob Slice one is", bob1)
    print("Back Bob Slice two is", bob2)
    print("Data type:", type(bob1), type(bob2))


main()