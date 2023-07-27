# GFG
# multiply all numbers in the list

n = int(input("Enter the how many elements: "))
list1 = []
for i in range(n):
    ele = int(input("Enter elements: "))
    list1.append(ele)
print(list1)
multiply = 1
for i in list1:
    multiply = multiply*i
print(f'Multiply all numbers {multiply}')