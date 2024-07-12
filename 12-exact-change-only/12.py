def give_change(amount, coins):
  res = []
  newAmount = amount
  for coin in coins:
    div = newAmount//coin
    newAmount -= div * coin
    res += [coin]*div
  return res
  
print(give_change(64, [50, 25, 10, 5, 1]))
print(give_change(123, [100, 25, 10, 5, 1]))
print(give_change(100, [42, 17, 11, 6, 1]))
