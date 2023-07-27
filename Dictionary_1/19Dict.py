# get(key[,default])
dict1 = {'A':'Apple','B':'Ball','C':'Cat'}
print(dict1.get('A'))
print(dict1.get('B'))
print(dict1.get('C'))
# If the key is not present in the dictionary, it will give default as 'None'.
# if you mention default value, then it will show in your output
print(dict1.get('D','Invalid Key'))
print(dict1.get('E'))

