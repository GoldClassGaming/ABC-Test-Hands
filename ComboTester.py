import random #xeo added a comment for repo testing purposes
from Combos import *
from DrawCards import *

#Shuffles deck
def shuffle(deck):
    random.shuffle(deck)

#Draws 5 cards
def draw(deck, n):
    hand = []
    for i in range(n):
        hand.append(deck.pop(0))
    return hand

# Checks whehter a given hand is capable of performing any of the preset combos
def combo(deck, n):
    End_Board = [] #sets up the end board list
    Interruptions = [] #sets up the final list for hand traps or set cards
    DesiresHands = 0
    for i in range(0, 1):
        test_deck = deck.copy()
        shuffle(test_deck)
        test_hand = draw(test_deck, 5)
        #Everything Below This and The Majority of Combos.py needs to be rewritten to match new card data formatting and to match new hand scoring system
        Results = ComboCheck(test_hand, test_deck)
        Hand_Strength = Results[0]
        if 'Upstart Goblin' in test_hand and Hand_Strength < 2:
          Results = Upstart(test_hand, test_deck)
          Hand_Strength = Results[0]
        if 'Pot of Desires' in test_hand and Hand_Strength < 1:
          DesiresHands += 1
          Results = Desires(test_hand, test_deck)
          Hand_Strength = Results[0]
        if Results[1] == True:
          Interruptions.append(1)
        End_Board.append(Hand_Strength) #adds the rank of the best possible board you can make with your starting hand to the End_Board list
    
    my_dict = {i:End_Board.count(i) for i in End_Board} #shows the entire numerical breakdown

    Bricked = (End_Board.count(0) / n) * 100 #a rank of 0 means you bricked and have no combo
    Rank_half_Board = (End_Board.count(0.5) / n) * 100 #a rank of 0.5 means ou have partial combo, no Buster dragon, but you can end on Infinity, or IP
    Rank_1_Board = (End_Board.count(1) / n) * 100 #a rank of 1 means you have a combo, you end on at least buster dragon
    Rank_2_Board = (End_Board.count(2) / n) * 100 #a rank of 2 means you end on a good combo, at least Buster dragon + IP, Buster + Blocker + DSword, etc
    Rank_3_Board = (End_Board.count(3) / n) * 100 #a rank 3 combo means you end on a great combo, at least, Buster + Infinity + IP, or Buster + IP + Dsword, etc

    Interruption_Count = (Interruptions.count(1) / n) * 100 #the number of hands that have an interuption (a hand trap or set card)

    'print(End_Board)' #un comment if you want to see every number in the list
    print(' ')
    print(my_dict)
    print(' ')
    print(Bricked, "% Bricked")
    print(Rank_half_Board, "% Rank 0.5 Board")
    print(Rank_1_Board, "% Rank 1 Board")
    print(Rank_2_Board, "% Rank 2 Board")
    print(Rank_3_Board, "% Rank 3 Board")
    print(' ')
    print(Interruption_Count, "% With Set Card")
    print(' ')
    print(f'{n} Test Hands Simulated')
    print(f'{DesiresHands} Hands resolved Pot of Desires')