     #1
def add(a,b):
    c=a+b
    print(c)
d=add(22,3)
print(d)

     #2
def aas(a,b):
    return a*b
w=aas(33,44)
print(w)

     #3
def ggg(a):
    return "anwar",a*333
print(ggg(2))

    #4
def ggg(e):
    return e*"Anwar"
e=int(input("enter the num"))
print(ggg(e))

    #5

def ggg(a):
    return a * "Anwar"

e = int(input(" "))
print(ggg(e), end='\n')  # 'end' parameter defaults to '\n', so you can omit it

        #6

class Student:
    def __init__(self, phy, chem, math) -> None:
        self.phy = phy
        self.chem = chem
        self.math = math

    @property
    def percentage(self):
       return (self.phy + self.chem + self.math) / 3 

# Create a Student instance
student = Student(88, 87, 99)

# Print the initial percentage
print(student.percentage)

# Change the physics marks
student.phy = 78

# Print the updated percentage
print(student.percentage)  