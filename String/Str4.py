# WAP to count alphabets,digits,special characters exist within string
str1 = input("Enter any string: ")
ac = 0
dc = 0
sc = 0
for ch in str1:
    if ch>='A' and ch<='Z' or ch>='a' and ch<='z':
        ac = ac+1
    elif ch>='0' and ch<='9':
        dc=dc+1
    else:
        sc=sc+1
print(f'Alphabte Count:{ac}')
print(f'Digits Count:{dc}')
print(f'Special Character Count:{sc}')