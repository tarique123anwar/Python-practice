# B=2
# A=4
# text="@"
# print(2*text*4)

# A,B="5",7
# T="@"
# print((A+T)*B)

# A,B=2,3
# C=4
# print(A+B*C)

#     #single line if s

# food=input("food :")
# eat="Yes" if food =="cake" else "No"
# print(eat)
 
#     #2nd////////////////////////

# food=input("food :")
# print("sweet") if food=="jalebi" else print("not sweet")


#     #clever if  ternary operator

# age=int(input("age :"))
# vote=("yes","no")[age>18]

# sal=float(input("Salary :"))
# tax=sal*(0.1,0.2)[sal<=50000]
# print(tax)
# print(input("name"))

#      #assig ope
# num=30
#      # num=num+30
# num+=30
# num*=30
# num-=30
# num**=30
# num%=30
# num/=30
# num//=30
# print(num)
#     #/////////////////////////////////
# age = 25
# category = "Teenager" if age < 18 else ("Adult" if age < 65 else "Senior")
# print(category)


# a=int(input("enter value 1st :"))
# b=int(input("enter value 2st :"))
# print(a>=b)
  
# value="this is str"
# value='this is str'
# value='''this is str'''

#     #this is false
#     # 'this is a python's classes'

#     #this is true
# "this is a python's classes"

#     #concatenation  ("hello"+"world")

# s="Tariq"
# c="Anwar"
# cc=c+" "+s
# print(len(cc))
# print(s[2],cc) #access indexing

#     #Slicing is very important in ML 
#                                 #(DOES NOT COUNT LAST INDEX)
# print(s[2:5],cc) #2 se 5 index tak 
# print(s[5:],cc) #5 se last tak


#     #vegative indexing 
# print(s[-2:-5],cc)

# print(cc.endswith("qqq"))

# print(cc.endswith("ar"))

#     #capitalize 
# r="hello ji"
# print(r.capitalize())

#     #replace fun

# str="Welcome to servicepack.ai"
# print(str.replace("e","a"))
# print(str.replace("servicepack.ai","company"))

#     #find fun 
# str="Tarique Anwar"
# print(str.find("Anwar"))


#     #count fun 
# str="Tarique Anwar"
# print(str.count("a"))

#     #nesting if statement

# age=70
# if age >= 18:
#     if age >= 75:
#         print("connot drive")
#     else:
#         print("can drive")
# else:
#         print("connot drive")


#     #even odd num 
        
# num=int(input("Enter the num "))
# rem=num % 2
# if(num % 2==0):
#     # if(rem==0):
#     print("Even")
# else:
#      print("Odd")


#     #greatest num 
# a=int(input("Enter 1st num  "))
# b=int(input("Enter 2nd num  "))
# c=int(input("Enter 3rd num  "))
# if a>=b and b>=c:
#     print("1st num largest",a)
# elif b>=c:
#      print("2nd num largest",b)
# else:
#      print("3rd num largest",c)

# 
#    # LIST IN PYTHON create [] list appned method

# list=['Anwar',21,'hyd',3.66]
# list.append(4)  #this is a mutate
# print(list)

#     #sort method
# list2=[66,21,4,3.66]
#     # list.sort()
# print(list2.sort())
# print(list2)

#     #sort(reverse=True) method
# list2.sort(reverse=True) 

#     #changes for original string
# list2.reverse()

#     #insert method  first old index  value and second new value 
# list2.insert(0,89)
# print(list2)

#     #remove method  remove the 1st element in this list

# lis=[2,1,4,5,1]

# lis.remove(1)
# print(lis)

#     #pop method provided option element is completely deleted 

# li=[2,1,4,5,1]    

# li.pop(3)
# print(li)

# #        #(TUPLE)tuple data type 

# tup=(2,1,4,5,1) #single value assign (2,)
# print(type(tup))
# print(tup[2])

#     #  tuple method 
#     #  (1)index method , index ko access kar sakte hain 
# tup=(2,1,4,5,1)

