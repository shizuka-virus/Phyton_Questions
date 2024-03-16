# Taking input for a list from the user
input_list = input("Enter elements of the list separated by spaces: ").split()

# Converting each input element to its appropriate data type
input_list = [int(x) if x.isdigit() else float(x) if x.replace('.', '', 1).isdigit() else x for x in input_list]

# Printing the input list
print("The input list is:", input_list)
