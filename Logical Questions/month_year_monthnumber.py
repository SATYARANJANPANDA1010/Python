year = int(input("Enter Year: "))
month = int(input("Enter Month Number: "))

#List of month name
month_name = [
    "January",
    "February",
    "March",
    "April",
    "May",
    "June",
    "July",
    "August",
    "September",
    "October",
    "November",
    "December"
]

#List of days in each month for a non-leap year
non_leap_year_days = [31,28,31,30,31,30,31,31,30,31,30,31]

#Check Year is leap year or not
if ( year % 4 == 0 and year % 100 != 0 ) or year % 400 == 0:
    non_leap_year_days[1] = 29

#get the name of the month
month_name = month_name[month-1]
#get the number of days of month
month_days = non_leap_year_days[month-1]

print(f'{month_name} {year} has {month_days} days.')
