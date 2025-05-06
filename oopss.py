'''---------------oops---------------------
multi-level
multiple
hierarchy
hybrid'''

#multiple-inheritance
class base1: # 1 st baseclass
    def __init__(self):
        super(base1,self).__init__()
        print("base class - 1")
class base2 : # 2nd base class
    def __init__(self):
        super(base2,self).__init__()
        print("base class -2")
class derived(base1,base2):
    def __init__(self):
        super(derived,self).__init__()
        print("derived class from both classes")
d=derived()

output::

base class -2
base class - 1
derived class from both classes
-----------------------------------------------------
"""initalsize classes addition,multiplication in a calculater and pass the values
from main program to super class where the sub classes addition and multiplication
were triggered and return the outputs respectively

1.take the derived classes calc
2.from derived class call math to the object
3.return the values after math to the object
4.manual values of f both numbers considered within the object"""
class add():
    def __init__(self,a,b):
        self.a=a
        self.b=b
    def ad(self):
        return self.a+self.b
       
class mul():
    def __init__(self,a,b):
        self.a=a
        self.b=b
    def mu(self):
        return self.a*self.b
        
class calc(add,mul) :
    def __init__(self,a,b):
        add.__init__(self,a,b)
        mul.__init__(self,a,b)
x=int(input())
y=int(input())
c=calc(x,y)
print(c.ad())
print(c.mu())

output:

 2
 3
5
6
-----------------------------------------------------
#wap to calculate square and cube of a number using multiple-inheritance 
class sq:
    def __init__(self,a):
        self.a=a
    def squ(self):
        return  self.a * self.a
class cub:
    def __init__(self,a):
        self.a=a
    def cube(self):
        return  self.a*self.a * self.a 
class result(sq,cub):
    def __init__(self,a):
        sq.__init__(self,a)
        cub.__init__(self,a)
x=int(input("enter:"))
c=result(x)
print(c.squ())
print(c.cube())
print(c.squ() + c.cube())

output:

enter: 3
9
27
36

--------------------------------------------------------
#multi-level inheritance
class person :
    def name(self):
        print("name")
class teacher(person):
    def qualification(self):
        print("hod")
class hod(teacher):
    def exp(self):
        print("expirence")
head=hod()
head.name()
head.qualification()
head.exp()
output:
name
hod
expirence
-------------------------------------------------------------
#multi-level inheritance  cubes and squares of object
class num:
    def __init__(self,n):
        self.n=n
class sq(num):
    def square(self):
        return self.n**2
class cu(sq):
    def cube(self):
        return self.n**3
calc=cu(4)
print(calc.square())
print(calc.cube())
output:

16
64
-------------------------------------------------
 #compoistion/containership ---used for complex objects
#abstract class
class fruit:
    def taste(self):
        raise NotImplementedError()
    def vitamin(self):
        raise NotImplementedError()
    def color(self):
        raise NotImplementedError()
class mango(fruit):
    def taste(self):
        return "sweet"
    def vitamin(self):
        return "vitamin-A"
    def color(self):
        return "yellow"
class orange(fruit):
    def taste(self):
        return "sweet and sour"
    def vitamin(self):
        return "vitamin-c"
    def color(self):
        return "orange"
alphanso=mango()
print(alphanso.taste(),alphanso.vitamin(),alphanso.color())
org=orange()
print(org.taste(),org.vitamin(),org.color())
output:

sweet vitamin-A yellow
sweet and sour vitamin-c orange
















