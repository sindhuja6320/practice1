#polymorphism:overloading,overid
ing
#overloading
def hi(name="abc"):
    print("hello",name)
hi()
hi("sindhu")
output:
hello abc
hello sindhu
--------------------------------------------------
#multiple args in overloading
def abc(*args):
    return sum(args)
print(abc(12,34,5,56))
output:
107
-------------------------------------------------------
#simple overloading using class with constructor
class ab:
    def __init__(self,name=None,age=None):
        if name and age :
            print(f"name:{name},age:{age}")
        elif name:
            print("name:",name)
        else:
            print("No Data")
ab()
ab("sindhu")
ab("prerana",20)
output:
No Data
name: sindhu
name:prerana,age:20
<__main__.ab at 0x2623e0f5580>
  ------------------------------------------------------
  #isinstance()
n=99
print(isinstance(n,int))
print(isinstance(n,float))
output:
True
False
----------------------------------------------
#isinstance using class
class pet:
    pass
class dog:
    pass
ob=dog()
print(isinstance(ob,dog))
print(isinstance(ob,pet))
output:
True
False
---------------------------------------------------------
#overriding redifine the child class which is already exists
class pet:
    def sound(self):
        print("animal sounds")
class dog(pet):
    def sound(self):
        print("bow boww!")
a=pet()
a.sound()
d=dog()
d.sound()
output:
animal sounds
bow boww!
--------------------------------------------------------------------------


-------------------------------------------------------
#overloading with operators
class val:
    def __init__(self,x,y):
        self.x=x
        self.y=y
    def __add__(self,ol):
        return val(self.x+ol.x,self.y+ol.y)
    def __str__(self):
        return f"{self.x},{self.y}"
a=val(1,2)
b=val(3,5)
print(a+b)
output:
4,7
----------------------------------------------
"""code for add two complex numbers,where imaginary numbers and real numbersto be evaluated seperately aith 
__add__()method and raise and error exception with this values where unsupportive data type is encountered
a=1+2i
b=3+4i
output:
4+6i"""
class complex:
    def __init__(self,x=0,y=0):
        self.x=x
        self.y=y
    def __add__(self,ol):
        if isinstance(ol,complex):
            return complex(self.x+ol.x,self.y+ol.y)
        else:
            raise TypeError("unsupported operand-type")
    def __str__(self):
        return f"{self.x} + {self.y}i"
a=complex(1,2)
b=complex(3,4)
print(a+b)
output:
4 + 6i
--------------------------------------------------------
#overriding
class pet:
    def sound(self):
        print("animal sounds")
class dog(pet):
    def sound(self):
        super().sound()#calling parent class
        print("bow boww!")
a=pet()
a.sound()
output:
animal sounds
------------------------------------------------------------

#constructor overriding:
class student:
    def __init__(self,name):
        self.name=name
        print("student constructor")
class person(student):
    def __init__(self,name,grade):
        super().__init__(name)
        self.grade=grade
        print("person constructor")
s=person('sindhu',"f")
output:
student constructor
person constructor
----------------------------------------------------------
#method overiding by a polymorphism eval
class pet:
    def sound(self):
        print("animalsound")
class dog:
    def sound(self):
        print("bow bow...!")
class cat:
    def sound(self):
        print("meow meow...!")

pets=[dog(),cat(),pet()]
for p in pets:
    p.sound()
output:
bow bow...!
meow meow...!
animalsound
--------------------------------------
'''code for overriding different parameteers in parent methods by calculating the area of 
circle and sqyare from a parent class shape 
pass side 4 for  square and radius 5 for circle.'''
from math import pi
class shape:
    def area(self):
        return 0
class Square(shape):
    def __init__(self,side):
        self.side=side
    def area(self):
        return side**2
        
       
        
class Circle(shape):
    def __init__(self,r):
        self.r=r
    def area(self):
        return pi*(r**2)
    

r=int(input())
side=int(input())
square=Square(side)
circle=Circle(r)

print(square.area())
print(circle.area())
output:
 4
 5
25
50.26548245743669
------------------------------------------------------------







  

