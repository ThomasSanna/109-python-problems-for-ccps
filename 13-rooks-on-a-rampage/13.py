def safe_squares_rooks(n, rooks):
    rowsRooks = set()
    colsRooks = set()
    
    for row, col in rooks:
        rowsRooks.add(row)
        colsRooks.add(col)
    
    safeRows = n - len(rowsRooks)
    safeCols = n - len(colsRooks)
    
    safeSquares = safeRows * safeCols
    
    return safeSquares

print(safe_squares_rooks(10, []))  # 100
print(safe_squares_rooks(4, [(2, 3), (0, 1)]))  # 4
print(safe_squares_rooks(8, [(1, 1), (3, 5), (7, 0), (7, 6)]))  # 20
print(safe_squares_rooks(2, [(1, 1)]))  # 1
print(safe_squares_rooks(6, [(r, r) for r in range(6)]))  # 0
print(safe_squares_rooks(100, [(r, (r*(r-1))%100) for r in range(0, 100, 2)]))  # 3900
print(safe_squares_rooks(10**6, [(r, r) for r in range(10**6)]))  # 0
