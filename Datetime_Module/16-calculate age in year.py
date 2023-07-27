import datetime

# current year
current_date = datetime.date.today()
print(current_date)
print(current_date.year)
print(current_date.month)
print(current_date.day)
# Input the date of birth in y/m/d format
date_of_birth = input("Enter your date of birth in yyyy/mm/dd format: ")
# Convert date of birth string to a date object
date_of_birth_object = datetime.datetime.strptime(date_of_birth,"%Y/%m/%d")
# Calculate the difference between the current date and the date of birth
calculate_age = current_date.year - date_of_birth_object.year-((current_date.month, current_date.day) < (date_of_birth_object.month, date_of_birth_object.day))
print(f"Age is: {calculate_age}")


