from CardCompiler import DataCompile

def ComboCheck(Starting_Hand, Test_Deck):
    Board_Rank = 0
    InterruptionCheck = False

    Hand = []
    Deck = []
    
    for card in Starting_Hand:
        DataCompile(card, card['name'])
        #Hand.append(card['name'])
    
    for card in Test_Deck:
        #Deck.append(card['name'])

    #print(Hand)
    #print(Deck)

    #Interruption Cards Like Hand Traps or Called by the Grave, add more checks to this list if you run other hand traps
    if 'Infinite Impermanence' in Starting_Hand or '"Called by the Grave"' in Starting_Hand or 'Ash Blossom & Joyous Spring' in Starting_Hand or 'Effect Veiler' in Starting_Hand:
        InterruptionCheck = True

    #Combos, checks if certain combinations of cards are present in your starting hand
    if 'Union Hangar' in Starting_Hand and 'Union Driver' in deck and Board_Rank < 3:
        Board_Rank = 3
    if 'Union Hangar' in Hand and 'Union Driver' in Deck:
        print('Yes')

    return Board_Rank, InterruptionCheck