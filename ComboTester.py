import random
from Combos import *

#Shuffles deck
def shuffle(deck):
    random.shuffle(deck)

#Draws 5 cards
def draw(deck, n):
    hand = []
    test_deck = deck.copy()
    shuffle(test_deck)
    for i in range(n):
        hand.append(test_deck.pop(0))
    return hand

# Checks whehter a given hand is capable of performing any of the preset combos
def combo(deck, n):
    End_Board = [] #sets up the end board list
    Interruptions = [] #sets up the final list for hand traps or set cards
    for i in range(0, n):
        test_hand = draw(deck, 5))
        shuffle(deck)
        Results = ComboCheck(test_hand, deck)
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
    print(my_dict)
    print(Bricked, "% Bricked")
    print(Rank_half_Board, "% Rank 0.5 Board")
    print(Rank_1_Board, "% Rank 1 Board")
    print(Rank_2_Board, "% Rank 2 Board")
    print(Rank_3_Board, "% Rank 3 Board")
    print(Interruption_Count, "% With Set Card")
    print(f'{n} Test Hands Simulated')