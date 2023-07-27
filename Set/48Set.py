f1 = {frozenset({10,20,30}),frozenset({10,20,30})}
print(f1)  #set does not allow duplicates

f2 = frozenset('PYTHON')
f3 = frozenset({1,2,3,4,5})
print(f2,f3,sep='\n')

f6 = {frozenset({'aeiou'}),frozenset({10,20,30,40})}
print(f6)