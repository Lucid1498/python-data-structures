def removeDuplicates(array):
    unique_elements = []
    for element in array:
        if element not in unique_elements:
            unique_elements.append(element)
        else:
            continue
    
    return unique_elements

input_array = [1, 1, 2, 3, 4, 5, 1, 2, 3]
output_array = removeDuplicates(input_array)

print(output_array)
