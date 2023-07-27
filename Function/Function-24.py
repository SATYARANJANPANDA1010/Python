def fun1(a=10,b=20):
    print(a,b)


def fun2(x,y=0):
    print(x,y)

def main():
    fun1()
    fun1(100)
    fun1(200,300)
    fun1(b=900)
    fun2(10)
    fun2(100,2000)
    fun2(x=70)
    fun2(10,y=90)

main()
