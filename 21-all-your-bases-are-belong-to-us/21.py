def group_and_skip(n, out, ins):
    res = []
    while n>0:
        res.append(n%out)
        n = (n//out)*ins
    return res

assert group_and_skip(13, 3, 2) == [1, 2, 1, 2]
assert group_and_skip(123456789, 10, 1) == [9, 8, 7, 6, 5, 4, 3, 2, 1]
assert group_and_skip(987654321, 1000, 1) == [321, 654, 987]
assert group_and_skip(255, 2, 1) == [1, 1, 1, 1, 1, 1, 1, 1]
assert group_and_skip(81, 5, 3) == [1, 3, 2, 0, 4, 3]
assert group_and_skip(10**9, 13, 3) == [12, 1, 2, 0, 7, 9, 8, 11, 6, 8, 10, 5, 8, 3]