# print(type(tup))
# print(tup.index(5))
    
#     #(2)count method jo bhi elemnets ham pass karte hain wo kitni baar axist karta hai uska count mere pass return hoke aa jata hai 
# tup=(2,1,4,5,1)

# print(tup.count(1))

#     #question 1 string ko jod kar list bnani hai 

# movie=[]
# movie.append(input("Enter the 1st movie"))
# movie.append(input("Enter the 2st movie"))
# movie.append(input("Enter the 3st movie"))
# print(movie)

#      #second method this pro
# movie=[]
# mov1=input("ent v1")
# mov2=input("ent v2")
# mov3=input("ent v3")

# movie.append(mov1)
# movie.append(mov2)
# movie.append(mov3)
# print(movie)

#     #palindrome of elements (Hint use copy () method ) ["m","a","a","m"],[1 2 3 2 1]=  left to right and right to left are equal 

# l1=[1,2,1]
# l1=["m","a","a","m"]
# # l1=[1,2,3]
# copy_l1=l1.copy()
# copy_l1.reverse()
# if(copy_l1==l1):
#     print("palindrome")
# else:
#     print("not palindrome")


#     #Q 2 tuple 
# grade=("C","D","A","A","B","B","A")
# print(grade.count("A"))

#     #Q 3 list
# grade=["C","D","A","A","B","B","A"]
# grade.sort()
# print(grade)

    #DICTIONATY IN PYTHON  dic is mutable , does not stored index values and dic does not allowed duplicate keys like name and name 

from typing import Any


dic={
    "name" : "Anwar",
    "cgpa" : 9.7,
    "marks": [2,4,11,7]

}
print(dic)

info={ 
    "name": "servicepack",
    "sub" : ["python","C","java"],
    "topics" :("dic","set"),
    "age" : 25,
    "is_adult" : True,
    12.99 :94.4
}
print(info["name"],info["age"])
        #change assign value 
# info["name"]= "Anwar"
# print(info)
    #add new key value in prog
info["city"]="Hyderabad"
print(info)
    #create a empty DICTIONARY 
emp={} 
    #assign the value of.......
emp["name"]="tarique"
print(emp)


student ={
    "name":"ANWAR",
    "subjects": {
        "phy" : 97,
        "chem" : 99,
        "math" : 65
    }
}
print(student)

dictionary={
    "emp i_d" :          "eee",
    #this is key // this is the value
    "city" : "reee",
    "num" : "9209898766",
    "address" :"ooijihj7755"
}
print(dictionary)
print(dictionary["emp i_d"])

    #////////////////////
d={
    "name" : "A",
    "city" : "hy",
    "dis" : "mal",
    "add" : "vinayak n"

}
print(d)

    #DICTIONATY METHODS  myDic.keys() returns all keys

student ={
    "name":"ANWAR",
    "subjects": {
        "phy" : 97,
        "chem" : 99,
        "math" : 65
    }
}
print(student.keys())
print(list(student.keys()))

    #DICTIONATY METHODS  myDic.values() return all values 

print(student.values())


    #DICTIONATY METHODS  myDic.items() return all (key ,value ) pairs as tuples  

print(list (student.items()))
pairs =list (student.items())
print(pairs[0])

     #DICTIONATY METHODS  myDic.get() return the key according to value

print (student.get("name"))  # no return error ---->None . print (student.get("name2")) 
print(student["name"]) #return error                     . print(student["name"])

 #DICTIONATY METHODS  myDic.update() return the key according to value

student ={
    "name":"ANWAR",
    "subjects": {
        "phy" : 97,
        "chem" : 99,
        "math" : 65
    }
}
student.update  ({"city":"hyderabad", "pin":17})
print(student)

    #SET IN PYTHON ,set is the collection of the unordered items each element in the set must be unique & mutable but set elemnts is immutable  NUM={22,33,2,SS,RR} IGNORE duplicate values 
