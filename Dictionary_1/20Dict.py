# setdefault(key[,default])
phoneDict = {'naresh':9988765432,'suresh':77785494534,'parmesh':756482848}
print(phoneDict.setdefault('naresh'))
print(phoneDict.setdefault('suresh'))
print(phoneDict.setdefault('parmesh'))
print(phoneDict.setdefault('brajesh'))
print(phoneDict.setdefault('harish',8454893844))
print(phoneDict)