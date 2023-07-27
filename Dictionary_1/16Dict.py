# dict.items()
salesDict = {2018: 45000, 2019: 50000, 2020: 49000, 2021: 52000, 2022: 56000}
total_item = salesDict.items()
print(total_item)
# item read
for i in total_item:
    print(i)
# key and value read
for x,y in total_item:
    print(x,y)