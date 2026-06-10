# This code defines a function to find common elements between two lists and demonstrates its usage with example lists.

# Function to find common elements between two lists
def find_common_elements(list1, list2):
    return list(set(list1) & set(list2))

# Sample input lists
list_a = [1, 2, 3, 4, 5]
list_b = [3, 4, 5, 6, 7]

# Finding common elements between the two lists
common_elements = find_common_elements(list_a, list_b)

# Printing the common elements
print("Common elements:", common_elements)

