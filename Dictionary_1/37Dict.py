# Create dictionary with name as a key and 2 subject marks as value
# read the details of n students

dict1 = {}
n = int(input('Enter how many students: '))
for i in range(n):
    name = input("Enter name: ")
    marks = [int(input("Enter Marks")) for j in range(2)]
    dict1[name] = marks
print(dict1)

# Comprehension
stud = {input("Enter Student Name: "):[int(input("Enter Student Marks"))for j in range(2)]for i in range(n)}
print(stud)