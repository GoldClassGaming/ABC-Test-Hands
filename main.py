#Original Author: jpalm @_JP53 on twitter
#Updated and Maintained by: GoldClass @AndyGCG on twitter

from ComboTester import combo

def import_deck(filename):
    with open(filename) as f:
        deck = [line.strip() for line in f if not line.startswith('#')]
        return deck


# What decklist we want to import and how many hands we want to simulate
def main(deck_txt, n):
    print(deck_txt)
    deck = import_deck(deck_txt)
    print(deck)
    combo(deck, n)

# By editing the parameters of main you can change which deck is tested and how many hands are simulated
main("Decklists/Pure_ABC.txt", 10000)
