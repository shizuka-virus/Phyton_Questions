# Take input for two numbers
num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))

# Display the numbers before swapping
print("Before swapping:")
print("First number:", num1)
print("Second number:", num2)

# Swap the values using tuple unpacking
num1, num2 = num2, num1

# Display the numbers after swapping
print("\nAfter swapping:")
print("First number:", num1)
print("Second number:", num2)
