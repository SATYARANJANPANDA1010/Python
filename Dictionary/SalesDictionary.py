#sales dictionary
salesDict={2000:45000,
           2001:54000,
           2002:42000,
           2003:56000,
           2004:78000,
           2005:67000,
           2006:48000}
print(salesDict)
sale1 = {}
sale2 = {}
sale3 = {}
for year,sale in salesDict.items():
    if sale>=40000 and sale<50000:
        sale1[year] = sale
    elif sale>=50000 and sale<60000:
        sale2[year] = sale
    elif sale >= 60000:
        sale3[year] = sale
print(sale1)
print(sale2)
print(sale3)
