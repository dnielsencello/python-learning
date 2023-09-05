from modules.deck import Deck
from time import sleep
from modules.gronkyutil import convertCardToId
from modules.gronkyutil import TITLE, GANG

def main():
    print("Welcome to Gronky Cards\n")
    print("Shuffling Cards", end="")
    thinking()

    deck = Deck()
    playerHand = []

    cardCount = int(input("How many cards would you like?: "))

    for i in range(cardCount):
        playerHand.append(deck.draw())

    done = False
    while not done:
        print()
        print("Menu")
        print("\t(1) Display hand")
        print("\t(2) Sort by title")
        print("\t(3) Sort by gang")
        print("\t(4) Search for card")
        print("\t(5) Quit")
        choice = int(input("Choose an option: "))
        print()

        if choice == 1:
            displayHand(playerHand)
        elif choice == 2:
            sortTitle(playerHand)
        elif choice == 3:
            sortGang(playerHand)
        elif choice == 4:
            srchCard(playerHand)
        elif choice == 5:
            print("Thank you for playing")
            done = True

def thinking():
    for i in range(5):
        print(".", end="")
        sleep(0.5)
    print()

def displayHand(hand):
   for i in range(len(hand)):
       print(hand[i])

def sortTitle(hand): #selectionsort
    print("Selection sort by title", end="")
    thinking()
    for i in range(len(hand)-1):
        currMinIndex = i

        for j in range(i + 1, len(hand)):
            if TITLE.index(hand[currMinIndex]).getTitle() > TITLE.index(hand[j]).getTitle():
                currMinIndex = j

        if currMinIndex != i:
            hand[i], hand[currMinIndex] = hand[currMinIndex], hand[i]

def sortGang(hand): #insertion sort
    print("Insertion sort by gang", end="")
    thinking()
    for i in range(1, len(hand)):
        currElement = hand[i]
        j = i - 1
        while j >= 0 and GANG.index(hand[j].getGang()) > GANG.index(currElement.getGang()):
            hand[j + 1] = hand[j]
            j -= 1

        hand[j + 1] = currElement

def srchCard(hand):

    sortGang(hand)
    for i in range(len(TITLE)):
        print("("+ str(i+1) +")", TITLE[i])

    cardTitle = TITLE[int(input("select a card title: "))-1]

    for i in range(len(GANG)):
        print("("+ str(i+1)+")", GANG[i])

    cardGang = GANG[int(input("select a card gang: "))-1]

    key = convertCardToId(cardTitle, cardGang)

    count = 0
    low = 0
    high = len(hand) - 1
    while high >= low:
        count += 1
        mid = (high + low) // 2
        print(hand[mid].getID())
        if key == hand[mid].getID():
            print("The card is in the hand ")
            return mid
        elif key < hand[mid].getID():
            high = mid - 1
        else:
            low = mid + 1
    #print("The card is not in the hand")
    return -1

#compare ids using binary search





main()