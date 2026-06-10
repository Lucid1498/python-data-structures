# This code defines a function to filter out even numbers from a given list and demonstrates its usage with an example input list.

# The function iterates through each element in the input list, checks if it is even, and if so, appends it to a new list. Finally, it returns the list of even numbers and prints the result for a sample input list.
def filterEven(array):
    even_array = []
    for element in array:
        if element%2 == 0:
            even_array.append(element)
    
    return even_array

# Example usage
input_array = [1,2,3,4,5,6,7,8,9]
output_array = filterEven(input_array)

# Printing the filtered list of even numbers
print(output_array)