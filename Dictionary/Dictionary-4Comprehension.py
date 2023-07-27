salesDict={2000:45000,
           2001:54000,
           2002:42000,
           2003:56000,
           2004:78000,
           2005:67000,
           2006:48000}
print(salesDict)
sale1 = {year:sales for year,sales in salesDict.items() if sales<=50000}
print(sale1)
sale2 = {year:sales for year,sales in salesDict.items() if sales>60000 and sales<70000}
print(sale2)
sale3 = {year:sales for year,sales in salesDict.items() if sales>70000}
print(sale3)
