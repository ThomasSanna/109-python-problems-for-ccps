def colour_trio(colours):
    if len(colours) == 1:
        return colours
    
    colourAfter = ''
    
    for i in range (len(colours)-1):
        if colours[i] == colours[i+1]:
            colourAfter += colours[i]
        elif (colours[i] in ('r', 'b')) and (colours[i+1] in ('r', 'b')):
            colourAfter += 'y'
        elif (colours[i] in ('y', 'b')) and (colours[i+1] in ('y', 'b')):
            colourAfter += 'r'
        else :
            colourAfter += 'b'
    return colour_trio(colourAfter)

# Tests of that : 

print(colour_trio('y')) # 'y'
print(colour_trio('bb')) # 'b'
print(colour_trio('rybyry')) # 'r'
print(colour_trio('brybbr')) # 'r'
print(colour_trio('rbyryrrbyrbb')) # 'y'
print(colour_trio('yrbbbbryyrybb')) # 'b'