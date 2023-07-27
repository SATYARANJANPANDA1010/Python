# Program to count vowels, consonant, digits and special characters in string.
str1 = "geeks for geeks121 aioqw@#"
vc = 0
cc = 0
dc = 0
sc = 0
for ch in str1:
    if (ch>='A' and ch<='Z') or (ch>='a' and ch<='z'):
        if ch.lower() in ('a','e','i','o','u'):
            vc=vc+1
        else:
            cc = cc+1
    elif ch>='0' and ch<='9':
        dc = dc+1
    else:
        sc = sc+1
print(f'Vowel: {vc}')
print(f'Consonant: {cc}')
print(f'Digit: {dc}')
print(f'Special Character: {sc}')
