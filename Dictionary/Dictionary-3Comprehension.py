grade = {'Satya':'A',
         'Ramesh':'B',
         'Naresh':'A',
         'Prateek':'C',
         'Ram':'D',
         'Biswas':'B',
         'Priya':'C',
         'Anukul':'D',
         'Moni':'B'}
print(grade)
gradeA = {name:grade for name,grade in grade.items() if grade=='A'}
print(gradeA)
gradeB = {name:grade for name,grade in grade.items() if grade=='B'}
print(gradeB)
gradeC = {name:grade for name,grade in grade.items() if grade=='C'}
print(gradeC)
gradeD = {name:grade for name,grade in grade.items() if grade=='D'}
print(gradeD)
