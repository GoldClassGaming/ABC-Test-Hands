import requests
import json
import pandas as pd
import numpy as np

#Depreciated
def CardDatabase():
  YGOProDeck = requests.get('https://db.ygoprodeck.com/api/v7/cardinfo.php')
  carddb = YGOProDeck.json()['data']
  #print(carddb)

  CardDataFrame = pd.DataFrame(carddb, index=carddb['name'])
  print(CardDataFrame)

def CardImport(ID):
  #Takes the card ID from the YDK File and gets all of that cards data from the Card DB
  RawData = requests.get(f'https://db.ygoprodeck.com/api/v7/cardinfo.php?id={ID}')
  CardData = RawData.json()['data']
  #Stores all of the cards info in a list to be returned to the deck importer
  return(CardData[0])

def import_deck(filename):
    with open(filename) as f:
        IDList = [line.strip() for line in f if not line.startswith('#') and not line.startswith('!')]
        #Add code for it to dynamically only import the main deck
        print(IDList)
        ImportedDeck = []
        for cardID in IDList:
          #Collects info about a card for each card in the deck
          ImportedDeck.append(CardImport(cardID))
          print(ImportedDeck[len(ImportedDeck) - 1]['name'])
        return ImportedDeck