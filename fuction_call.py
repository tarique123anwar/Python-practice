def a():
    print("welcome to servicepack")
a()

    #fun with arguments 
def f(a,b):
    return a+b

print(f(70,90))
value = f(44,55) 
print(value-10) 
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