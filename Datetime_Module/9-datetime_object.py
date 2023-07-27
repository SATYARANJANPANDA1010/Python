import datetime
# datetime object carry --> year,month,day,hour,minute,second
d1 = datetime.datetime(2023, 3, 14, 5, 12, 23)
print(d1)

# read individual values
print(d1.year, d1.month, d1.day, d1.hour, d1.minute, d1.second)

# separate date
print(d1.date())
# separate time
print(d1.time())

# today/system date & time
today = datetime.datetime.today()
print(today)