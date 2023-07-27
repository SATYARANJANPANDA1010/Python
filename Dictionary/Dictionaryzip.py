#zip(*iterables)
rollno = [1,2,3]
names = ["satya","naresh","ramesh"]
studDict = dict(zip(rollno,names))
print(studDict)
l1 = [1,2,3]
l2 = [10,20,30]
l3 = zip(l1,l2)
d5 = dict(l3)
print(d5)
for x in l3:
    print(x)
z1 = ["naresh","surresh","ramesh"]
z2 = [101,102,103]
z3 = [1,2,3]
z = zip(z1,z2,z3)
for i in z:
    print(i)

