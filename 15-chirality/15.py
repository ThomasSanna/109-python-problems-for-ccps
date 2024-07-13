def is_left_handed(pips):
  return pips[1]>pips[0] and pips[2]>pips[1] # I did not understand this challenge
  
print(is_left_handed((1, 2, 3)))
print(is_left_handed((1, 5, 3)))
print(is_left_handed((5, 3, 1)))
print(is_left_handed((1, 3, 5)))
print(is_left_handed((6, 5, 4)))