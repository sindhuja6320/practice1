#class declaration
class sample():
    var="sindhu"
    def display(self):
        print("sample class pro")
ob=sample()
print(ob.var)
ob.display()
#output:
sindhu
sample class pro


------------------------------------
#create class constructer __init__(method)
class sample():
    def __init__(self,name,age):
        self.name=name
        self.age=age
        print(name,age)
        
        
    
obj=sample("sindhu",20)
#output:
sindhu 20
-----------------------------------
#class var,obj var
class ab():
    cv=0
    def __init__(self,var):
        ab.cv+=1
        self.var=var
        print("object var:",var)
        print("class var:",ab.cv)
ob=ab(10)
ob=ab(20)
ob=ab(30)
#output:
object var: 10
class var: 1
object var: 20
class var: 2
object var: 30
class var: 3
--------------------------------------
#check even /odd
class ev():
    def __init__(self,val):
        self.val=val
        if val%2==0:
            print("even")
        else:
            print("odd")
obj=ev(13)
obj=ev(2)
#output:
odd
even
----------------------------------------
#segregate even /odd in a separate list
class ev():
    el=[]
    ol=[]
    
    def __init__(self,val):
        self.val=val
        if val%2==0:
            ev.el.append(val)
           
        else:
            ev.ol.append(val)
            
obj=ev(13)
obj=ev(2)
obj=ev(4)
obj=ev(7)
obj=ev(5)
obj=ev(9)
print(ev.el)
print(ev.ol)
#output:
[2, 4]
[13, 7, 5, 9]
------------------------------------------
#__del__(method) 
class ab():
    cv=0
    def __init__(self,var):
        ab.cv+=2
        self.var=var
        print("object var:",var)
        print("class var:",ab.cv)
    def __del__(self):
        ab.cv-=1
        print('object with %d is going out of scope '%self.var)
ob1=ab(10)
ob2=ab(20)
ob3=ab(30)
del ob2
#output:
object var: 10
class var: 2
object var: 20
class var: 4
object var: 30
class var: 6
object with 20 is going out of scope 
------------------------------------------------------------------

#special methods in classes like
#__repr__ :return string representation
#__cmp__:compare 2 class
#__len__:length of the class object
class ab():
    def __init__(self,name,age):
        self.name=name
        self.age=age
    def __repr__(self):
        return repr(self.age)
    def __cmp__(self,obj):
        return self.age-obj.age
    def __len__(self): 
        return len(self.name)
obj=ab("abcdef",10)
print(repr(obj))
print(len(obj))
obj1=ab("ghuijk",1)
val=obj.__cmp__(obj1)
if val==0:
    print("equal")
elif val==-1:
    print("less")
#output:
10
6
greater

