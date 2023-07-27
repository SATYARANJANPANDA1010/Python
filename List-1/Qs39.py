# replacing more than one value using slicing

list1 = [10,20, 30, 40, 50, 60, 70]
print(list1)
list1[:3] = [1,2,3]
print(list1)
list1[3:5] = ["satya", "moni"]
print(list1)
list1[-2:] = [9, 10]
print(list1)
list1[3:-3] = [4, 5, 6, 7, 8]
print(list1)
list1[-1:-3:-1] = [100, 90]
print(list1)
