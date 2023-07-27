#This define Object Level Operation 

class Robot:
    def walk(self):             #without argument
        print("Robot walk")
    def talk(self,msg):         #with argument
        print(f"{msg}")

def main():
    robo1 = Robot()
    robo1.walk()
    robo1.talk("Hello,Human")
    robo2 = Robot()
    robo2.walk()
    robo2.talk("Hello,Satya!")
main()
