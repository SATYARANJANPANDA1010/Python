grade = {'Satya':'A',
         'Ramesh':'B',
         'Naresh':'A',
         'Prateek':'C',
         'Ram':'D',
         'Biswas':'B',
         'Priya':'C',
         'Anukul':'D',
         'Moni':'B'}
gradeA = {}
gradeB ={}
gradeC = {}
gradeD = {}
for name,grade in grade.items():
    if grade=='A':
        gradeA[name]=grade
    elif grade =='B':
        gradeB[name] = grade
    elif grade == 'C':
        gradeC[name] = grade
    else:
        gradeD[name] = grade
print(gradeA)
print(gradeB)
print(gradeC)
print(gradeD)

