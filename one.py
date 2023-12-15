#class define 
class Animal(): #base class
     #1.1 property
     name=''
     age=''
    #1.2 constructor
     def __init__(self,x ,y): #self is internal object
         self.name= x
         self.age= y
    #1.3 method
     def dogInfo(self): #self is internal object
         print(f'dog name is {self.name}')
         print(f'dog age is {self.age}')
     
 #create class object
 #classobject = ClassName
co = Animal('BullDog','1year')
 #classobject.method
co.dogInfo()