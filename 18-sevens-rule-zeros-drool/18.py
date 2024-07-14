def seven_zero(n):
    if n == 0:
        return None
    
    def generate_number(d, k):
        return int('7' * k + '0' * (d - k))
    
    if n % 2 != 0 and n % 5 != 0:
        return int('7' * n)
    
    for d in range(1, 824):
        for k in range(1, d + 1):
            number = generate_number(d, k)
            if number % n == 0:
                return number
    
    return None

print(seven_zero(70))
print(seven_zero(17)) 
print(seven_zero(42)) 
print(seven_zero(103))
print(seven_zero(77700))
print(seven_zero(2**50)) 
print(seven_zero(12345)) 
