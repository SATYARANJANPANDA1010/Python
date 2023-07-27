n = int(input("Enter howmany students: "))
m = int(input("Enter howmany Subjects: "))
marks = []
for i in range(n):
    students = []
    for j in range(m):
        sub = int(input("ENTER THE MARKS: "))
        students.append(sub)
    marks.append(students)
for students in marks:
    print(f'{students},{sum(students)},{sum(students)/n:.2f}')
    
        
