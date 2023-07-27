#Example of global keyword
x = 100 #global variables
def fun1():
    global x
    x="satya" #local variables
fun1()
print(x)