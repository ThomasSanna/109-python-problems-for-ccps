def is_ascending(items):
    if len(items) <= 1:
        return True
    else:
        for i in range (len(items)-1):
            if items[i]>=items[i+1]:
                return False
    return True

# Tests

print(is_ascending([])) # True
print(is_ascending([-5, 10, 99, 123456])) # True
print(is_ascending([2, 3, 3, 4, 5])) # False
print(is_ascending([-99])) # True
print(is_ascending([1, 1, 1, 1])) # False