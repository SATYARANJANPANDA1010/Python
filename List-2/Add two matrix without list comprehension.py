m1 = []
for i in range(2):
    row = []
    for j in range(2):
        ele = int(input("Enter the element"))
        row.append(ele)
    m1.append(row)
m2 = []
for i in range(2):
    row = []
    for j in range(2):
        ele = int(input("Enter the element"))
        row.append(ele)
    m2.append(row)
m3 = []
for i in range(2):
    row = []
    for j in range(2):
        row.append(m1[i][j]+m2[i][j])
    m3.append(row)
print(f'Matrix1 {m1}')
print(f'Matrix2 {m2}')
print(f'Matrix3 {m3}')

