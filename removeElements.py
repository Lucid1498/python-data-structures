def removeElements(array):
    first = array.pop(0)
    third = array.pop(2)
    fourth = array.pop(2)
    return array

input_array = ['Red', 'Green', 'White', 4, (5,6), 'Yellow']
output_array = removeElements(input_array)

print(output_array)