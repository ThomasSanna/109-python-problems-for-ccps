def taxi_zum_zum(moves):
  dictCoos = {
    "N" : (0, 1),
    "E" : (1, 0),
    "S" : (0, -1),
    "W" : (-1, 0)
  }
  tabCoos = [(0, 1), (1, 0), (0, -1), (-1, 0)]
  moves = moves.replace("LR", "").replace("RL", "")
  coos = [0, 0]
  direction = 0
  
  for let in moves:
    if let == 'F':
      coos[0] += tabCoos[direction][0]
      coos[1] += tabCoos[direction][1]
    else:
      direction += 1 if let == 'R' else -1+4
      direction %= 4
  return coos
  
  
print(taxi_zum_zum("RFRL"))
print(taxi_zum_zum("LFFLF"))
print(taxi_zum_zum("LLFLFLRLFR"))
print(taxi_zum_zum("FR" * 1729))
print(taxi_zum_zum("FFLLLFRLFLRFRLRRL"))