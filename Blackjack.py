#!/bin/python3
import random

"""
    Blackjack
    Written by: lotharthequiet@gmail.com

"""

CARDS = ["Ac","2c","3c","4c","5c","6c","7c","8c","9c","10c","Jc","Qc","Kc","Ad","2d","3d","4d","5d","6d","7d","8d","9d","10d","Jd","Qd","Kd","Ah","2h","3h","4h","5h","6h","7h","8h","9h","10h","Jh","Qh","Kh","As","2s","3s","4s","5s","6s","7s","8s","9s","10s","Js","Qs","Ks",]
PLAYERS = ["Player1","Dealer"]
playerhand = []
dealerhand = []

def shuffle():
    print("Shuffling deck", end="")
    i = 0
    while i <= 6:
        random.shuffle(CARDS)
        if i == 6:
            print(".")
            print("Shuffle completed.")
        else:
            print(".", end="")
        i += 1
    print(CARDS)

def determinehandval(hand):
    handval=0
    for card in hand:
        cardval = determintecardval(card)
        handval = handval + cardval
    return handval

def determintecardval(card):
    cardval = 0   
    if "A" in card:
        print("Ace")
        cardval = 11
    if "2" in card:
        print("Number 2 Card")
        cardval = 2
    if "3" in card:
        print("Number 3 Card")
        cardval = 3
    if "4" in card:
        print("Number 4 Card")
        cardval = 4
    if "5" in card:
        print("Number 5 Card")
        cardval = 5
    if "6" in card:
        print("Number 6 Card")
        cardval = 6
    if "7" in card:
        print("Number 7 Card")
        cardval = 7
    if "8" in card:
        print("Number 8 Card")
        cardval = 8
    if "9" in card:
        print("Number 9 Card")
        cardval = 9
    if "1" in card:
        print("Number 10 Card")
        cardval = 10
    if "J" in card:
        print("Jack")
        cardval = 10
    return cardval 

def dealcards():
    print("Dealing", end="")
    player="Player1"
    i = 0
    while i < 4:
        if player == "Player1":
            playerhand.insert(i, CARDS[i])
            print(".", end="")
            player = "Dealer"
            i += 1
        if player == "Dealer":
            dealerhand.insert(i, CARDS[i])
            print(".", end="")
            player = "Player1"
            i += 1
    print("")
    print("Hands dealt.")

def hit():
    print("Foo")

def stay():
    print("Foo")

def determinewin():
    print("Foo")



def main():
    
    hands = 0
    wins = 0
    losses = 0
    playerresult = 0
    dealerresult = 0
    print("Welcome to Blackjack.")
    input("Press ENTER to continue.")
    shuffle()
    dealcards()
    print(playerhand)
    print(dealerhand)
    hands += 1
    playerresult = determinehandval(playerhand)
    dealerresult = determinehandval(dealerhand)
    if playerresult < 21:
        print("Player1 Hand: ", playerhand, "                             Dealer Hand: ", dealerhand[0]," ", dealerhand[1])
        print("Player1 Val: ", playerresult, "                             Dealer Val: x")
        print("")
        print("Hit or Stay (H or S)?")
        action = input(action)
        if action == "H":
            print("Hit")
        elif action == "S":
            print("Stay")
        else:
            print("Do nothing")
    if playerresult == 21:
        print("Player1 Hand: ", playerhand, "                             Dealer Hand: Xx, Xx")
        print("Player1 Val: ", playerresult, "                             Dealer Val: x")
        print("")
        print("Blackjack! Player 1 Wins!")
        wins += 1
    if playerresult > 21:
        print("Player1 Hand: ", playerhand, "                             Dealer Hand: Xx, Xx")
        print("Player1 Val: ", playerresult, "                             Dealer Val: x")
        print("")
        print("Bust! Player 1 Loses!")
        losses += 1

        
if __name__ == "__main__":
    main()