s={22,43,22,"anwar","anwar","t"}
print(s)
print(type(s))
    #how to create empty set

col=set()
print(type(col))
 
    #SET METHODS   set is mutable but set elements is immutable 

    #(1)set.add() adds an element 

coll=set()
coll.add(1)
coll.add(2)
coll.add("servicepack")
coll.add((2,44,3,1,33))
    #coll.add([2,44,3,1,33]) does not support list 
print(len(coll))

      #(2)set.clear() removes the element an 

coll.clear()
print(len(coll))

    #set pop() removes a random value 

co={"hello","welcome","hi"}
print(co.pop())
print(co.pop())
print(co.pop())
                        
    #/////////////////////////// practice
dicc={
    "1":"a",    
    "2":"b",
    "3":"c"
}
print(dicc.keys())
print(dicc.values())
print(dicc.items())
print(dicc.get(0))
print(dicc["1"])


    #set.union(set2) combines both set values & returns new  21/2/2024  

set1={1,2,3}
set2={2,3,4}
print(set1.union(set2)) # o/p {1,2,3,4}
    #agian run simply 
print(set1)
print(set2)

    #set.intersection(set2) combines common values & returns new set1={1,2,3}
set1={1,2,3}
set2={2,3,4}
print(set1.intersection(set2)) # o/p  {2,3}
    #again run simply 
print(set1)
print(set2)

    #practice Q 1
D={
    "cat": "a small animal ",
    "table" : ["wooden ","steal"]
}
print(D)

    #practice Q 2
sub={
    "python ","java","c++", "python ","javascript","java",
    "python","java","c++","c"
}
print(sub)

    #practice Q 3
marks={}
x=int(input("enter the math"))
marks.update({"math":x})

x=int(input("enter the phy"))
marks.update({"phy":x})

x=int(input("enter the com"))
marks.update({"com":x})

print(marks)

    #practice 

subj_st={}  

s=int(input("enter the com"))
subj_st.update({"com":s})

s=int(input("enter the math"))
subj_st.update({"math":s})

s=int(input("enter the chem"))
subj_st.update({"chem":s})

print(subj_st)

    #store the value of 9,9.0 in set

value_set={9,9.0}  #doesn't support 
value_set={9,"9.0"} #Its support 
value_set={"int":9,"float":9.0} #Its support 
print(value_set)                                         #FINISHED CHAPTER 4th 

         #(5) CHAPTER 5th LOOP IN PYTHON ,TWO TYPES OF LOOP (for) & (while)
# while True:
#     print("servicepack.ai")
count=1

while count<=5:
    print("servicepack.ai")
    count+=1 
    #/////////////////////////////
    num=1
while num<=20:
    print("servicepack.ai",num)
    num+=1

        #  Qs 1 ////////////////////////////

i=1
while i<=50:
    print(i)
    i+=1
        # Qs 2 ////////////////////// reverse print num
i=100
while i>=1: #this is a stoppint condition 
    print(i)
    i-=1

        # Qs 3 ////////////////////// print the table
# i=1
# while i<=10:
#     n=int(input("which table r u taking"))
#     print(n*i)
#     i+=1
n = int(input("Enter the number for the table: "))
i = 1
while i <= 10:
    # print(n*i)  #
    print(f"{n} x {i} = {n*i}")
    i += 1 

    # Qs 4 ////////////////////// print the table

    num2=[2,44,55,77,89,99,100]
    idx=0
    while idx < len(num2):
        print(num2[idx])
        idx+=1

    # Qs 5 ////////////////////// fiding index
        
num2=(2,44,55,77,89,99,100)
x=77
i=0
while i < len(num2):
    if (num2[i]==x):
        print("FOUND IT" ,i)    
    else:
        print("finding")
    i+=1

    #practice
f=int(input("Enter \n"))
j=1
while j<=10:
    print(f*j)
    j+=1

    #////////////

