def fun():
    print("Anwar")
fun()

def fun2(name):
    print(name)
fun2('Ali')
fun2('Anwar')
fun2('Tarique')

def fun3(x):
    '''
    This is the fun return values
    '''
    return x**2
x=float(input("Enter the Value:"))
o=fun3(x)
print('Ur values are :-',x,"is",o)