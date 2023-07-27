#Python: Print current time and date

import datetime
now = datetime.datetime.now()
print("Current Date-Time: ")
print(now.strftime("%Y-%m-%d %H:%M:%S"))