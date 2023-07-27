# pop(key)
personDict = {'naresh': 45, 'suresh': 30, 'kishore': 37, 'ramesh': 46}

age = personDict.pop('ramesh')
print(age)
print(personDict)
# if key is not there , you have to mention  'None' --> otherwise it will give key error
age = personDict.pop('harish',None)
print(age)
print(personDict)