num = int(input("Enter a number: "))  # Taking input from the user

# Checking if the input number is negative
if num < 0:
    print("Factorial is not defined for negative numbers")
elif num == 0:
    print("Factorial of 0 is 1")
else:
    factorial = 1
    while num > 0:
        factorial *= num
        num -= 1
    print("Factorial is:", factorial)
