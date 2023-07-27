n1,n2,n3 = map(int,input("Enter 3 numbers: ").split())
if n1>n2:
    if n1>n3:
        print(f'{n1} is Max')
    else:
        print(f'{n3} is Max')
elif n2>n1:
    if n2>n3:
        print(f'{n2} is Max')
    else:
        print(f'{n3} is Max')
elif n3>n1:
    if n3>n2:
        print(f'{n3} is Max')
    else:
        print(f'{n2} is Max')
else:
    print(f'{n1},{n2},{n3} are equal')