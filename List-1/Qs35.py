# WAP to read score n players into list

n = int(input("Enter How many players "))
list1 = []
for i in range(n):
    score = int(input("Enter score "))
    list1.append(score)
print(f'Read score: {list1}')

# Read values from List without using index
for score in list1:
    print(score)

print("----------------------------------------------")
# Read values from List using Index
for i in range(n):
    print(list1[i])