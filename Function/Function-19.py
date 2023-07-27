#Python Does not support Function Overloading

#the old function replaced by the new function


def fun1():
    print("1.0")

def fun1():
    print("2.0")
def fun1(a):
    print("3.0")

def fun1(a,b):
    print("4.0")

def main():
    fun1(10,20)
main()