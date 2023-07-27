def upper(s):   #it converts upper case to lower case
    us=' '     #empty string
    for ch in s:
        if ch>='a' and ch<='z':
            us=us+chr(ord(ch)-32)   #concatenate in empty string
        else:
            us=us+ch      #else it is a upper case
    return us

def lower(s):   #it converts lower case to upper case
    ls= ' '
    for ch in s:
        if ch>='A' and ch<='Z':
            ls=ls+chr(ord(ch)+32)
        else:
            ls=ls+ch    #else it is a lower case
    return ls

def main():
    s1 = upper("satya")
    s2 = lower("MONISHA")
    print(f"From lower case to upper case convertion is {s1}")
    print(f"From upper case to lower case convertion is {s2}")
main()

