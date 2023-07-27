year = int(input("enter the year:"))
print(year,"this is a leap year") if year % 4 == 0 and (year % 400 == 0 or year % 100!=0) else print(year,"this is not leap year")
