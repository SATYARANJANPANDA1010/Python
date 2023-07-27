# Skipping letters
# You are given a word and an index position of a character. You need to write program that print without
# the character at the given index.
# Example :
# input: Combine
# index: 4
# Output: Combne
str = input("Enter a string: ")
index = int(input("Enter index: "))
lis = list(str)
remove_ind = lis.pop(index)
modify_string = ""
for ele in lis:
    modify_string = modify_string+ele
print(modify_string)