r=[4,5,33,44,32,22,12]
t=0
while t<len(r):
    print(r[t])
    t+=1
    #/////////////// finding the values

v=(22,44,56,78,98,78,200)
l=78
z=0
while z<len(v):
    if (v[z]==l):
        print("found",z)
    else:
        print("finding")
    z+=1
    #/////////////////
    
v=(22,44,56,78,98,78,200)
l=78
z=0
while z<len(v):
    if (v[z]==l):
        print("found",z)
    else:
        print("finding")
    z+=1
    #///////////////////////
bb=[4,44,23,"ddd",3.87]
e=0
while e < len(bb):
        print(bb[e])
        e+=1
    #break keyword jahan pe ham break likhte hain wahi pe program rukh jayega aage execute nahi hoga 
i=1
while i<=5:
    print(i)
    if(i==3):
        break
    i+=1
print("End of loop")

    #///////////////

v=(22,44,56,78,98,78,200)
l=78
z=0
while z<len(v):
    if (v[z]==l):
        print("found",z)
        break
    else:
        print("finding")
    z+=1
print("end of loop")

        #continue statement 
i=0
while i<=5:
    if(i==3):
        i+=1
        continue #skip
    print(i)
    i+=1 

    #skip even number PRINT ONLY ODD NUM
i=0
while i<=5:
    if(i%2==0):
        i+=1
        continue #skip
    print(i)
    i+=1

     ##skip ODD number PRINT ONLY EVEN NUM
i=0
while i<=5:
    if(i%2 !=0):
        i+=1
        continue #skip
    print(i)
    i+=1

        #for loop in python 
print("others") 
f=[2,4,5,6,77]
for val in f:
    print(val)
    #////////////////////
fruits=["banana","litchi","graps"]
for fr in fruits:
    print(fr)\

        #////////////////
tup=(2,45,66,5,43,67,98)
for n in tup:
    print(n)

str="servicepackai"
for char in str:
    if(char=='a'):
        print("a found")
        break
#     print(char)
# else:
    print("end")
    #///////////////
nums=[3,4,5,66,77,89,90,900]
for el in nums:
    print(el)

    #//////////////
nums=(3,4,5,66,77,89,90,900,66)
y="66"
ind=0
for el in nums:
    if(el==y):
        print("number found at ind",ind)
    ind +=1

    #range() function 

seq=range(5)
for i in seq:
    print(i)

    #///////////////

for i in range(20):
    print(i)

    # 1 step//////////////////// starting value and stopping value
for i in range(4,20):
    print(i)

    # 2 step/////////////////// step size like 2 and 2 and 2

for i in range(4,20,4): #step size 2 
    print(i)
# print("select",i)
    #//////////////
o=[22,44,56,54,566,434]
for s in o:
    print(o)

    #//////////////
o=[22,44,56,54,566,434]
for s in o:
    print(s)
    # pass
    #/////////////
name=("anwar","ali","sohel","asif","lee")
for h in name:
    print(h)
    # pass

    #negative step size 
for i in range(50,0,-1): #step size 2 
    print(i)
    # print("other")

    #from user input 
print("other")
u=int(input("Enter the number "))
for w in range(1,11,1):
    print(w*u)

    #pass statment jab kisi statement ko print nahi karna hota hai to pass ka use karte hain 

for r in range(10):
    #empty
    # pass
    print("some usefull work")

    #(1Q) sum of numbers using for
n=7
sum=0
for i in range(1,n+1):
    sum+=i
print("total sum =",sum)


     #(Q1) sum of numbers using while (real number is the)
n=5
sum=0
i=1
while i<=n:
    sum+=i
    i+=1
print("total sum =",sum)

    #Q2 factorial number using while 
n=5
fact=1
i=1
while i<=n:
    fact*=i
    i+=1
print("fac=",fact)

     #Q2 factorial number using for

n=7
fact=1
for i in range(1,n+1):
    fact*=i
print("fac=",fact)


    #PRACTICE
