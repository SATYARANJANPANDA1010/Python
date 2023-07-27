class Alpha:
    def __init__(self):
        print("Constructor without Arguments")
class Beta:
    def __init__(self,x,y):
        print("Constructor with Arguments")
def main():
    A1 = Alpha() #it takes --> Alpha.__init__()
    A2 = Alpha()
    B1 = Beta(10,20)  #it takes --> Beta.__init__()
    B2 = Beta(100,200)
main()