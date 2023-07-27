# Iterator
# Iterator is a object which is used to read or iterate each item from elements(collection).
# Iterators are read only and forward only
# iter() function return iterator object
# iter(iterables/collections)

list1 = [10,20,30,40,50]
a = iter(list1)
x = a.__next__()
y = a.__next__()
z = a.__next__()
p = a.__next__()
q = a.__next__()
# r = a.__next__() --> Stopiteration Error
print(x,y,z,p,q)


