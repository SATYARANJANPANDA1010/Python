#Write a Python program that accepts a sequence of comma-separated numbers
#from the user and generates a list and a tuple of those numbers.

values = input("Enter numbers separated by list: ")
lis = values.split(",")
tupl = tuple(lis)
print("List:",lis)
print("Tuple",tupl)
