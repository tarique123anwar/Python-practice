class demoA:
    def disA(self):
        print("Welcome to Servicepack.ai A")
        
class demoB(demoA): # Using Inheritance
    def disB(self):
        print("Welcome to Servicepack.ai B")
o=demoB()
o.disA()
o.disB()
#//////////////
class a:
    def ss(self):
        print("Hello")
class b(a):
    def ss2(self):
        print("hello")
class c(b):     # Multilevel Inheritance
    def ss3(self): 
        print("hEllO")
o=c()
o.ss()
o.ss2()
o.ss3()

#Multiple Inheritance 

class a:
    def ss(self):
        print("Hello")
class b:
    def ss2(self):
        print("hello")
class c(a,b):     # Multilevel Inheritance
    def ss3(self): 
        print("hEllO")
o=c()
o.ss()
o.ss2()
o.ss3()


a=int(input("Pl Choose the any 3 number 1 to 3"))
if a==1:
    ff="I"
elif a==2:
    ff="L"
elif a==3:
 ff="U"
print(ff,a)