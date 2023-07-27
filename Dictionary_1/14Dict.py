# Dictionary Views
# They provide dynamic view on the dictionary, if any changes in dictionary , it will reflect these changes
# dict.keys()
# key view object
salesDict = {2018: 45000, 2019: 50000, 2020: 49000, 2021: 52000, 2022: 56000}
years = salesDict.keys()
print(years)
# whenever you do the changes in the dictionary, it will reflect to dictionary.
salesDict[2023] = 68000
print(years) # here 'years' is a view object.

for y in years:
    print(y)

# keys and values different
for v in years:
    print(v,salesDict[v])