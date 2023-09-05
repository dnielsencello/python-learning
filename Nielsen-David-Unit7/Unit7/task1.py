from deck import Deck
from card import Card
import time

def main():
    # input the number of players
    players = eval(input("How many players?: "))
    # Create list for the starting account ammounts of $100
    account = []
    for i in range(players + 1):
        account.append(100)
    # make sure play continues until game play is over
    done = False
    while done == False:
        # create deck and lists
        deck1 = Deck()
        # card list
        lst1 = []
        # bet amount
        lst2 = []
        # card total list
        lst3 = []

        for i in range(players + 1):
            lst3.append(0)
            lst1.append([])
            # allow users to input bet amount unless they have no money
            if i != players and account[i] > 0:
                print(account[i])
                betamount = eval(input("Player " + str(i + 1) + " has $" + str(account[i]) + ". How much is Player " + str(i + 1) + " going to bet: "))

                if (account[i] > 5 and betamount > 5) or account[i] < 5:
                    lst2.append(betamount)
                elif account[i] <= 0:
                    print("You cannot place a bet")
                    lst2.append(betamount)
                # ensure users input a good bet
                elif betamount < 5:
                    betamount = eval(input("The minimum bet is $5 and/or less than your remaining balance. Please enter a proper bet: "))
                    lst2.append(betamount)

            else:
                lst2.append(0)

            # deal players and the dealer their first two cards
            for p in range(2):
                if i == players:
                    lst2.append(0)
                    lst1[i].append(deck1.draw())
                    gloppy = lst3[i]
                    floppy = lst1[i][p].getCardValue()
                    lst3[i] += cardVal(floppy, gloppy)

                elif account[i] > 0:
                    lst1[i].append(deck1.draw())
                    gloppy = lst3[i]
                    floppy = lst1[i][p].getCardValue()
                    lst3[i] += cardVal(floppy, gloppy)

                else:
                    lst1[i].append(0)


        print("The dealer's second card is  " + str(lst1[players][1]))

        # show player their hand, allow them to add to their hand
        for i in range(players):
            if account[i] > 0:
                hold = False
                while hold == False:
                    print("This is Player " + str(i+1) + "'s hand:" + str(lst1[i]))

                    print("(1) Hit \n(2) Hold ")
                    play = eval(input("Hit or hold?: "))
                    if play == 1:
                        lst1[i].append(deck1.draw())
                        gloppy = lst3[i]
                        floppy = lst1[i][len(lst1[i]) - 1].getCardValue()
                        lst3[i] += cardVal(floppy, gloppy)
                        if lst3[i] > 21:
                            print("This is Player " + str(i + 1) + "'s hand:" + str(lst1[i]))
                            print("Bust! You lose")
                            hold = True
                    elif play == 2:
                        hold = True
        #show players the dealers hand
        print("This is the dealers hand:")
        time.sleep(2)
        print(str(lst1[players][0]))
        time.sleep(1)
        print(str(lst1[players][1]))

        i = 1
        # if the dealers hand ammount is less than 17 they pick another card
        while lst3[players] < 17:
            print("The dealer will draw another card")
            i += 1
            lst1[players].append(deck1.draw())
            gloppy = lst3[players]
            floppy = lst1[players][len(lst1[players])-1].getCardValue()
            lst3[players] += cardVal(floppy, gloppy)
            time.sleep(3)
            print(lst1[players][i])
            time.sleep(2)
        time.sleep(2)
        print("The dealer holds")

        # compute the results of the game if the dealer busts
        if lst3[players] > 21:
            print("The dealer busted")
            for p in range(len(lst3)-1):
                if lst3[p] < 21:
                    print("Player " + str(p+1) + " has won $" + str(lst2[p])  + " and has $" + str(account[p] + lst2[p]))
                    account[p] = account[p] + lst2[p]
                else:
                    print("Player " + str(p+1) + " has lost $" + str(lst2[p]) + " and has $" + str(account[p] - lst2[p]))
                    account[p] = account[p] - lst2[p]

        # compute the results of the game if the dealer doesn't bust
        if lst3[players] <= 21:
            for p in range(len(lst3)-1):
                if lst3[p] < lst3[players]:
                    print("Player " + str(p+1) + " has lost $" + str(lst2[p]) + " and has $" + str(account[p] - lst2[p]))
                    account[p] = account[p] - lst2[p]
                elif lst3[p] > lst3[players] and lst3[p] <= 21:
                    print("Player " + str(p+1) + " has won $" + str(lst2[p]) + " and has $" + str(account[p] + lst2[p]))
                    account[p] = account[p] + lst2[p]
                elif lst3[p] == lst3[players]:
                    print("Player " + str(p+1) + " broke even and has $" + str(account[p]))
                    account[p] += 0
                else:
                    print("Player " + str(p+1) + " has lost $" + str(lst2[p]) + " and has $" + str(account[p] - lst2[p]))
                    account[p] = account[p] - lst2[p]
        print("(1) Yes\n(2) No")
        cont = eval(input("Would you like to play another round: "))

        if cont == 1:
            continue
        else:
            done = True
        account.pop()
        pllst = []
        sortList(account, pllst)


# sort and the print players in order of winnings to loses
def sortList(account, pllst):
    didSwap = True

    while didSwap:
        didSwap = False
        sortCnt = 1

        for i in range(len(account)):
            pllst.append(i + 1)
        for i in range(len(account) - sortCnt):
            if account[i] < account[i + 1]:
                account[i], account[i+1] = account[i+1], account[i]
                pllst[i], pllst[i + 1] = pllst[i + 1], pllst[i]
                didSwap = True

        sortCnt += 1

    for i in range(len(account)):
        print("Player " + str(pllst[i]) + " goes home with $" + str(account[i]))

# calculate card value to add to each players hand
def cardVal(floppy, gloppy):
    # returns value for non face value cards
    if floppy > 1 and floppy < 11:
        return floppy
    # returns a 10 for face value cards
    elif floppy >= 11:
        return 10
    # returns value of an ace with special conditions.
    if floppy == 1:
        if floppy + gloppy > 21:
            return 1
        else:
            return 11


main()