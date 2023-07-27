# print matrix using index
matrix = [[10, 20, 30], [40, 50, 60], [70, 80, 90]]

for i in range(len(matrix)):
    for j in range(len(matrix[i])):
        print(matrix[i][j], end=' ')
    print()


# print matrix without using index
for ele in matrix:
    for value in ele:
        print(value, end=' ')
    print()
