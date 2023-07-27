courseSet = {'python', 'java', 'C++', 'Oracle'}
e = enumerate(courseSet)
for n,course in e:
    print(n,course)

print()
# Count value set manually
enu = enumerate(courseSet,1)
for n,course in enu:
    print(n,course)
