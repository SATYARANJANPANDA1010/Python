def fun1():
    x=100
    y=200
    print(f'Local Variable x={x}')
    print(f'Local Variable y={y}')
def fun2():
    print(f'Local Variable x={x}')
fun1()

# fun2() #it will give 'name' error because name 'x' is not defined
