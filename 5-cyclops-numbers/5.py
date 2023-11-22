# 2018 % 10 = 8 (last digit)

def is_cyclops(n):
    longN = 0
    tempN = n
    while tempN > 0:
        tempN = tempN // 10
        longN += 1
    
    if (longN % 2 == 0 and longN != 0) or n < 0:
        return False
    if longN == 0:
        return True
    
    boool = False
    
    for i in range(longN):
        if n // (10**i) % 10 != 0 and i == longN//2 :
            return False
        elif n // (10**i) % 10 == 0 and i != longN//2:
            return False
    return True

print(is_cyclops(0)) # True
print(is_cyclops(101)) # True
print(is_cyclops(98053)) # True
print(is_cyclops(77788850)) # False
print(is_cyclops(1056)) # False
print(is_cyclops(675409820)) # False
