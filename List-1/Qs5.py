# bool() in list

list1 = [10, 20, 30, 40, 50]

print(list1[bool(10)])  

print(list1[bool()])

print(list1[bool('')])  # this bool('') carries no space

print(list1[bool('A')])

print(list1[bool(' ')])  # this bool(' ') carries one white space
