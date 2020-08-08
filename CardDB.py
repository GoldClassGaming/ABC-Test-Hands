import requests
import json
import pandas as pd
import numpy as np

def CardDatabase():
  YGOProDeck = requests.get('https://db.ygoprodeck.com/api/v7/cardinfo.php')
  carddb = YGOProDeck.json()['data']

  CardDataFrame = pd.DataFrame(carddb, index=carddb[]['name'])
  print(CardDataFrame)