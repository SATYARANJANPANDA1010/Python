# WAP to read m students and
# n subject marks and display
m = int(input("Enter how many students: "))
n = int(input("Enter how many marks: "))
list_marks = []
for i in range(m):
    score = []
    for j in range(n):
        marks = int(input("enter marks: "))
        score.append(marks)
    list_marks.append(score)

print(f'The {m} students mark: {list_marks}')

# Find sum and average score

for score in list_marks:
    print(f'Sum of Mark is {sum(score)},Average Marks is{sum(score)/n:.2f}')