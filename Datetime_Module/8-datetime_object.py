import datetime
d1 = datetime.datetime(2023,3,11)
print(d1)

d2 = datetime.datetime(2023, 3, 11, 12, 00, 00)
print(d2)

# read individual values
print(d2.year, d2.month, d2.day, d2.hour, d2.minute, d2.second)

# from datetime object you can read or separate only date
d3 = d2.date()
print(d3)
# from datetime object you can read or separate only time
t1 = d2.time()
print(t1)
# using datetime object you can find system date
dt = datetime.datetime.today()
print(dt)