ch = input("Enter the character:")
result = chr(ord(ch)+32) if ch>="A" and ch<="Z" else chr(ord(ch)-32) if ch>="a" and ch<="z" else ch
print(ch)
print(result)
