# Remove all occurrences of input element or value

n = int(input("Enter how many values: "))
list1 = []
for i in range(n):
    ele = int(input("Enter elements: "))
    list1.append(ele)
print(f'Original List is {list1}')
x = int(input("Enter remove All Occurrences of input element: "))
while x in list1:
    list1.remove(x)

print(f'After remove all occurrences {list1}')
