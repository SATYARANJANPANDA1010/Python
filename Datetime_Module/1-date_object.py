import datetime
d1 = datetime.date(2023, 3, 12)
print(d1)

# read values
print(d1.day, d1.month, d1.year)

# But 'date' object can not modify it
# d1.day = 11
# AttributeError: attribute 'day' of 'datetime.date' objects is not writable



