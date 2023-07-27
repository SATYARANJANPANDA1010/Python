#Python Program for simple interest
p = float(input("Enter the Principal Value: "))
t = int(input("Enter time: "))
r = float(input("Enter the rate of interest: "))
si = p*t*r/100
print(f'The simple interest is: {round(si,2)}')