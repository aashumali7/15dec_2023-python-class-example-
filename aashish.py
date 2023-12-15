class A():
    #1 property
    name =''
    surname = ''
    #2 constructor
    def __init__(self,x ,y):
        self.name = x
        self.surname = y
    #3 method
    def myName(self):
        print(f'my name is {self.name}')
        print(f'my surname is {self.surname}')        

#create class object 
#classobject = ClassName
co = A('aashish','mali')
#classobject.method
co.myName()


