#Original Author: jpalm @_JP53 on twitter
#Updated and Maintained by: GoldClass @AndyGCG on twitter

from ComboTester import combo
from DeckImport import import_deck


# What decklist we want to import and how many hands we want to simulate
def main(deck_txt, n):
    print(deck_txt)
    deck = import_deck(deck_txt)
    print()
    combo(deck, n)

# By editing the parameters of main you can change which deck is tested and how many hands are simulated
main("Decklists/Dogmatika ABC.ydk", 1000)
