# WAP to create 3*3 Matrix and display

# without comprehension
m = int(input("Enter how many rows: "))
n = int(input("Enter how many columns: "))
matrix = []
for i in range(m):
    row = []
    for j in range(n):
        value = int(input("enter elements: "))
        row.append(value)
    matrix.append(row)
print(matrix)

# Using Comprehension
matrix1 = [[int(input("Enter elements: ")) for j in range(3)]for i in range(3)]
print(matrix1)

