def knight_jump(knight, start, end):
  return set(knight) == set([abs(start[i] - end[i]) for i in range(len(start))])

print(knight_jump((2, 1), (12, 10), (11, 12)))
print(knight_jump((7, 5, 1), (15, 11, 16), (8, 12, 11)))
print(knight_jump((9, 7, 6, 5, 1), (19, 12, 14, 11, 20), (24, 3, 20, 11, 13)))