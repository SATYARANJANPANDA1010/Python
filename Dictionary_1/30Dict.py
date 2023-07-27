# copy()
d1 = {1:10, 2:20, 3:30, 4:40}
d2 = d1.copy()
print(d1)
print(d2)
d3 = {1:[10,20],2:[30,40],3:[50,60]}
d4 = d3.copy()
print(d3)
print(d4)
d3[1].append(100)
print(d3)
print(d4)
