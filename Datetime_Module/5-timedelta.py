# Add Month
import datetime
d1 = datetime.date.today()
print(d1)
month = datetime.timedelta(weeks=4)
d1 = d1+month
print(d1)
d1 = d1-month
print(d1)
