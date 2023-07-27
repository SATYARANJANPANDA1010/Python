# GFG
# Filtering even and odd numbers of list

numList = [1,5,9,3,4,2,12,15,13,17,19,21,24,16,27,37,67,79]
evenList = []
oddList = []
for value in numList:
    if value % 2 == 0:
        evenList.append(value)
    else:
        oddList.append(value)

print(numList)
print(evenList)
print(oddList)