# WAP to read name and n subject marks
# find total marks,avg,min,max

name = input("Enter name: ")
n = int(input("Enter how many subjects: "))
marks = []
for i in range(n):
    s = int(input("Enter marks: "))
    marks.append(s)

total = sum(marks)
avg = total/len(marks)
maxSub = max(marks)
minSub = min(marks)

print(f"Name{name}")
print(f"Marks{marks}")
print(f"Total Marks{total}")
print(f"Avg Marks {avg}")
print(f"Maximum Marks{maxSub}")
print(f"Minimum Marks{minSub}")

