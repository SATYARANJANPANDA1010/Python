# enumerate
list1 = [10, 20, 30, 40, 50]
a = enumerate(list1)
print(next(a))
print(next(a))
print(next(a))
print(next(a))
print(next(a))
# print(next(a)) --> out of the index, so that it will stop iteration and give Stop Iteration error.


studNames = ["naresh", "suresh", "satya"]
e = enumerate(studNames)
x = e.__next__()
y = e.__next__()
z = e.__next__()
print(x,y,z)