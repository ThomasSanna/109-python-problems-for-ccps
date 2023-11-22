def only_odd_digits(n):
    strN = str(n)
    for digit in strN:
        if int(digit) % 2 == 0:
            return False
    return True

# Tests

print(only_odd_digits(8)) # False
print(only_odd_digits(1357975313579)) # True
print(only_odd_digits(81235548984)) # False
