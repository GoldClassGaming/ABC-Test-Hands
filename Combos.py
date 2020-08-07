

def ComboCheck(Starting_Hand, deck):
    Board_Rank = 0
    InterruptionCheck = False
    
    #Interruption Cards Like Hand Traps or Called by the Grave, add more checks to this list if you run other hand traps
    if 'Infinite Impermanence' in Starting_Hand or '"Called by the Grave"' in Starting_Hand or 'Ash Blossom & Joyous Spring' in Starting_Hand or 'Effect Veiler' in Starting_Hand:
        InterruptionCheck = True

    #Combos, checks if certain combinations of cards are present in your starting hand

    # 1 Card Combos
    # Tier 3
    if 'Union Hangar' in Starting_Hand and 'Union Driver' in deck and Board_Rank < 3:
        Board_Rank = 3
    if 'Terraforming' in Starting_Hand and 'Union Driver' in deck and Board_Rank < 3:
        Board_Rank = 3
    if 'Set Rotation' in Starting_Hand and 'Mystic Mine' in deck and 'Union Driver' in deck and Board_Rank < 3:
        Board_Rank = 3
    if 'Set Rotation' in Starting_Hand and 'Cynet Universe' in deck and 'Union Driver' in deck and Board_Rank < 3:
        Board_Rank = 3
    # Tier 2

    # Tier 1

    # Tier 0.5

    # 2 Card Combos
    # Tier 3
    if 'Unauthorized Reactivation' in Starting_Hand and 'A-Assault Core' in Starting_Hand and Board_Rank < 3:
        Board_Rank = 3
    if 'Unauthorized Reactivation' in Starting_Hand and 'B-Buster Drake' in Starting_Hand and Board_Rank < 3:
        Board_Rank = 3
    # Tier 2

    # Tier 1
    if 'Unauthorized Reactivation' in Starting_Hand and 'C-Crush Wyvern' in Starting_Hand and Board_Rank < 1:
        Board_Rank = 1
    if 'B-Buster Drake' in Starting_Hand and 'Photon Sanctuary' in Starting_Hand and Board_Rank < 1:
        Board_Rank = 1
    # Tier 0.5

    # 3+ Card Combos
    # Tier 3

    # Tier 2
    if 'Galaxy Soldier' in Starting_Hand and 'B-Buster Drake' in Starting_Hand and 'A-Assault Core' in Starting_Hand and Board_Rank < 2:
        Board_Rank = 2
    if 'Galaxy Soldier' in Starting_Hand and 'B-Buster Drake' in Starting_Hand and 'C-Crush Wyvern' in Starting_Hand and Board_Rank < 2:
        Board_Rank = 2
    # Tier 1

    # Tier 0.5
    if 'Galaxy Soldier' in Starting_Hand and 'A-Assault Core' in Starting_Hand and 'A-Assault Core' in Starting_Hand and Board_Rank < 0.5:
        Board_Rank = 0.5
    if 'Galaxy Soldier' in Starting_Hand and 'A-Assault Core' in Starting_Hand and 'B-Buster Drake' in Starting_Hand and Board_Rank < 0.5:
        Board_Rank = 0.5
    if 'Galaxy Soldier' in Starting_Hand and 'A-Assault Core' in Starting_Hand and 'C-Crush Wyvern' in Starting_Hand and Board_Rank < 0.5:
        Board_Rank = 0.5
    if 'Galaxy Soldier' in Starting_Hand and 'A-Assault Core' in Starting_Hand and 'Effect Veiler' in Starting_Hand and Board_Rank < 0.5:
        Board_Rank = 0.5
    if 'Galaxy Soldier' in Starting_Hand and 'A-Assault Core' in Starting_Hand and 'Union Driver' in Starting_Hand and Board_Rank < 0.5:
        Board_Rank = 0.5
    if 'Galaxy Soldier' in Starting_Hand and 'B-Buster Drake' in Starting_Hand and 'A-Assault Core' in Starting_Hand and Board_Rank < 0.5:
        Board_Rank = 0.5
    if 'Galaxy Soldier' in Starting_Hand and 'B-Buster Drake' in Starting_Hand and 'B-Buster Drake' in Starting_Hand and Board_Rank < 0.5:
        Board_Rank = 0.5
    if 'Galaxy Soldier' in Starting_Hand and 'B-Buster Drake' in Starting_Hand and 'C-Crush Wyvern' in Starting_Hand and Board_Rank < 0.5:
        Board_Rank = 0.5
    if 'Galaxy Soldier' in Starting_Hand and 'B-Buster Drake' in Starting_Hand and 'Effect Veiler' in Starting_Hand and Board_Rank < 0.5:
        Board_Rank = 0.5
    if 'Galaxy Soldier' in Starting_Hand and 'B-Buster Drake' in Starting_Hand and 'Union Driver' in Starting_Hand and Board_Rank < 0.5:
        Board_Rank = 0.5
    if 'Galaxy Soldier' in Starting_Hand and 'C-Crush Wyvern' in Starting_Hand and 'A-Assault Core' in Starting_Hand and Board_Rank < 0.5:
        Board_Rank = 0.5
    if 'Galaxy Soldier' in Starting_Hand and 'C-Crush Wyvern' in Starting_Hand and 'B-Buster Drake' in Starting_Hand and Board_Rank < 0.5:
        Board_Rank = 0.5
    if 'Galaxy Soldier' in Starting_Hand and 'C-Crush Wyvern' in Starting_Hand and 'C-Crush Wyvern' in Starting_Hand and Board_Rank < 0.5:
        Board_Rank = 0.5
    if 'Galaxy Soldier' in Starting_Hand and 'C-Crush Wyvern' in Starting_Hand and 'Effect Veiler' in Starting_Hand and Board_Rank < 0.5:
        Board_Rank = 0.5
    if 'Galaxy Soldier' in Starting_Hand and 'C-Crush Wyvern' in Starting_Hand and 'Union Driver' in Starting_Hand and Board_Rank < 0.5:
        Board_Rank = 0.5
    if 'Galaxy Soldier' in Starting_Hand and 'Effect Veiler' in Starting_Hand and 'A-Assault Core' in Starting_Hand and Board_Rank < 0.5:
        Board_Rank = 0.5
    if 'Galaxy Soldier' in Starting_Hand and 'Effect Veiler' in Starting_Hand and 'B-Buster Drake' in Starting_Hand and Board_Rank < 0.5:
        Board_Rank = 0.5
    if 'Galaxy Soldier' in Starting_Hand and 'Effect Veiler' in Starting_Hand and 'C-Crush Wyvern' in Starting_Hand and Board_Rank < 0.5:
        Board_Rank = 0.5
    if 'Galaxy Soldier' in Starting_Hand and 'Effect Veiler' in Starting_Hand and 'Effect Veiler' in Starting_Hand and Board_Rank < 0.5:
        Board_Rank = 0.5
    if 'Galaxy Soldier' in Starting_Hand and 'Effect Veiler' in Starting_Hand and 'Union Driver' in Starting_Hand and Board_Rank < 0.5:
        Board_Rank = 0.5
    if 'Galaxy Soldier' in Starting_Hand and 'Union Driver' in Starting_Hand and 'A-Assault Core' in Starting_Hand and Board_Rank < 0.5:
        Board_Rank = 0.5
    if 'Galaxy Soldier' in Starting_Hand and 'Union Driver' in Starting_Hand and 'B-Buster Drake' in Starting_Hand and Board_Rank < 0.5:
        Board_Rank = 0.5
    if 'Galaxy Soldier' in Starting_Hand and 'Union Driver' in Starting_Hand and 'C-Crush Wyvern' in Starting_Hand and Board_Rank < 0.5:
        Board_Rank = 0.5
    if 'Galaxy Soldier' in Starting_Hand and 'Union Driver' in Starting_Hand and 'Effect Veiler' in Starting_Hand and Board_Rank < 0.5:
        Board_Rank = 0.5
    if 'Galaxy Soldier' in Starting_Hand and 'Union Driver' in Starting_Hand and 'Union Driver' in Starting_Hand and Board_Rank < 0.5:
        Board_Rank = 0.5
    if 'Photon Sanctuary' in Starting_Hand and 'A-Assault Core' in Starting_Hand and 'A-Assault Core' in Starting_Hand and Board_Rank < 0.5:
        Board_Rank = 0.5
    if 'Photon Sanctuary' in Starting_Hand and 'A-Assault Core' in Starting_Hand and 'B-Buster Drake' in Starting_Hand and Board_Rank < 0.5:
        Board_Rank = 0.5
    if 'Photon Sanctuary' in Starting_Hand and 'A-Assault Core' in Starting_Hand and 'C-Crush Wyvern' in Starting_Hand and Board_Rank < 0.5:
        Board_Rank = 0.5
    if 'Photon Sanctuary' in Starting_Hand and 'A-Assault Core' in Starting_Hand and 'Effect Veiler' in Starting_Hand and Board_Rank < 0.5:
        Board_Rank = 0.5
    if 'Photon Sanctuary' in Starting_Hand and 'A-Assault Core' in Starting_Hand and 'Union Driver' in Starting_Hand and Board_Rank < 0.5:
        Board_Rank = 0.5
    if 'Photon Sanctuary' in Starting_Hand and 'B-Buster Drake' in Starting_Hand and 'A-Assault Core' in Starting_Hand and Board_Rank < 0.5:
        Board_Rank = 0.5
    if 'Photon Sanctuary' in Starting_Hand and 'B-Buster Drake' in Starting_Hand and 'B-Buster Drake' in Starting_Hand and Board_Rank < 0.5:
        Board_Rank = 0.5
    if 'Photon Sanctuary' in Starting_Hand and 'B-Buster Drake' in Starting_Hand and 'C-Crush Wyvern' in Starting_Hand and Board_Rank < 0.5:
        Board_Rank = 0.5
    if 'Photon Sanctuary' in Starting_Hand and 'B-Buster Drake' in Starting_Hand and 'Effect Veiler' in Starting_Hand and Board_Rank < 0.5:
        Board_Rank = 0.5
    if 'Photon Sanctuary' in Starting_Hand and 'B-Buster Drake' in Starting_Hand and 'Union Driver' in Starting_Hand and Board_Rank < 0.5:
        Board_Rank = 0.5
    if 'Photon Sanctuary' in Starting_Hand and 'C-Crush Wyvern' in Starting_Hand and 'A-Assault Core' in Starting_Hand and Board_Rank < 0.5:
        Board_Rank = 0.5
    if 'Photon Sanctuary' in Starting_Hand and 'C-Crush Wyvern' in Starting_Hand and 'B-Buster Drake' in Starting_Hand and Board_Rank < 0.5:
        Board_Rank = 0.5
    if 'Photon Sanctuary' in Starting_Hand and 'C-Crush Wyvern' in Starting_Hand and 'C-Crush Wyvern' in Starting_Hand and Board_Rank < 0.5:
        Board_Rank = 0.5
    if 'Photon Sanctuary' in Starting_Hand and 'C-Crush Wyvern' in Starting_Hand and 'Effect Veiler' in Starting_Hand and Board_Rank < 0.5:
        Board_Rank = 0.5
    if 'Photon Sanctuary' in Starting_Hand and 'C-Crush Wyvern' in Starting_Hand and 'Union Driver' in Starting_Hand and Board_Rank < 0.5:
        Board_Rank = 0.5
    if 'Photon Sanctuary' in Starting_Hand and 'Effect Veiler' in Starting_Hand and 'A-Assault Core' in Starting_Hand and Board_Rank < 0.5:
        Board_Rank = 0.5
    if 'Photon Sanctuary' in Starting_Hand and 'Effect Veiler' in Starting_Hand and 'B-Buster Drake' in Starting_Hand and Board_Rank < 0.5:
        Board_Rank = 0.5
    if 'Photon Sanctuary' in Starting_Hand and 'Effect Veiler' in Starting_Hand and 'C-Crush Wyvern' in Starting_Hand and Board_Rank < 0.5:
        Board_Rank = 0.5
    if 'Photon Sanctuary' in Starting_Hand and 'Effect Veiler' in Starting_Hand and 'Effect Veiler' in Starting_Hand and Board_Rank < 0.5:
        Board_Rank = 0.5
    if 'Photon Sanctuary' in Starting_Hand and 'Effect Veiler' in Starting_Hand and 'Union Driver' in Starting_Hand and Board_Rank < 0.5:
        Board_Rank = 0.5
    if 'Photon Sanctuary' in Starting_Hand and 'Union Driver' in Starting_Hand and 'A-Assault Core' in Starting_Hand and Board_Rank < 0.5:
        Board_Rank = 0.5
    if 'Photon Sanctuary' in Starting_Hand and 'Union Driver' in Starting_Hand and 'B-Buster Drake' in Starting_Hand and Board_Rank < 0.5:
        Board_Rank = 0.5
    if 'Photon Sanctuary' in Starting_Hand and 'Union Driver' in Starting_Hand and 'C-Crush Wyvern' in Starting_Hand and Board_Rank < 0.5:
        Board_Rank = 0.5
    if 'Photon Sanctuary' in Starting_Hand and 'Union Driver' in Starting_Hand and 'Effect Veiler' in Starting_Hand and Board_Rank < 0.5:
        Board_Rank = 0.5
    if 'Photon Sanctuary' in Starting_Hand and 'Union Driver' in Starting_Hand and 'Union Driver' in Starting_Hand and Board_Rank < 0.5:
        Board_Rank = 0.5
    
    return Board_Rank, InterruptionCheck