#syntax - del d[key]
#Remove d[key] from d.
#raises key error if key is not in the map

d1 = {1:10,2:20,3:30,4:40}
print(d1)
del d1[1]
print(d1)
del d1[2]
print(d1)
#del d1[1]
#print(d1)
#Output: KeyError: 1

#key in d
#Return True if f has a key , else False

course = {'java':2000,
          'python':4000,
          'C++':3500,
          'Web':8000}
print(course)
print("python" in course)
print("C++" in course)
print("Oracle" in course)
print("SQL" not in course)
print("java" not in course)
