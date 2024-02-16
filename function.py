#     #without arguments 
# def fun():
#     print("Anwar")
# fun()

#     #with arguments 
# def fun2(name):
#     print(name)
# fun2('Ali')
# fun2('Anwar')
# fun2('Tarique')

#     #return fun
# def fun3(x):
#     '''
#     This is the return fun values
#     '''
#     return x**2
# x=float(input("Enter the Value:"))
# o=fun3(x)
# print('Ur values are :-',x,"is",o)

    # practice //////////////////////////////////

def add(num1: int, num2: int) -> int:
    """Add two numbers"""
    num3 = num1 + num2
 
    return num3
 
# Driver code
num1=22 
num2 = 5
ans = add(num1, num2)
print("toatal num = ",ans)

    #1//////////////////////////
def p1():
    print("Welcome to Servicepck.ai")

p1()

    #2////////////////

def p2(name):
    print(name)
a=input("enter the name of c")
p2(a)

    #3///////////////////////////

def p3(num1):
    '''mul two numbers'''
    return num1*4

r=p3(3)
w=p3(4)
e=p3(2-2)
x=input("Enter the value ")
print("mul two of ..",r,w,e,x*(+4))

    #/////////////////////////
def pri1(n):
    i=input("Enter the value")
    print(i,n)
pri1("anwar")