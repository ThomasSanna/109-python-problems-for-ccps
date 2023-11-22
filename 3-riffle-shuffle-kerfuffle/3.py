def riffle(items, out):
    if len(items)%2 != 0 or len(items) == 0:
        return items
    longDiv = len(items)//2
    leftItems = items[0:longDiv]
    rightItems = items[longDiv:len(items)]
    itemsRiffle = []
    for i in range(longDiv):
            itemsRiffle.append(leftItems[i]) if out else itemsRiffle.append(rightItems[i])
            itemsRiffle.append(rightItems[i]) if out else itemsRiffle.append(leftItems[i])
    return itemsRiffle

# Tests
    
print(riffle([1, 2, 3, 4, 5, 6, 7, 8], True)) # [1, 5, 2, 6, 3, 7, 4, 8]
print(riffle([1, 2, 3, 4, 5, 6, 7, 8], False)) # [5, 1, 6, 2, 7, 3, 8, 4]
print(riffle(['bob', 'jack'], True)) # ['bob', 'jack']
print(riffle(['bob', 'jack'], False)) # ['jack', 'bob']