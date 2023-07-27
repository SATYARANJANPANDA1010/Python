# Comprehension
# WAP to add n integer inside list
# without using comprehension

n = int(input("enter how many values: "))
list1 = []
for i in range(n):
    ele = int(input("Enter Elements: "))
    list1.append(ele)
print(list1)

# Using Comprehension
num = int(input("enter how many values: "))
list2 = [int(input("Enter Elements: ")) for i in range(num)]
print(list2)


