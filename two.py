#class define 
class Student(): #base class
     #1.1 property
     name=''
     surname=''
     age=''
     hobby=''
    #1.2 constructor
     def __init__(self,w, x ,y,z): #self is internal object
         self.name= w
         self.surname= x
         self.age= y
         self.hobby = z
    #1.3 method
     def studentInfo(self): #self is internal object
        print(f"student name is a {self.name}")
        print(f"student surname is a {self.surname}")
        print(f"student age is a {self.age}")
        print(f"student hobby is a {self.hobby}")

#classobject=ClassName
aa = Student('Aashish',"Mali",'''19''','Cricket')
#classobject.method
aa.studentInfo()