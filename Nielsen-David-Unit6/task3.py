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
        playerHand.append(deck.draw()) # Single line

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
            sortbytitle(playerHand) # Single line
        elif choice == 3:
            sortByGang(playerHand) # Single line
        elif choice == 4:
            searchCard(playerHand) # Single line
        elif choice == 5:
            print('Thank you for playing')
            done = True
            # Not a function and not 'break'

def thinking():
    for i in range(5):
        print(".", end="")
        sleep(0.5)
    print()

def displayHand(hand):
    for i in hand:
        print(i)

# Add other functions you need below

def sortbytitle(hand):
    print("Selection sort by title", end = "")
    thinking()

    for i in range(len(hand)):
        minIndex = i
        for j in range(i + 1, len(hand)):
            if TITLE.index(hand[minIndex].getTitle()) > TITLE.index(hand[j].getTitle()):
                minIndex = j
        if minIndex != 1:
            hand[i], hand[minIndex] = hand[minIndex], hand[i]

def sortByGang(hand):
    print('Insertion sort by gang', end = "")
    thinking()

    for i in range(len(hand)):
        curIndex = i
        for j in range(1, len(hand)):
            curIndex = hand[i]
            j = i -1
            while j >= 0 and GANG.index(hand[j].getGang()) > GANG.index(curIndex.getGang()):
                hand[j + 1] = hand[j]
                j -= 1

            hand[j + 1] = curIndex


def searchCard(hand):

    sortByGang(hand)
    for i in TITLE:
        print("(" + str(TITLE.index(i) + 1) + ") " + i)
    cardTitle = TITLE[int(input("select a card title: "))- 1]
    for i in GANG:
        print("(" + str(GANG.index(i) + 1) + ") " + i)
    cardGang = GANG[int(input("select a card gang: ")) - 1]

    key = convertCardToId(cardTitle, cardGang)

    count = 0
    low = 0
    mid = 0
    high = len(hand) - 1
    while high >= low:
        count += 1
        mid = (high + low) // 2
        print(hand[mid].getID())
        if key == hand[mid].getID():
            print('The card is in the hand')
            break
        elif key < hand[mid].getID():
            high = mid - 1
        else:
            low = mid + 1
    if key != hand[mid].getID():
        print('The card is not in the hand')
    return -1

main()