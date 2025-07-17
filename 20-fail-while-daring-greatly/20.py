def josephus(n, k):
  lst = list(map(lambda x: x+1, list(range(n))))
  res = []
  i = (k-1)%len(lst)
  while len(lst) > 1:
    res.append(lst.pop(i))
    i = (i+k-1)%len(lst)
  res += lst
  return res

print(josephus(4, 1))
print(josephus(4, 2))
print(josephus(10, 3))
print(josephus(8, 7))
print(josephus(30, 4))
print(josephus(10, 10**100))