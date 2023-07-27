# Python program to multiply two matrices
A = [[1, 5, 7],
     [4, 0, 2],
     [6, 0, 3]]

B = [[1, 0],
     [4, 0],
     [5, 0]]
# A(3*3) B(3*2) --> C(3*2)
C = [[0, 0],
    [0, 0],
    [0, 0]]

for i in range(len(C)):
    for j in range(len(C[0])):
        for k in range(len(B)):
            C[i][j] += A[i][k] * B[k][j]
for row in C:
    print(row)












