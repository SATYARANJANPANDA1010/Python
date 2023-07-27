m = int(input("Enter howmany students"))
n= int(input("Enter howmany subjects"))
marks = []
for i in range(m):
    students = []
    for j in range(n):
        sub = int(input("Enter the subjects"))
        students.append(sub)
    marks.append(students)
print(marks)
