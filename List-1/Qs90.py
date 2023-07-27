# WAP to read m*n matrix and display

m = int(input("Enter how many rows: "))
n = int(input("Enter how many columns: "))
matrix = []
for i in range(m):
    row = []
    for j in range(n):
        ele = int(input("Enter the elements: "))
        row.append(ele)
    matrix.append(row)
print(matrix)

for row in matrix:
    for col in row:
        print(col, end=' ')
    print()