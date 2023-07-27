# WAP to read name and
# n subject marks and
# display total avg.


name = input("Enter name: ")
sub = int(input("Enter how many subjects: "))
marks = []
for i in range(sub):
    m = int(input("Enter input Marks: "))
    marks.append(m)

total = 0
for m in marks:
    total = total + m

avg = total/sub
print(f'Name : {name} ')
print(f'Marks : {marks}')
print(f'Total : {total}')
print(f'Average: {avg:.2f}')







