# This function calculates the average marks based on the grades provided in the input dictionary.

# The function uses a predefined mapping of grades to marks, sums the marks for each subject, and then divides by the number of subjects to get the average. Finally, it demonstrates the usage of the function with an example input dictionary.
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

# Example usage
input_dict = {'Math': 'B', 'English': 'C', 'Science': 'A'}
output = calculateaverage(input_dict)

# Printing the average marks
print(output)