d=8
s=0
for u in range(1,d+1):
    s+=u
print("T",s)

    #//////
l=5
ss=0
j=1
while j<=l:
    ss+=j
    j+=1
print("tl",ss)

    #/////////////
l=7
w=0
for o in range(1,l+1):
    w+=o
print("Total",w)

    #/////////////
f=8
e=0
k=1
while k<=f:
    e+=k
    k+=1
print("rrr",e)

    #////////////

w=5
f=1
for s in range(1,w+1):
    f*=s
print("used for ,  ddd",f)

    #////////////
r=5
t=1
f=1
while f<=r:
    t*=f
    f+=1
print("used while ,  sasas",t)

        #FUNCTION IN PYTHON ,fun is a block of statements that perform a specific task

def f():
    '''add two num'''
    k=22+34
    print("funcccc",k)
f()
    #///////////////

def ee(n,m):
    '''sub two num'''
    sum=n-m
    print(sum)
    return sum 
ee(33,44)
print("hello func")

    #deff
ee(33,32)

    #deff
ee(44,33)

        #fun2
#function definition 
def cal_sum(a,b): #parameters
    return a+b  

s=cal_sum(22,33) #function call ,arguments  
print(s)

    #///////////
def pri_hello():
    print("Hello")
pri_hello()
pri_hello()
pri_hello()

    #///////////
def calc_avg(a,b,c):
    sum=a+b+c
    avg=sum/3
    print(avg)
    return avg
calc_avg(55,78,92)

        #TYPES OF FUNCTION 
        #1 Built-in  ----> print() , len() ,type() , range() jo pahle se hai 
        #2 User-defined ----> jisko han define karte hain


def cal(a=2,b=22):  #default values 
    print(a*b)
    return a*b
cal(1)

        #Q1 WAF to print the lentrh of a list (list is the parameter)

cities=["delhi","mumbai","patna","hyderabad","bengaluru "]
actor=["srk","sallu","amir","ntr"]
def f_len(list):
    print(len(list))       
f_len(cities)
f_len(actor)

def p_len(list):
    for item in list:
        print(item,end=" ")   
f_len(cities)

        #Q2 FACTORIAL using function 

def call(n):
    fact=1
    for i in range(1,n+1):
        fact*=i
        print(fact)
call(7)

        # Q3 WAF to convert USD to INR 
 
def converter(usd_val):
    inr_val=usd_val*83
    print(usd_val,"USD =",inr_val,"INR")
converter(1)

    #///////////////

def con(usd):
    inr=usd*83
    print(usd,"usd =",inr,"INR")
a=int(input("Enter the INR ..."))
con(a)  

        #RECURSION  
        #When a fun calls itself repeatedly.
def show(n):
    if(n==0):
        return
    print(n)
    show(n-1) #recursion
    print("end")
show(3)

    #//////////////

def r(m):
    if(m==0):
        return
    print(m)
    r(m-1)
r(4)
print("other")
    #////////////

def recursion(d):
    if(d==0):  #base case is a very important in recursion
        return
    print(d)
    recursion(d-1)
    print("real")
    print("recursion")
recursion(5)

        #////////////////
def r1(q):
    if(q==0):
        return
    print(q)
    r1(q-1)
    print("hye")
r1(29)

        #practice Q1 WAR fun to calculate the sum of first n natural number 
def cal(n):
    if(n==0):
        return 0
    return cal(n-1)+n
sum = cal(5)
print(sum)

    #/////////////
def ddd(k):
    if (k==0):
        return 0
    return ddd(k-1)+k
s=ddd(4)
print(s)
()
        #WAR fun to print all elements in a list 
        #Hint : use list & index as parameters 

        #///////////////////////////// CHAPTER 7 File I/O //////////////////////////////////



# f=open("demo.txt","r")
# line1=f.readline()
# print(line1)
# line2=f.readline()
# print(line2)
# data=f.read()
# data=f.read(3) #character ko bhi read kar sakte hin 
# print(data)
# print(type(data))///////
# f.close()
    #/////////////////////
