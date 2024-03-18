def is_prime(number):
    if number < 2:
        return False
    for i in range(2, int(number ** 0.5) + 1):
        if number % i == 0:
            return False
    return True

def print_primes():
    for num in range(2, 101):
        if is_prime(num):
            print(num)

# Example usage:
print_primes()
