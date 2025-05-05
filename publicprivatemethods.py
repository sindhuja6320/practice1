#private method useage
class abc:
    def __init__(self,var):
        self.__var=var #private
    def __display(self) :#private method
        print("form class method ,var=",self.__var)
ob=abc(100)
ob._abc__display()#use "_"to access a private method in a class 

output:
form class method ,var= 100
----------------------------------------------------------------------------
#calling a class method using another method in same class
class abc:
    def __init__(self,var):
        self.var=var
    def display(self):
        print("var is:",self.var)
    def add_val(self):
        self.var += 5
        self.display()


ob=abc(10)
ob.add_val()

ootput:
var is: 15
-----------------------------------------------------------------------------
#class method,which call a function define global namespace
def aa(x):
    return x*10
class abc:
    def __init__(self,var):
        self.var=var
    def display(self):
        print("var is:",self.var)
    def modify(self):
        self.var=aa(self.var)
ob=abc(10)
ob.display()
ob.modify()
ob.display()

output:
var is: 10
var is:100
-----------------------------------------------------------------------
#built-in methods : get,set,delete
#getattr(),setattr()and deletattr()
class abc():
    def __init__(self,var):
        self.var=var
    def display(self):
        print("var is :",self.var)
ob=abc(20)
ob.display()
print("obj has attribute var ",hasattr(ob,'var'))
getattr(ob,'var')
setattr(ob,'var',88)
print("after setting value var is:",ob.var)
setattr(ob,"count",10)
print("new var count is created with value:",ob.count)
delattr(ob,'var')
print("after deleting",ob.var)

output:
var is : 20
obj has attribute var  True
after setting value var is: 88
new var count is created with value: 10
----------------
AttributeError                            Traceback (most recent call last)
Cell In[45], line 17
     15 print("new var count is created with value:",ob.count)
     16 delattr(ob,'var')
---> 17 print("after deleting",ob.var)

AttributeError: 'abc' object has no attribute 'var'
-------------------------------------------------------------------------------
""" built-in functions in class attributes and multiple val for attributes
.__doc__--- when str doc is not specified no return attr
.__dict__---namespace accesed attributes
.__name__--return class attributes names
.__module__
.__bases__---inheritance
 . is a permission for accessing a method """
------------
class abc:
    def __init__(self,v1,v2):
        self.v1=v1
        self.v2=v2
    def display(self):
        print("vars are:",self.v1,self.v2)
ob=abc(20,67)
ob.display()
print("object.__dict__:",ob.__dict__)
print("object.__doc__:",ob.__doc__)
print("class.__name__:",abc.__name__)
print("object.__module__:",ob.__module__)
print("class.__bases__:",abc.__bases__)

 output:
 vars are: 20 67
object.__dict__: {'v1': 20, 'v2': 67}
object.__doc__: None
class.__name__: abc
object.__module__: __main__
class.__bases__: (<class 'object'>,)
----------------------------------------------------------------
#program that uses class as student to store name and marks of a student,use a list to store the marks of 3 subjects.
#constrains:
""" 1.take class as student
2.create a constructer for the student name
3.create a function for marks,to be entered manuly within the class function and add the marks to list
4.display the student name and the marks he /she got
5.pass the obj, attributes of 2 student names
testcase1:
obj1:"vijay"
obj2:"anil"
output: vijay got [88,9,88]
anil got[67,45,67] """
-----------------
class student:
    def __init__(self,name):
        self.name=name
        self.marks=[]
    def mark(self):
        for i in range(0,3):
            m=int(input((self.name,i+1)))
            self.marks.append(m)
            
        
    def display(self):
        print(self.name,"got",self.marks)
a=input() 
b=input()
ob=student(a)
ob.mark()
ob2=student(b)
ob2.mark()
ob.display()
ob2.display()
output:
 vijay
 anil
('vijay', 1) 34
('vijay', 2) 5
('vijay', 3) 67
('anil', 1) 78
('anil', 2) 89
('anil', 3) 46
vijay got [34, 5, 67]
anil got [78, 89, 46]
----------------------------------------------
""" program that has a class circle,use a class var to define the val of contant pi.
use this class var to calculate the area and circumfrence of circle with the specified radious
pi=3.14159
r=7.5
return area and circumfrence value to main program by creating function with in the class"""
class circle():
    pi=3.14159
    def __init__(self,radius):
        self.radius=radius
    def area (self):
      return pi*(radius**2)
    def circu(self):
      return 2*pi*radius
    """def display(self):
        print(circle.area())
        print(circle.circu())"""
        
ob=circle(7.5) 
class.area()
class.circu()
ob.display()
 





