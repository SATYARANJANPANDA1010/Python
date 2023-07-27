# Python allows reading items/elements from list in different ways
# 1. Using Index

course = ['python', 'java', '.net', 'oracle']
c1 = course[0]
c2 = course[1]
c3 = course[2]
c4 = course[3]
# c5 = course[4] --> IndexError: list index out of range
print(c1, c2, c3, c4)

c1 = course[-1]
c2 = course[-2]
c3 = course[-3]
c4 = course[-4]
print(c1, c2, c3, c4)


