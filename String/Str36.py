namesList = ["naresh","suresh","kiran","rama","rajesh"]
for name in namesList:
    if name.startswith("r"):
        print(name)
for name in namesList:
    if name.startswith(('n','r')):
        print(name)
