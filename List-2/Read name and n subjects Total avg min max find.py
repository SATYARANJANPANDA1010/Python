name = input("Enter the name: ")
n = int(input("Enter howmany subjects"))
marks = []
for i in range(n):
    s = int(input("Enter marks"))
    marks.append(s)
total = sum(marks)
avg = total/len(marks)
maxSub = max(marks)
minSub = min(marks)
print(f'''Name: {name}
Marks: {marks}
Total: {total}
Average: {avg}
Maximum Marks: {maxSub}
Minimum Marks: {minSub}''')
