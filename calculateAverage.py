# This function calculates the average marks based on the grades provided in the input dictionary.

def calculateaverage(input_dict):
    marks = {'A':90, 'B':80, 'C':70, 'D':60}
    sum = 0
    length = len(input_dict)
    for key in input_dict:
        grade = input_dict[key]
        grade_to_marks = marks[grade]
        sum = sum + grade_to_marks
    
    average = sum / length
    return average

input_dict = {'Math': 'B', 'English': 'C', 'Science': 'A'}
output = calculateaverage(input_dict)

print(output)