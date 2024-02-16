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
        
num=int(input("Enter the num "))
rem=num % 2
if(num % 2==0):
# if(rem==0):
    print("Even")
else:
     print("Odd")


    #greatest num 
a=int(input("Enter 1st num  "))
b=int(input("Enter 2nd num  "))
c=int(input("Enter 3rd num  "))
if a>=b and b>=c:
    print("1st num largest",a)
elif b>=c:
     print("2nd num largest",b)
else:
     print("3rd num largest",c)


    #list appned method
list=['Anwar',21,'hyd',3.66]
list.append(4)  #this is a mutate
print(list)

    #sort method
list2=[66,21,4,3.66]
    # list.sort()
print(list2.sort())
print(list2)

    #sort(reverse=True) method
list2.sort(reverse=True) 
    #changes for original string

list2.reverse()

    #insert method
list2.insert(0,89)
print(list2)