# -*- coding: utf-8 -*-
"""
Created on Thu Jul 23 20:25:01 2020

@author: jpalm
"""
Player_Turn = 1 #Input 1 for first, 2 for second

Trials = 10000 #Input the number of test hands you want to run at once
End_Board = [] #sets up the end board list
Interruptions = [] #sets up the list for hand traps or set cards
import random #for the randomizer

for x in range(Trials): #runs all the code within this for loop, for the set numbber of trials specified

    Starting_Hand = []
    
    Board_Rank = 0
    
    
    #cards in deck, to change it just replace the given cards, or add more for up to a 60 card deck
    Card_1 = "A-Assault Core"
    Card_2 = "A-Assault Core"
    Card_3 = "A-Assault Core"
    Card_4 = "B-Buster Drake"
    Card_5 = "B-Buster Drake"
    Card_6 = "B-Buster Drake"
    Card_7 = "C-Crush Wyvern"
    Card_8 = "C-Crush Wyvern"
    Card_9 = "C-Crush Wyvern"
    Card_10 = "Union Driver"
    Card_11 = "Union Driver"
    Card_12 = "Galaxy Soldier"
    Card_13 = "Galaxy Soldier"
    Card_14 = "Galaxy Soldier"
    Card_15 = "Ash Blossom & Joyous Spring"
    Card_16 = "Ash Blossom & Joyous Spring"
    Card_17 = "Ash Blossom & Joyous Spring"
    Card_18 = "Effect Veiler"
    Card_19 = "Effect Veiler"
    Card_20 = "Effect Veiler"
    Card_21 = "Photon Orbital"
    Card_22 = "Union Hangar"
    Card_23 = "Union Hangar"
    Card_24 = "Union Hangar"
    Card_25 = "Union Hangar" #This is Terraforming
    Card_26 = "Union Hangar" #This is Set Rotation
    Card_27 = "Mystic Mine"
    Card_28 = "Cynet Universe"
    Card_29 = "Unauthorized Reactivation"
    Card_30 = "Unauthorized Reactivation"
    Card_31 = "Unauthorized Reactivation"
    Card_32 = "Photon Sanctuary"
    Card_33 = "Photon Sanctuary"
    Card_34 = "Photon Sanctuary"
    Card_35 = "Called by the Grave"
    Card_36 = "Called by the Grave"
    Card_37 = "Called by the Grave"
    Card_38 = "Infinite Impermanence"
    Card_39 = "Infinite Impermanence"
    Card_40 = "Infinite Impermanence"
    #If you're playing upstart, comment out Card_40
    
    #If you add more cards, make sure the coresponding card numbers are present in this deck list (get it, its literally a deck list... ha...)
    Deck_List = [Card_1, Card_2, Card_3, Card_4, Card_5, Card_6,Card_7,Card_8,Card_9,
                 Card_10, Card_11,Card_12,Card_13,Card_14,Card_15,Card_16,Card_17,Card_18,Card_19,Card_20,
                 Card_21,Card_22,Card_23,Card_24,Card_25,Card_26,Card_27,Card_28,Card_29,Card_30,Card_31,
                 Card_32,Card_33,Card_34,Card_35,Card_36,Card_37,Card_38,Card_39,Card_40] # Delete Card_40 if you're playing upstart.
    Deck_Length = len(Deck_List)
    
    #sets the starting hand size
    if Player_Turn == 1:
        Cards_Drawn = 5
    else:
        Cards_Drawn = 6
     
    #randomly adds cards for your Starting_Hand and removes them from the Deck_List as you draw them
    for x in range (Cards_Drawn):
        Draw = random.choice(Deck_List)
        Deck_List.remove(Draw)
        Starting_Hand.append(Draw)
    
    
    'print(Starting_Hand)' #uncomment to debug or to test specific starting hands
    
    #Interruption Cards Like Hand Traps or Called by the Grave, add more checks to this list if you run other hand traps
    if 'Infinite Impermanence' in Starting_Hand or '"Called by the Grave"' in Starting_Hand or 'Ash Blossom & Joyous Spring' in Starting_Hand or 'Effect Veiler' in Starting_Hand:
        Interruptions.append(1)
   
    #Combos, checks if certain combinations of cards are present in your starting hand
    if 'Union Hangar' in Starting_Hand and Board_Rank < 3:
        Board_Rank = 3
    if 'Unauthorized Reactivation' in Starting_Hand and 'A-Assault Core' in Starting_Hand and Board_Rank < 3:
        Board_Rank = 3
    if 'Unauthorized Reactivation' in Starting_Hand and 'B-Buster Drake' in Starting_Hand and Board_Rank < 3:
        Board_Rank = 3
    if 'Unauthorized Reactivation' in Starting_Hand and 'C-Crush Wyvern' in Starting_Hand and Board_Rank < 1:
        Board_Rank = 1
    if 'Galaxy Soldier' in Starting_Hand and 'B-Buster Drake' in Starting_Hand and 'A-Assault Core' in Starting_Hand and Board_Rank < 2:
        Board_Rank = 2
    if 'Galaxy Soldier' in Starting_Hand and 'B-Buster Drake' in Starting_Hand and 'C-Crush Wyvern' in Starting_Hand and Board_Rank < 2:
        Board_Rank = 2
    if 'B-Buster Drake' in Starting_Hand and 'Photon Sanctuary' in Starting_Hand and Board_Rank < 1:
        Board_Rank = 1
    if 'Galaxy Soldier' in Starting_Hand
    End_Board.append(Board_Rank) #adds the rank of the best possible board you can make with your starting hand to the End_Board list


my_dict = {i:End_Board.count(i) for i in End_Board} #shows the entire numerical breakdown

Bricked = (End_Board.count(0) / Trials) * 100 #a rank of 0 means you bricked and have no combo
Rank_half_Board = (End_Board.count(0.5) / Trials) * 100 #a rank of 0.5 means ou have partial combo, no Buster dragon, but you can end on Infinity, or IP
Rank_1_Board = (End_Board.count(1) / Trials) * 100 #a rank of 1 means you have a combo, you end on at least buster dragon
Rank_2_Board = (End_Board.count(2) / Trials) * 100 #a rank of 2 means you end on a good combo, at least Buster dragon + IP, Buster + Blocker + DSword, etc
Rank_3_Board = (End_Board.count(3) / Trials) * 100 #a rank 3 combo means you end on a great combo, at least, Buster + Infinity + IP, or Buster + IP + Dsword, etc

Interruption_Count = (Interruptions.count(1) / Trials) * 100 #the number of hands that have an interuption (a hand trap or set card)

'print(End_Board)' #un comment if you want to see every number in the list
print(my_dict)
print(Bricked, "% Bricked")
print(Rank_half_Board, "% Rank 0.5 Board")
print(Rank_1_Board, "% Rank 1 Board")
print(Rank_2_Board, "% Rank 2 Board")
print(Rank_3_Board, "% Rank 3 Board")
print(Interruption_Count, "% With Set Card")
