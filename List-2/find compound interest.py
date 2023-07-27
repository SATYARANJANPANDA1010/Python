principal = float(input("Enter the principal amount"))
rate = float(input("Enter the rate of interest"))
time = int(input("Enter the time"))
amount = principal*(1+(rate/100))**time
compound_interest = amount- principal
print(round(compound_interest,2))
