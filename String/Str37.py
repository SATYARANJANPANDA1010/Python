# str.endswith()
namesList = ["naresh","suresh","kiran","rama","rajesh"]
for name in namesList:
    if name.endswith("h"):
        print(name)

print()

for name in namesList:
    if name.endswith(("h","a")):
        print(name)