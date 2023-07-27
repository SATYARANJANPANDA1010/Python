import datetime
dt = datetime.datetime.today()
print(dt)

# strf --> string format time
# %a --> weekday abbreviated name
print(dt.strftime("%a"))
# %A --> weekday full name
print(dt.strftime("%A"))
# %w --> weekday as decimal number --> where sunday--> 0 & saturday --> 6
print(dt.strftime("%w"))
# %d --> day of the month
print(dt.strftime("%d"))
# %b --> month abbreviated name
print(dt.strftime("%b"))
# %B --> month full name
print(dt.strftime("%B"))
# %A %d --> Weekday full name & day of the month
print(dt.strftime("%A %d"))
# %B %A %d --> month & Weekday full name , day of the month
print(dt.strftime("%B %d %A"))
# %m --> month number
print(dt.strftime("%m"))
# %y --> year without century
print(dt.strftime("%y"))
# %y ---> year with century
print(dt.strftime("%Y"))
# Weekday fullname, day of the month, Month name, Year with century
print(dt.strftime("%A %d %B %Y"))

# day of the year --> %j
print(dt.strftime("%j"))
# weekday of the year --> %U
print(dt.strftime("%U"))
#
print(dt.strftime("%u"))

# Hour --> %H
print(dt.strftime("%H"))
# Hour,Minute,Second --> %H %M %S
print(dt.strftime("%H:%M:%S"))

# date and time representation
print(dt.strftime("%c"))
# DD/MM/YY
print(dt.strftime("%x"))
# HH/MM/SS
print(dt.strftime("%X"))


