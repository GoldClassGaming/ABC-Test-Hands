from Combos import * 

def Desires(test_hand, deck):
  banished_pile = []
  #get rid of cards
  test_hand.remove('Pot of Desires')
  for i in range(0,10):
    banished_pile.append(deck.pop(0))

  test_hand.append(deck.pop(0))
  test_hand.append(deck.pop(0))

  return ComboCheck(test_hand, deck)

def Upstart(test_hand, deck):
  test_hand.remove('Upstart Goblin')
  test_hand.append(deck.pop(0))
  return ComboCheck(test_hand,deck)
  