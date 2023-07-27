gradeList = [['naresh', 'A'],
             ['suresh', 'B'],
             ['ramesh', 'C'],
             ['kishore', 'D'],
             ['rajesh', 'E']]
gradeListA = [stud for stud in gradeList if stud[1]=='A']
gradeListB = [stud for stud in gradeList if stud[1]=='B'] 
print(gradeListA)
print(gradeListB)