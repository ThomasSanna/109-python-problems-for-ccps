def can_balance(lst):
  if len(lst) == 0:
    return -1
  for i in range(len(lst)):
    count = 0
    for avant in range(i):
      count += (i-avant) * lst[avant]
    for apres in range(i+1, len(lst)):
      count -= (apres-i) * lst[apres]
    if count == 0:
      return i
  return -1

print(can_balance([6, 1, 10, 5, 4]))  # Expected result: 2
print(can_balance([10, 3, 3, 2, 1]))  # Expected result: 1
print(can_balance([7, 3, 4, 2, 9, 7, 4]))  # Expected result: -1
print(can_balance([42]))  # Expected result: 0
print(can_balance([]))