# ff=open("demo.txt","r") # if we 
# # data1=ff.read()
# line1=ff.readline(5)
# print(line1)
# ff.close()

# #////////////
# ff=open("demo.txt","r+") # 
# # ff.write("abc")
# print(ff.read())
# ff.close()

#     # write 

# ff=open("demo.txt","w+") # write mode
# ff.write("abc")
# print(ff.read())
# ff.close()


#     #appned mode
# ff=open("demo.txt","a+") # append mode
# # ff.write("abc")
# print(ff.read())
# ff.write("abc") 
# ff.close()


        #open file with open (read)

# with open("demo.txt","r")as f:
#     da=f.read()
#     print(da) #automatically close this file does not need to close 

#         #write mode
# with open("demo.txt","w")as f:
#     f.write("new data ")
#     #same practice 
# with open ("demo.txt","w") as g:
#     g.write("Anwar")
    
#     #//////////////////////////
# with open("demo.txt","r") as a:
#     data=a.read(3)
#     print(data)


#         #deliting a file 
    
# import os
# os.remove("demo.txt")

        # (Q1)  #how to create a new file

with open("practice.txt","w") as i:
    i.write("Hi everyone\n we are learnin File I/O \n")
    i.write("using python.\nI like programmimg in python.")

        # (Q2)data changes and replace 
with open("practice.txt","r")as i:
    data=i.read()
new_data=data.replace("python","java")
print(new_data)

with open("practice.txt","w")as i:
    i.write(new_data)

        # (Q3) search if the word 'learning', axixst in the file or not 
word="learnin"
with open("practice.txt") as i :
    data=i.read()
    if(data.find(word) !=-1): #find is a keayword finding the words 
        print("Found")
    else:
        print("not found")


        #sane pro with fun 
def check_for_word():
    word="learnin"
    with open("practice.txt") as i :
        data=i.read()
        if(data.find(word) !=-1): #find is a keayword finding the words 
            print("Found")
        else:
            print("not found")
check_for_word() #fun call :

#/////////////////////////
# for _,row in df.iterrows():
#     output = llm_api(row['input'],prompt,system_prompt)
#     print(_,"clean_output",output)

# #/////////////////////////
# for _,row in df.iterrows():
#     output = llm_api(row['input'],prompt,system_prompt)
#     print(_,"clean_output",output)\
# #/////////////////////////
# for _,row in df.iterrows():
#     output = llm_api(row['input'],prompt,system_prompt)
#     print(_,"clean_output",output)

        #/////////////////////////////
def check():
    d="File"
    with open("practice.txt") as i:
        s=i.read()
        if (s.find(d)!=-1):
            print("found")
        else:
            print("not found")
check()

        #   OOPS PROGRAMMING IN PYTHON 
    #to map with real world scenarios ,we started using object in code. (MONDAY 4/May/2024)

            #OBJECT AND CLASS 
class Student:
    name="Anwar"
s1=Student()
print(s1.name)

s2=Student()
print(s2.name)

        #//////////////////////
class Car:
    color="green"
    brand="mercedes"
car1=Car()
print(car1.color)
print(car1.brand)

        #practice
class S:
    w="realcar"
d=S()
print(d.w)

    #/////////

class Fin:
    building="headquater"
    bui="head"
g=Fin()
print(g.building)
g2=Fin()
print(g.bui)


            #CONSTRUCTOR FUNCTION __init__ (constructor is call automatic)
class Student:
    name="Anwar"
    def __init__(self) -> None:
        print(self)
        print("adding new student in Datebase ...")
s1=Student() #call automatically 
# print(s1.name)

# s2=Student()
# print(s2.name)

    #///////////
class read:
    k="aap ka hai "
    def __init__(self) -> None:
        print("this is a constructor")
c=read()

    #////////////
class ready:
    m="real number "
    def __init__(self,fullname) -> None:
       self.name=fullname
       print("welcome Anwar")
