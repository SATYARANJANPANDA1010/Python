x = 100 #global variable
def fun1():
    x=200 #local variable
    print(x)
    d= globals()  #globals function --> This function returns global dictionary --> "d variable"  holding global dictionary object
    print(d['x'])

fun1()