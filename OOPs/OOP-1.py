class Car:
    def start(self):           #instance method
        print("Car Start..")
    def stop(self):            #instance method
        print("Car Stop..")

#Car is a User Defined Class Type
bmw = Car()      #creating object of Car class  --> bmw is the object of Car class
bmw.start()
bmw.stop()

i20 = Car()      #i20 is the object of Car class
i20.start()
i20.stop()

#object level function should call object name only

#List is a Pre-defined class Type
list1 = list()  # --> list() is a pre-defined class
list2 = list()

print(type(bmw),type(i20))
print(type(list1),type(list2))