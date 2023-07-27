# string alignment methods
namesList = ['naresh','suresh','harish','kiran','satya']
for name in namesList:
    print(name.center(20))
for name in namesList:
    print(name.center(20,"*"))
empDict = {'naresh': 5000,
           'suresh': 9000,
           'raman': 8500,
           'kiran': 10500}
for name,salary in empDict.items():
    print(name.center(10,"*"),salary)