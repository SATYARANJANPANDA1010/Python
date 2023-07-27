# nested if
# develop login or signin application
users = {'naresh':'n123',
         'ramesh':'r123',
         'kishore':'k658'}
user = input("Enter user name: ")
pwd = input("Enter Password: ")
if user in users:
    if users[user] == pwd:
        print(f'{user} Welcome')
    else:
        print("invalid password")
else:
    print("invalid user name")