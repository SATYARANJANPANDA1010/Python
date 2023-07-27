#global keyword

#syntax: global variable-name/identifier1,identifier2,identifier3..

x = 100 #global variable
def fun1():
    print(x) #it's printing global variable

def fun2():
    y = 200 #local variable
    print(x) #access global variable
    print(y) #access local varibale
def fun3():
    z = 300 #local variable
    x = 400 #local variable
    print(x) #local variable
    print(z) #local variable
def fun4():
    global x
    x = 600
    p = 700
    print(x) #it's print global variable
    print(p) #it's print local variable

#if I called the fun1(),then the global value can modified from x=100  to x=600,because In fun4() x value, it would assign as a "global" keyword.
def fun1():  
    print(x)
    
def main():
    fun1()
    fun2()
    fun3()
    fun4()
main()
