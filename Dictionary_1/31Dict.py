# fromkeys(iterable,[value])
d1 = dict.fromkeys(range(1,10))
print(d1)
names = ['satya', 'ramesh', 'harish', 'suresh']
d2 = dict.fromkeys(names)
print(d2)
d2['satya'] = 100
print(d2)