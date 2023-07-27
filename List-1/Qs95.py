# WAP to add two marices

# Using Comprehension
print("First Matrix")
matrix1 = [[int(input("Enter elements: "))for j in range(2)]for i in range(2)]
print("Second Matrix")
matrix2 = [[int(input("Enter elements: "))for j in range(2)]for i in range(2)]
print("Add Two Matrices")
matrix3 = [[matrix1[i][j]+matrix2[i][j]for j in range(2)]for i in range(2)]
print(matrix1)
print(matrix2)
print(matrix3)

# without using comprehension
m1 = []
for i in range(2):
    row = []
    for j in range(2):
        ele = int(input("Enter element: "))
        row.append(ele)
    m1.append(row)
m2 = []
for i in range(2):
    row = []
    for j in range(2):
        ele = int(input("Enter elements: "))
        row.append(ele)
    m2.append(row)
m3 = []
for i in range(2):
    row = []
    for j in range(2):
        row.append(m1[i][j]+m2[i][j])
    m3.append(row)

print(m1)
print(m2)
print(m3)

