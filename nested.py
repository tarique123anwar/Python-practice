# Input: Nested list with names and grades
students = [
    ["John", 45.0],
    ["Alice", 30.0],
    ["Bob", 35.0],
    ["Charlie", 30.0],
    ["David", 40.0]
]

# Extracting unique grades
grades = set(student[1] for student in students)

# Finding the second lowest grade
second_lowest_grade = sorted(grades)[1]

# Finding names with the second lowest grade
students_with_second_lowest = [student[0] for student in students if student[1] == second_lowest_grade]

# Sorting names alphabetically
students_with_second_lowest.sort()

# Printing the result
for name in students_with_second_lowest:
    print(name)
