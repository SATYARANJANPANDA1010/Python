# dict.values()
salesDict = {2018: 45000, 2019: 50000, 2020: 49000, 2021: 52000, 2022: 56000}
sales = salesDict.values()
print(sales)
# if you want to changes in dictionary, then these changes are refelect to views.
# and views are dynamic so , doesn't require to create a views object another time.
salesDict[2023] = 69000
print(sales)
# read sales value
for s in sales:
    print(s)
# sum of sales value
print(sum(sales))