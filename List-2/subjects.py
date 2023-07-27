n = int(input("enter howmany players: "))
slist = []
for i in range(n):
    score = int(input("ENTER SCORES: "))
    slist.append(score)
print(slist)
for score in slist:
    print(score)
for i in range(n):
    print(slist[i])
