def find_min_element(input_list):
    if len(input_list) == 0:
        return None  # Return None for an empty list
    else:
        min_element = input_list[0]  # Assume first element is the minimum
        for element in input_list:
            if element < min_element:
                min_element = element
        return min_element

# Example usage:
my_list = [5, 2, 9, 1, 7]
min_element = find_min_element(my_list)
print("The minimum element in the list is:", min_element)
