# Remove character
str1 = "xxyyzxx"
occ = "x"
str2 = str()
for ch in range(len(str1)):
    if str1[ch] != occ:
        str2 = str2+str1[ch]
print(str2)

