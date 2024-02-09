def is_prime(num):
    if num < 2:
        return False
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            return False
    return True

def find_smallest_prime(input_numbers):
    q = min(input_numbers)
    
    if q % 2 == 0:
        return "None"
    
    for p in range(q, 10 ** 10):
        if is_prime(p):
            divisible = True
            for num in input_numbers:
                if num != q and p % num != q:
                    divisible = False
                    break
            if divisible:
                return p
    return "None"

# Input
input_numbers = list(map(int, input().split()))

# Output
result = find_smallest_prime(input_numbers)
print(result)
