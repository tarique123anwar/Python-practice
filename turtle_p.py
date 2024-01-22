# import turtle
# wn=turtle.Screen()
# wn.bgcolor('light green')
# wn.title("Happy DoB")
# s = turtle.Turtle()
# for i in range(5):
#  s.forward(30)
#  s.right(144)
# turtle.done()
# #/////////////////////////
import math 
from turtle import*
def hearta(k):
    return 15*math.sin(k)**3
def heartb(k):
    return 12*math.cos(k)-5*\
            math.cos(2*k)-2*\
            math.cos(3*k)-\
            math.cos(4*k)
speed(4)
bgcolor("black")
for i in range(30+1+25):
    goto(hearta(i)*5,heartb(i)*5)
    for j in range(5):
        color("#f73487")
    goto(0,0)
done()


#/////////////////

# import time
# from random import randint
# for i in range(1,85):
#     print('')
# space = ''
# for i in range(1,1000):
#     count = randint(1, 100)
#     while(count > 0):
#         space += ' '
#         count -= 1
#     if(i%10==0):
#         print(space + ':birthday:Happy Birthday!')
#     elif(i%9 == 0):
#         print(space + ":birthday:")
#     elif(i%5==0):
#         print(space +":yellow_heart:")
#     elif(i%8==0):
#         print(space + ":tada:")
#     elif(i%7==0):
#         print(space + ":chocolate_bar:")
#     elif(i%6==0):
#         print(space + "Happy Birthday!:sparkling_heart:")
#     else:
#         print(space + ":small_orange_diamond:")
#     space = ''
#     time.sleep(0.2)