x=100
y=200

def fun1():
    print(f'Global variable x={x}')
    print(f'Global variable y={y}')
fun1()
print(f'value of X is {x}')
print(f'value of Y is {y}')

def fun2():
    print(f'Global variable x={x}')
    print(f'Global variable y={y}')
fun2()
