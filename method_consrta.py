class d:
    t=49
    def __init__(self): #this is a constructor fun
        print("welcome to Servicepack.ai")
    def show(self): #this is a fun
        self.c=self.t*self.t #this is a variable & * but mandotary use self 
        print(self.c)
    def showv(self,a,b): # another fun
        print(a+b)
o=d()  
o.show() #this is a  calling a class by object
o.showv(39,44) #this is a object calling for class with parameters 

#///////////////
class demo:
    r=33
    def __init__(self):
        print("Welcome to dealGo store")
    def sh(se):
        se.s=se.r*se.r
        print(se.s)
    def sho(se,Anwar,Ali):
        print(Anwar+Ali)
x=demo()
x.sh()
x.sho(33,44)
