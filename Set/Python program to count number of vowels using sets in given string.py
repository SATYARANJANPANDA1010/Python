str1 = "GeeksforGeeks"
setV = set("AEIOUaeiou")
c =0
for ch in str1:
    if ch in setV:
        c=c+1
print(f'Vowel Count {c}')
