def count_dominators(items):
    if not items:
        return 0

    count = 1   # the last item is already counted.
    maxElement = items[-1]

    for i in range(len(items) - 2, -1, -1):
        if items[i] > maxElement:
            count += 1
            max_element = items[i]

    return count

# Tests

print(count_dominators([42, 7, 12, 9, 2, 5]))  # 4
print(count_dominators([]))  # 0
print(count_dominators([-2, 5, -1, -3]))  # 3
print(count_dominators([-10, -20, -30, -42]))  # 4
print(count_dominators([42, 42, 42, 42]))  # 1
print(count_dominators(range(10**7)))  # 1
print(count_dominators(range(10**7, 0, -1)))  # 10000000


# The following is my first solution, which is not as good as the one above.
# It is not as good because it uses the max() function, which is O(n).
# The solution above is O(n) because it only loops once through the list.
#
# def count_dominators(items):
#     count = 1  # the last item is already counted.
    
#     if len(items) < 2:
#         return 0 if len(items)==0 else 1
    
#     for i in range(len(items)-1):
#         if items[i] > max(items[i+1:]):
#             count += 1
#     return count

# print(count_dominators([42, 7, 12, 9, 2, 5])) # 4
# print(count_dominators([])) # 0
# print(count_dominators([-2, 5, -1, -3])) # 3
# print(count_dominators([-10, -20, -30, -42])) # 4
# print(count_dominators([42, 42, 42, 42])) # 1
# print(count_dominators(range(10**7))) # 1
# print(count_dominators(range(10**7, 0, -1))) # 10000000 (takes a while)