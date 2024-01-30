    #class is define (class) keyword and class name : colon
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

#//////////////////////////////////////////////////////  30/1/2024 //////////////////////////////////////////////////////////#

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

#constructor pro ,constructor ko call karne ki zarorat nahi hoti ye khud se ho jata ahi object bnate hi 
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
# obj=C()
# obj.displayA()
# obj.displayB()
# obj.displayC()

    # Multilevel inheritance

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


class student:
    def __init__(self):
        self.__name=""
    def getname(self):
        return self.__name 
    def setname(self,name):
        self.__name=name

obj=student()
obj.setname('Testing')
name=obj.getname()
print(name)

