def calculator(operation, num1, num2):
    if operation == "+":
        return num1 + num2
    elif operation == "-":
        return num1 - num2
    elif operation == "*":
        return num1 * num2
    elif operation == "/":
        if num2 != 0:
            return num1 / num2
        else:
            return "Error: Division by zero"
    else:
        return "Error: Invalid operation"

# Example usage:
result = calculator("+", 5, 3)  # Addition
print("Result of addition:", result)

result = calculator("-", 5, 3)  # Subtraction
print("Result of subtraction:", result)

result = calculator("*", 5, 3)  # Multiplication
print("Result of multiplication:", result)

result = calculator("/", 5, 3)  # Division
print("Result of division:", result)

result = calculator("/", 5, 0)  # Division by zero
print("Result of division:", result)
