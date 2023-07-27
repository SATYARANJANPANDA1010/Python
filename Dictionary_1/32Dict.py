# reversed()
empDict = {'naresh': 5000,
           'suresh': 6000,
           'ramesh': 9000,
           'kishore': 6000}
print("--------FORWARD DIRECTION-----------")
a = iter(empDict)
for name in a:
    print(f'{name} --> {empDict[name]}')
print("--------BACKWARD DIRECTION or REVERSE DIRECTION-----------")
b = reversed(empDict)
for name in b:
    print(f'{name} --> {empDict[name]}')



