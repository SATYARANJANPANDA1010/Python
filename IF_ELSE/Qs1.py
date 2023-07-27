# https://csiplearninghub.com/python-if-else-conditional-statement-practice/
units = int(input("Enter Units: "))
if units <= 100:
    amt = 0
elif units>100 and units<=200:
    amt = (units-100)*5
elif units>200:
    amt = 0+500+(units-200)*10

print(f'Amount{amt}')