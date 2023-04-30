#!/bin/python3
import random

"""
    Blackjack
    Written by: lotharthequiet@gmail.com

"""

CARDS = ["Ac","2c","3c","4c","5c","6c","7c","8c","9c","10c","Jc","Qc","Kc","Ad","2d","3d","4d","5d","6d","7d","8d","9d","10d","Jd","Qd","Kd","Ah","2h","3h","4h","5h","6h","7h","8h","9h","10h","Jh","Qh","Kh","As","2s","3s","4s","5s","6s","7s","8s","9s","10s","Js","Qs","Ks",]
PLAYERS = ["Player1","Dealer"]
PLAYERHAND = []
DEALERHAND = []
WINS = 0
LOSSES = 0
PLAYERRESULT = 0
DEALERRESULT = 0

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

def gethandval(hand):
    handval=0
    for card in hand:
        cardval = getcardval(card)
        handval = handval + cardval
    return handval

def getcardval(card):
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
    if "Q" in card:
        print("Queen")
        cardval = 10
    if "K" in card:
        print("King")
        cardval = 10
    return cardval 

def dealcards():
    print("Dealing", end="")
    player=PLAYERS[0]
    i = 0
    while i < 4:
        if player == "Player1":
            PLAYERHAND.insert(i, CARDS[0])
            CARDS.pop(0)
            print(".", end="")
            player = "Dealer"
            i += 1
        if player == "Dealer":
            DEALERHAND.insert(i, CARDS[0])
            CARDS.pop(0)
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
    HANDCOUNT = 0
    print("Welcome to Blackjack.")
    input("Press ENTER to continue.")
    shuffle()
    dealcards()
    print(PLAYERHAND)
    print(DEALERHAND)
    HANDCOUNT += 1
    PLAYERRESULT = gethandval(PLAYERHAND)
    DEALERRESULT = gethandval(DEALERHAND)
    if PLAYERRESULT < 21:
        print("Player1 Hand: ", PLAYERHAND, "                             Dealer Hand: ", DEALERHAND[0]," ", DEALERHAND[1])
        print("Player1 Val: ", PLAYERRESULT, "                             Dealer Val: x")
        print("")
        print("Hit or Stay (H or S)?")
        action = input(action)
        if action == "H":
            print("Hit")
        elif action == "S":
            print("Stay")
        else:
            print("Do nothing")
    if PLAYERRESULT == 21:
        print("Player1 Hand: ", PLAYERHAND, "                             Dealer Hand: Xx, Xx")
        print("Player1 Val: ", PLAYERRESULT, "                             Dealer Val: x")
        print("")
        print("Blackjack! Player 1 Wins!")
        WINS += 1
    if PLAYERRESULT > 21:
        print("Player1 Hand: ", PLAYERHAND, "                             Dealer Hand: Xx, Xx")
        print("Player1 Val: ", PLAYERRESULT, "                             Dealer Val: x")
        print("")
        print("Bust! Player 1 Loses!")
        LOSSES += 1
  
if __name__ == "__main__":
    main()
