name = input("Enter name: ")
username = input("Enter username: ")
pwd = input("Password: ")
if not name.isalpha():
    print("invalid name")
else:
    print("Valid Name")
if not username.isalnum():
    print("invalid username")
else:
    print("Valid User Name")
