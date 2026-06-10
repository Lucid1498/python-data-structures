# This code defines a function to remove duplicate elements from a given list and demonstrates its usage with an example input list.

# The function iterates through each element in the input list, checks if it is already present in a new list of unique elements, and if not, appends it to that list. Finally, it returns the list of unique elements and prints the result for a sample input list.
def removeDuplicates(array):
    unique_elements = []
    for element in array:
        if element not in unique_elements:
            unique_elements.append(element)
        else:
            continue
    
    return unique_elements

# Example usage
input_array = [1, 1, 2, 3, 4, 5, 1, 2, 3]
output_array = removeDuplicates(input_array)

# Printing the list of unique elements
print(output_array)