ff=ready("Rehan")
print(ff.name)
ff2=ready("arjun")
print(ff2.name)

    #/////////////
class anw:
    b="arshad"
    def __init__(self,name,marks) -> None:
        self.name=name
        self.marks=marks
        print("ye mera cons... hai ")
d1=anw("raja",65)
print(d1.name,d1.marks)
d2=anw("rani",98)
print(d2.name,d2.marks)
# really="ppp"


        #default constructor.
class dell:
    def __init__(self):
        pass

        #parameterized constructor.
    def __init__(self,naam,fulnam) :
        self.naam=naam
        self.fulnam=fulnam
        print("passing parameters")
hy=dell("dell","_laptop")
print(hy.naam,hy.fulnam)
hy=dell("dell_lappy","_adapter")
print(hy.naam,hy.fulnam)

        #CREATE A METHOD 


class dell:
    company_name="Servicepack.ai"   #this is class attribute 
    def __init__(self,naam,fulnam) :
        self.naam=naam              #this is object attribute 
        self.fulnam=fulnam

    def welcome (self): #its a method
        print("welcome to empolyees",self.naam)

    def which_lappy(self):  #its a another method with return keyword
        return self.fulnam
    
hy=dell("lenovo","_laptop")
# print(hy.naam,hy.fulnam)
hy.welcome()
print(hy.which_lappy)

#practice Q1 create student class that takes name $ marks of 3 subject as arguments in constructor .
    #The create a method to print the average.

class Stu:
    def __init__(self,name,marks) -> None:
        self.name = name
        self.marks = marks

    def get_avg(self):
        sum=0
        for val in self.marks:
            sum +=val
        print("Hi",self.name,"ur avg score is ",sum/3)

s1=Stu("actual",[99,76,66])
s1.get_avg()

s1.name="really"  #directly name changing method 
s1.get_avg() 

        #STATIC METHODS
    #Methods that do not use the self parameter (work at class level) isme self parameter ki zaroorat nahi hoti 

class Studennts:
    @staticmethod  #decorator
    def college():
        print("Manuu")


            # ABSTRACTION  
                    #Hiding the implementation details of a class and only showing the essential feautures to the user. 
        
# class Cars:
    # def __init__(self) -> None:
    #     self.acc=False
    #     self.brk=False
    #     self.clutch=False

#     def start(self):
#         self.clutch=True
#         self.acc=True
#         print("car started ........")
# car1 = Cars()
# car1 . start()

            
#             #ENCAPSULATION 
#                     #Wrapping data and functions into a single unit (object)

# class carr:
#     def st(self):
#         self.clutch=True
#         self.acc=True
#         print("Started now...............")
# ob1=carr
# ob1.st()

        #////////////////////
class bikes:
    def __init__(self) -> None:
        self.acc=False
        self.brk=False
        self.clutch=False
    
    def s(self):
        self.acc=True
        self.clutch=True
        print("Bike started-_-_-_-_-_-.....")
b=bikes()
b.s()

class bi:
    def __init__(self) -> None:
        self.acc=False
        self.brk=False
        self.clutch=False
    
    def st(self):
        self.clutch=False
        self.acc=False
        print("bike ja rahi hai...")
e=bi()
e.st()


#             #ENCAPSULATION 
#                     #Wrapping data and functions into a single unit (object)


        #Q Bank account management system in 
class Account:
    def __init__(self,bal,acc) -> None:
        self.balance=bal
        self.account_no=acc

    #debit method 
    def debit(self,amount):
        self.balance-=amount
        print("Rs",amount,"was debited")
        print("total balance =",self.get_balance())

    #credit method 
    def credit(self,amount):
        self.balance+=amount
        print("Rs",amount,"was credited")
        print("total balance =",self.get_balance())
    
    #return final balace
    def get_balance(self):
        return self.balance

