m = int(input("enter howmany rows"))
n = int(input("enter howmany column"))
matrix = []
for i in range(m):
    row =[]
    for j in range(n):
        ele = int(input("enter the value"))
        row.append(ele)
    matrix.append(row)
print(matrix)


    
    
