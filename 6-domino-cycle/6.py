def domino_cycles (tiles):
    if len(tiles) < 1:
        return True
    
    if len(tiles) == 1:
        return tiles[0][0] == tiles[0][-1]
    
    for i in range(len(tiles)-1):
        if tiles[i][-1] != tiles[i+1][0]:
            return False
        
    return True and tiles[0][0] == tiles[-1][-1]

# Tests 

print(domino_cycles([(1, 2), (2, 3), (3, 1)])) # True
print(domino_cycles([(1, 2), (2, 3), (3, 4)])) # False
print(domino_cycles([])) # True
print(domino_cycles([(1, 2)])) # False
print(domino_cycles([(1, 1)])) # True