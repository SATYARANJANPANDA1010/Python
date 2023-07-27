#without comprehension 
matrix = []
for i in range(2):
    rows = []
    for j in range(2):
        ele= int(input("Enter the elements: "))
        rows.append(ele)
    matrix.append(rows)
print(matrix)

#with comprehension
list2= [[int(input("Enter the value"))for j in range(2)]for i in range(2)]
print(list2)
