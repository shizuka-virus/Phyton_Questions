def is_palindrome(string):
    # Convert the string to lowercase and remove spaces
    string = string.lower().replace(" ", "")
    # Check if the string is equal to its reverse
    return string == string[::-1]

# Example usage:
print(is_palindrome("radar"))  # Output: True
print(is_palindrome("hello"))  # Output: False