acc1=Account(10000,98711232121332)
acc1.debit(1000)
acc1.credit(5000)
acc1.credit(25000)
acc1.debit(7000)
acc1.credit(250)


        #OOPS DEL KEAYWORD (del)
        #used to delete object properties or object itself 

# class aap:
#     def __init__(self,name) -> None:
#         self.name=name
# s1=aap("tarique")
# print(s1.name)
# del s1.name    #its deleted.
# print(s1.name)

#         #PRIVATE(like) attributes & methods 

# class acccount:
#     def __init__(self,acc_no ,acc_pwd) -> None:
#         self.acc_no=acc_no
#         self.__acc_pwd=acc_pwd  # kisis bhi attribute ko private karne ke liye ham uske aage 2 underscore lga dete hain (__acc_pwd)
    
#     def reset_pwd(self):
#         print(self.acc_pwd)
# acc1=acccount("12345","xyzzz")
# print(acc1.acc_no)
# print(acc1.reset_pwd())

#         #///////////////

# class person:
#     __name="pahla"
#     def __hello(): 
#         print("hello person!")

#     def welcome(self):
#         self.__hello()
# p1=person()
# print(p1.__hello())

            #INHERITANCE.
                    #when one class (child/derived) derived the properties & method of another class (parent/base).


# class std:
#     def __init__(self,phy,chem,math) -> None:
#         self.phy=phy
#         self.chem=chem
#         self.math=math

#     @property
#     def percentage(self):
#         return ((self.phy + self.chem + self.math)/3) + "%"

# st=std(88,87,99)
# print(st.percentage)
#         #i am changing the marks
# st.phy = 78
# print(st.percentage)


        #/////////////////   GPT type

class Student:
    def __init__(self, phy, chem, math) -> None:
        self.phy = phy
        self.chem = chem
        self.math = math

    @property
    def percentage(self):
        # return "{:.2f}%".format((self.phy + self.chem + self.math) / 3)  
        return (self.phy + self.chem + self.math) / 3  

# Create a Student instance
student = Student(88, 87, 99)

# Print the initial percentage
print(student.percentage)

# Change the physics marks
student.phy = 78

# Print the updated percentage
print(student.percentage)  

        #POLYMORPHISM : 
                #OPERATOR OVERLOADING 
                            #when the same operator is allowed to have different meaning according to the context.

class complex:
    def __init__(self,real,img) -> None:
        self.real=real 
        self.img=img

    def ShowNum(self):
        print(self.real,"i +",self.img,"j")

    def __sub__(self,num2):                #USING DUNDER FUN __add__()
        newreal=self.real-num2.real
        newimg=self.img-num2.img
        return complex(newreal,newimg)


num1=complex(1,3)   
num1.ShowNum()    

num2=complex(4,7)
num2.ShowNum()   

# num3=num1.add(num2)
num3=num1 - num2 
num3.ShowNum()


            #***MINI PROJECT USING  RANDOM NUM***

# import random

# target=random.randint(1,30)

# while True:
#     uch=input("Guess the target or Quit (Q)")
#     if (uch=="Q"):
#         break
#     uch=int (uch)
#     if(uch==target):
#         print("Success : Correct Guess!!")
#         break
#     elif(uch<target):
#         print("ur num small .pl take big num")
#     else:
#         print("ur num big .pl take small num")
# print("___GAME OVER__")


# import random
# t=random.randint(1,20)

# while True:
#     userneliya=input("Guess the num or(Q)")
#     if(userneliya=="Q"):
#         break
#     userneliya=int(userneliya)
#     if (userneliya==t):
#         print("Successful: Correct Guess!!")
#         break
#     elif(userneliya <t):
#         print("ur num too small ,pl big ")
#     else:
#         print("ur num too big ,pl small ")

# print("__GAME OVER__")


        #generate  password
import random
import string

pass_len=6
charVal=string.ascii_letters + string.digits + string.punctuation
password=""
for i  in range(pass_len):
    password+=random.choice(charVal)
print("Your password is :",password)


1