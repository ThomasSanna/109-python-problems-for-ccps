def count_growlers(animals):
    left = ["cat", "dog"]
    dogs = ["dog", 'god']
    res = 0
    for i in range(len(animals)):
        nbAll=0
        nbDogs=0
        n=i
        isLeft = animals[i] in left
        while n > 0 and n < len(animals)-1:
            n = n-1 if isLeft else n+1
            nbAll+=1
            nbDogs+=1 if animals[n] in dogs else 0
        res += 1 if nbDogs > nbAll/2 else 0
    return res

assert count_growlers(['cat', 'dog']) == 0
assert count_growlers(['god', 'cat', 'cat', 'tac', 'tac', 'dog', 'cat', 'god']) == 2
assert count_growlers([
    'dog', 'cat', 'dog', 'god', 'dog', 'god', 'dog', 'god',
    'dog', 'dog', 'god', 'god', 'cat', 'dog', 'god', 'cat',
    'tac'
]) == 11
assert count_growlers([
    'god', 'tac', 'tac', 'tac', 'tac', 'dog', 'dog', 'tac',
    'cat', 'dog', 'god', 'cat', 'dog', 'cat', 'cat', 'tac'
]) == 0