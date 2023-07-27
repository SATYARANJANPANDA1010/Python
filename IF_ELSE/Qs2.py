cost = int(input("Enter Cost of Bike: "))
if cost > 100000:
    tax = cost*15/100
elif cost > 50000 and cost<= 100000:
    tax = cost*10/100
else:
    tax = cost*5/100
print(f'Bike Cost{cost}')
print(f'Tax{tax}')