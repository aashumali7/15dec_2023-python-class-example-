#1 class define 
class Vehicle(): #base class
    #1.1 property
    name=''
    model=''
#1.2 constructor
    def __init__(self,x ,y): #self is internal object
        self.name = x
        self.model = y
   #1.3 method
#2 class define 
class Car(Vehicle): #derived class
    #2.1 property
    #2.2 constuctor
    #2.3 method
    def myCar(self): #self is internal object
        print(f"My Car Name is {self.name}")
        print(f"My Car Model is {self.model}")
#create class obeject
#classobject = ClassName
co = Car('Verna','2024')
#classobject.method
co.myCar()