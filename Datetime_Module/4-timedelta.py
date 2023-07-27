# Add/Increment day

import datetime
d1 = datetime.date.today()
print(d1)
days = datetime.timedelta(days=1)
d1 = d1+days
print(d1)
d1 = d1-days
print(d1)
