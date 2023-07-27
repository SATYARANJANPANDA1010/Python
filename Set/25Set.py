# iterate over a set
import timeit
set1 = {10, 20, 30, 40}
start = timeit.default_timer()
for value in set1:
    print(value)
stop = timeit.default_timer()
print(stop-start)
