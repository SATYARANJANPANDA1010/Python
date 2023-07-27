namesList = ['naresh', 'suresh', 'kishore', 'kiran', 'rajesh']
namesList1 = [name for name in namesList if name[-1] == 'h']
namesList2 = [name for name in namesList if name[-1] == 'h' or name[0] == 'k']
print(namesList1)
print(namesList2)