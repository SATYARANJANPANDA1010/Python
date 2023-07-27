#Login Application

user_dict = {'naresh':'n123',
             'suresh':'s123',
             'satya':'',
             'kishore':'k123'}
print("*****Login*****")
uname=input("UserName")
pwd=input("Password")
if uname in user_dict and user_dict[uname]==pwd:
    print(f'{uname} welcome')
else:
    print("invalid username or password")
