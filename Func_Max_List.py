def find_largest_element(input_list):
    if len(input_list) == 0:
        return None  # Return None for an empty list
    else:
        max_element = input_list[0]  # Assume first element is the maximum
        for element in input_list:
            if element > max_element:
                max_element = element
        return max_element

# Example usage:
my_list = [5, 2, 9, 1, 7]
largest_element = find_largest_element(my_list)
print("The largest element in the list is:", largest_element)
