"""
hearts = coeurs
diamonds = carreaux
spades = piques
clubs = trèfles
"""

listingRank = ['one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine', 'ten', 'jack', 'queen', 'king', 'ace']
# listingSuit = ['hearts', 'diamonds', 'spades', 'clubs']

def winning_card(cards, trump=None):
  if not trump: 
    winningSuit = cards[0][1]
  else:
    winningSuit = trump
    
  cardsSameSuit = [card for card in cards if card[1] == winningSuit]
  cardsSameSuit = cards if cardsSameSuit == [] else cardsSameSuit
  winningCard = [
    card for card in cardsSameSuit 
    if listingRank.index(card[0]) == max(
      listingRank.index(i[0]) for i in cardsSameSuit
      )
  ][0]
  
  return winningCard
    
    
  
print(winning_card([('three', 'spades'), ('ace', 'diamonds'), ('jack', 'spades'), ('eight', 'spades')]))
print(winning_card([('ace', 'diamonds'), ('ace', 'hearts'), ('ace', 'spades'), ('two', 'clubs')], 'clubs'))
print(winning_card([('two', 'clubs'), ('ace', 'diamonds'), ('ace', 'hearts'), ('ace', 'spades')]))
print(winning_card([('six', 'hearts'), ('ace', 'spades'), ('three', 'hearts'), ('jack', 'hearts')], 'hearts'))
print(winning_card([('jack', 'spades'), ('queen', 'spades'), ('eight', 'spades'), ('two', 'diamonds')], 'diamonds'))
print(winning_card([('jack', 'spades'), ('queen', 'spades'), ('eight', 'spades'), ('two', 'diamonds')], 'clubs'))