
# find the size of the set in python
# the amount of memory in bytes occupied by object

# sys.getsizeof(object)

a = 10
import sys
print(sys.getsizeof(a))

b = 888888888888888888888888
print(sys.getsizeof(b))

set1 = {10, 20, 30}
print(sys.getsizeof(set1)) 