# GFG | Remove items from Set
# Using While Loop
# Input : set(['a','b','c','d','e'])
# Output :
# {'d', 'c', 'a', 'b'}
# {'c', 'a', 'b'}
# {'a', 'b'}
# {'b'}
# set()
set1  = set([12, 10, 13, 15, 8, 9])
while set1:
    set1.pop()
    print(set1)

# Using For Loop
# Input : set([12, 10, 13, 15, 8, 9])
# Output :
# {9, 10, 12, 13, 15}
# {10, 12, 13, 15}
# {12, 13, 15}
# {13, 15}
# {15}
# set()

inital_set = set([12, 10, 13, 15, 8, 9])
for i in range(len(inital_set)):
    inital_set.remove(next(iter(inital_set)))
    print(inital_set)
