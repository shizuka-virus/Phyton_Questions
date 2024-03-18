def is_prime(number):
    if number < 2:
        return False
    for i in range(2, int(number ** 0.5) + 1):
        if number % i == 0:
            return False
    return True

# Example usage:
print(is_prime(7))  # Output: True
print(is_prime(12))  # Output: False
