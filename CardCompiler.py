

def DataCompile(Card, Name):
  #Check for Card Type (Monster/Spell/Trap)
  if Card['type'] == 'Spell Card':
    print(Name)
  elif Card['type'] == 'Trap Card':
    print(Name)
  else:
    print(Name)
    print(Card['attribute'])
  return
