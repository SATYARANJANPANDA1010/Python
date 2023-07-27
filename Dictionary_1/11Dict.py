users_dict = {'naresh':'nit123',
              'suresh':'sit456',
              'kiran':'kit234',
              'satya':'sit321'}
print("****Login****")
username = input("User Name: ")
pwd = input("Password: ")
if username in users_dict:
    p = users_dict[username]
    if p == pwd:
        print(f'{username} Welcome')
    else:
        print('Invalid Password')
else:
    print("Invalid Username ")