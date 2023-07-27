# time object
# default arguments 0

import datetime
t1 = datetime.time()
print(t1)

t2 = datetime.time(11, 54, 23)
print(t2)
# read individual values
print(t2.hour, t2.minute, t2.second)