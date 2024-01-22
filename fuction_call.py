def a():
    print("welcome to servicepack")
a()

    #fun with arguments 
def f(a,b):
    print(a+b)
f(70,90) 
f(44,55)  
f(50,94) 
    #first_default parameter value 
def d(a,b=56):
    print(a+b)
d(30)
  #sec_default parameter value 
def d(a,b=56):
    print(a+b)
d(20+30) 
    #return
def r(w):
    return w*w,w*2
q=r(4)
print(q)
    #/////////////////////
def a(a,b):
    print(a**b)
a(30,78)