# GFG | Python program to count number of vowels using sets in given string
'''
Input : GeeksforGeeks
Output : No. of vowels : 5

Input : Hello World
Output : No. of vowels :  3
'''
str1 = 'GeeksforGeeks'
set1 = set("AEIOUaeiou")
print(set1)
count = 0
for ch in str1:
    if ch in set1:
        count = count+1
print(f'Vowel Count{count}')