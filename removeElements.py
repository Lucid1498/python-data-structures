# This code defines a function to remove specific elements from a given list and demonstrates its usage with an example input list.

# The function removes the first, third, and fourth elements from the input list using the pop method and returns the modified list. Finally, it prints the result for a sample input list.
def removeElements(array):
    first = array.pop(0)
    third = array.pop(2)
    fourth = array.pop(2)
    return array

# Example usage
input_array = ['Red', 'Green', 'White', 4, (5,6), 'Yellow']
output_array = removeElements(input_array)

# Printing the modified list
print(output_array)