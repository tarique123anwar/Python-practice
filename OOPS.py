#OOPS PROGRAMMM CONCEPT   

 #class is define (class) keyword , class name and : colon
# class DemClass:
#     s=20
#     def fun(self):
#         print(20+60)
# o=DemClass()  #Object is define any variable (=) and class name () sqr braket
# o1=DemClass()
# o2=DemClass()
# print(o.s)   # class ko ham kitne baar bhi call kar sakte hain object ke throw
# print(o1.s)
# print(o2.s)
# o.fun()
# #/////
# class d:
#     o=33
#     def f(self):
#         print(23+44)
# v=d()
# print(v.o)
# v.f()

#/////////

# class Anwar:
#     k=30
#     def a(self):
#         print(3*4)
# d=Anwar()
# print(d.k)
# d.a()

# #////////////////

# class sohel:
#     Anwar=1500,"Total"
#     def clear(self):
#         print(1500-500,"Phonepe")
#         print("Earphone",500)
#         print("sohel due:-",1)
# d=sohel()
# print(d.Anwar)
# d.clear()

# class Anwar: #(This is Class)
#     k=30
# d=Anwar()    #(This is Object)
# print(d.k)   #(Calling)

#//////////////////////////////////////////////////////  30/1/2024  //////////////////////////////////////////////////////////#

#new practice
     #class object using Method in self keyword
# class Demo():
#     a=10
#     def showvalue(self):
#         self.c=self.a*self.a
#         print("this in value\n",self.c)
#     def showvalue1(self,a,b):
#         print(a+b)
# obj=Demo()
# obj.showvalue()
# obj.showvalue1(29,39)

#constructor pro ,constructor ko call karne ki zarorat nahi hoti ye khud se ho jata hai object bnatehi 
# class Demo():
#     a=10
#     def __init__(self):
#         print("Welcome to Servicepack.ia",2+30)
#     def showvalue(self):
#         self.c=self.a*self.a
#         print("this in value\n",self.c)
#     def showvalue1(self,a,b):
#         print(a+b)
# obj=Demo()
# obj.showvalue()
# obj.showvalue1(29,39)

    # Single inheritance 

# class A:
#     def displayA(self):
#         print("Welcome to Servicepack.ai")

# class B(A):
#     def displayB(self):
#         print("Welcome to Hyderabad")
        
# obj=B()
# obj.displayA()
# obj.displayB()

# class C(A,B):
#     def displayC(self):
#         print("Welcome to Office")
# obj=B()
# obj.displayA()
# obj.displayB()
# # obj.displayC()

#     # Multilevel inheritance

# class A:
#     def displayA(self):
#         print("Welcome to Servicepack.ai")

# class B:
#     def displayB(self):
#         print("Welcome to Hyderabad")

# class C(A,B):
#     def displayC(self):
#         print("Welcome to Office")
# obj=C()
# obj.displayA()
# obj.displayB()
# obj.displayC()


    # encapsulation (getter and setter method)


# class student:
#     def __init__(self):
#         self.__name=""
#     def getname(self):
#         return self.__name 
#     def setname(self,name):
#         self.__name=name

# obj=student()
# obj.setname('Testing')
# name=obj.getname()
# print(name)

#//////////////////////////////31/1/2024//////////////////////////////////////////

#practice...class and object 

# class a:
#     s=20*3
# obj=a()
# print(a.s)

# class d:
#     q=30
#     w=300
#     def e(self):
#         print("Hy ji ")
#         print("Hello")

# obj=d()
# print(obj.q)
# print(obj.w)
# obj.e
# obj.d()

#class object with method 

# class test():
#     r=233
#     def show(self):
#         self.c=self.r**self.r
#         print("This is value ",self.r)
#     def show2(self,a,b):
#         print(a*b)
# #this is object
# obj=test()
# obj.show()
# obj.show2(30,234)

# class t2():
#     v=34+88
#     def s(self):
#         self.c=self.v**self.v
#         print('this value',self.v)
#     def x(self,a,b):
#         print(a-b)
# #create object
# ob=t2()
# ob.x(20,3)
# ob.s()

 # encapsulation (getter and setter method)

# class student:
#     __name="Anwar"
#     def __init__(self):
#         print(self.__name)
#         self.__displayinfo()
#     def __displayinfo(self):
#         print("Welcome to Servicepack.ai")
# obj=student()


class s:
    __n="Tarique"
    def __init__(self):
        print(self.__n)
        self.__dis()
    def __dis(self):
        print("Welcome to servicepack.ai")
obj=s()

    # method overloading concept is same name fun calling repeating (yek fun ko baar baar call karna h with parameters and without parameters)

class a:
    def find_area(self,x=None,y=None):
        if x !=None and y != None:
            print(x*y)
        elif x != None:
            print(x*x)
        else:
            print("Nothing")
obj=a()
obj.find_area()
obj.find_area(10)
obj.find_area(49,89)

    # same 


class q:
    def f(self,a=None , b=None):
        if a !=None and b !=None:
            print(a*b)
        elif a != None:
            print(a)
        else :
            print("Ntg")
obj=q()
obj.f(40,77)
obj.f(40)
obj.f()

    # method overrding same naam ka fun firse aata hai to wo overide ho jata hai 

class og:
    def showdata(self):
        print("I'm in python class ")
class og2(og):
    def showdata(self):
        # c=input("Value\n")
        print("I'm in java class\n")
obj=og2()
obj.showdata()
obj.showdata()
obj.showdata() 
obj.showdata()
obj.showdata() 
obj.showdata()

#/////////////////////////???

class d:
    t=22
    h=44
ob=()
print(d.t)
print('\n')
print(d.h)
ob.d()
ob.d()
 