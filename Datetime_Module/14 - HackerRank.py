import datetime

# Read the input date in format "MM DD YYYY"
month, day, year = map(int, input().split())

# create a datetime object with the input date
input_date = datetime.date(year, month, day)

# Find the day of the week for the input date
day_of_week = input_date.strftime("%A")

# Output the day of the week in capital letters
print(day_of_week.upper())
