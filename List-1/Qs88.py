# Representing details of 3 students and
# each student is having roll no, name, course

# Using Index
students = [[1, 'Satya', 'Python'], [2, 'Moni', 'java'], [3, 'Kishore', 'C++']]
for i in range(len(students)): # 0 1 2
    for j in range(len(students[i])):
        print(students[i][j],end=' ')
    print()

# Without using index
for stud in students:
    for value in stud:
        print(value, end=' ')
    print()







