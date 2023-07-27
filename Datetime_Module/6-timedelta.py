# Add year
# 52 weeks in one year

import datetime
d1 = datetime.date.today()
print(d1)
year = datetime.timedelta(weeks=52)
d1 = d1+year
print(d1)
d1 = d1-year
print(d1) 