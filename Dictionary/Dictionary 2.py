d1 = dict()
print(d1)
print(type(d1))
d2 = dict(java=2000,python=4000)
print(d2)
#list1 = [1,2,3,4,5]
#d3 = dict(list1)
#print(d3)
#TypeError: cannot convert dictionary update sequence element #0 to a sequence
lis1 = [(1,10),(2,20),(3,30),(4,40),(5,50)]
d1 = dict(lis1)
print(d1)
#enumerate
lis2 = [10,20,30,40]
e = enumerate(lis2,1)
d5 = dict(e)
print(d5)
#list comprehension
l1 = [1,2,3]
l2 = [10,20,30]
l3 = [(l1[i],l2[i]) for i in range(3)]
print(l3)
d6 = dict(l3)
print(d6)

