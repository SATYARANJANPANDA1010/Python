salesDict = {2000:45000, 2001:54000, 2002:42000, 2003:56000, 2004:78000, 2005:67000}
print(salesDict)
sales1 = {year:sales for year,sales in salesDict.items() if sales<=50000}
print(sales1)
sales2 = {year:sales for year,sales in salesDict.items() if sales>50000}
print(sales2)
