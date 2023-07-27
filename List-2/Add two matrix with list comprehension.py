print("Enter elements of matrix1")
matrix1=[[int(input("enter value")) for j in range(2)] for i in range(2)]
print("Enter elements of matrix2")
matrix2=[[int(input("enter value")) for j in range(2)] for i in range(2)]
matrix3=[[matrix1[i][j]+matrix2[i][j] for j in range(2)] for i in range(2)]

print(f'Matrix1={matrix1}')
print(f'Matrix2={matrix2}')
print(f'Matrix3={matrix3}')
