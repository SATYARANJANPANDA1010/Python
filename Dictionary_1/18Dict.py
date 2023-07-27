# iterator
d1 = {'a': 'apple', 'b': 'ball'}
i = iter(d1)
n1 = next(i)
n2 = next(i)
print(n1,n2)
print(d1[n1],d1[n2])