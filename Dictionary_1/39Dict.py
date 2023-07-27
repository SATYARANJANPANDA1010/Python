# Dictionary Comprehension
gradeDict = {'naresh':'A', 'suresh':'B', 'ramesh':'C', 'Kiran':'A', 'raman':'B', 'rajesh':'C'}
gradeDictA = {name:grade for name,grade in gradeDict.items() if grade == 'A'}
print(gradeDictA)
gradeDictB = {name:grade for name,grade in gradeDict.items() if grade == 'B'}
print(gradeDictB)
gradeDictC = {name:grade for name,grade in gradeDict.items() if grade == 'C'}
print(gradeDictC)

