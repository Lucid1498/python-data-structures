def filterEven(array):
    even_array = []
    for element in array:
        if element%2 == 0:
            even_array.append(element)
    
    return even_array

input_array = [1,2,3,4,5,6,7,8,9]
output_array = filterEven(input_array)

print(output_array)