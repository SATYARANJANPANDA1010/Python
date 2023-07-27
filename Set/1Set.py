set1 = {10, 20, 30, 40, 50, 60}
print(set1)

# Hashable Objects
a = 10
print(hash(a))

b = 20
print(hash(b))

c = 1.5
print(hash(c))

d = 'satya'
print(hash(d))

# Because tuple is a hashable object.
tuple1 = (10,20,30)
print(hash(tuple1))

# List is not a hashable object
# unhashable type
# list1 = [10, 20, 30]
# print(hash(list1))