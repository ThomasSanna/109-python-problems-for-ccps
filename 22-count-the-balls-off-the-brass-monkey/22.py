def pyramid_blocks(n, m, h):
    s = 0
    for i in range (h):
        s += (n+i)*(m+i)
    return s
        
assert pyramid_blocks(2, 3, 1) == 6
print("ye")
assert pyramid_blocks(2, 3, 10) == 570
print("ye")
assert pyramid_blocks(10, 11, 12) == 3212
print("ye")
assert pyramid_blocks(100, 100, 100) == 2318350
print("ye")
assert pyramid_blocks(10**6, 10**6, 10**6) == 2333331833333500000
print("ye")
