# Find a string --> Hacker Rank
str1 = input("Enter a String: ") # ABCDCDC
str2 = input("Enter a Sub_string: ") # CDC
length = len(str2)
count = 0
for i in range(len(str1)):
    s = str1[i:length+i]
    if s == str2:
        count = count+1
print(count)
