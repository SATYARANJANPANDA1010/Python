# WAP to count each element in the list
# [10, 10, 20, 30, 40, 50, 20, 40, 30, 60, 30]

list1 = [10, 10, 20, 30, 40, 50, 20, 40, 30, 60, 30]
set1 = set(list1)
for value in set1:
    c = list1.count(value)
    print(f'{value} --> {c}')