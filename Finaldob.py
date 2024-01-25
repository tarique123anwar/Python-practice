import random
from turtle import *
import math 
from turtle import*
import turtle
import random
import turtle as tur
import datetime
def f1():
          print("If you are not sure ,press the any key for play again ")
characters = ['ߎ', 'ߏ', 'ߐ']
def r():
    r=input("If you Sure,press and find the Gift (y)")
    if r=='y':
        turt=tur.Turtle()
        turt.screen
        tur.title("Birthday")
        turt.width(8)
        turt.color("cyan")
        new=tur.getscreen()
        turt.speed(10)

        new.bgcolor("green")

        turt.left(180)
        turt.penup()
        turt.forward(300)
        turt.right(90)
        turt.forward(100)
        turt.pendown()

        # Display H

        turt.forward(50)
        turt.right(90)
        turt.forward(50)
        turt.left(90)
        turt.forward(50)
        turt.left(90)
        turt.penup()
        turt.forward(50)
        turt.left(90)
        turt.pendown()
        turt.forward(50)
        turt.left(90)
        turt.forward(50)
        turt.right(90)
        turt.forward(50)

        # Display A

        turt.penup()
        turt.left(90)
        turt.forward(15)
        turt.pendown()
        turt.left(70)
        turt.forward(110)
        turt.right(70)
        turt.right(70)
        turt.forward(110)
        turt.left(180)
        turt.forward(55)
        turt.left(70)
        turt.forward(38)
        turt.left(70)
        turt.penup()
        turt.forward(55)
        turt.left(110)
        turt.forward(100)

        # Display P

        turt.left(90)
        turt.pendown()
        turt.forward(100)
        turt.right(90)
        turt.forward(50)
        turt.right(20)
        turt.forward(20)
        turt.right(70)
        turt.forward(40)
        turt.right(70)
        turt.forward(20)
        turt.right(20)
        turt.forward(50)
        turt.left(90)
        turt.forward(50)
        turt.left(90)
        turt.penup()
        turt.forward(100)

        # Display P

        turt.left(90)
        turt.pendown()
        turt.forward(100)
        turt.right(90)
        turt.forward(50)
        turt.right(20)
        turt.forward(20)
        turt.right(70)
        turt.forward(40)
        turt.right(70)
        turt.forward(20)
        turt.right(20)
        turt.forward(50)
        turt.left(90)
        turt.forward(50)
        turt.left(90)
        turt.penup()
        turt.forward(100)

        # Display Y

        turt.forward(20)
        turt.pendown()
        turt.left(90)
        turt.forward(50)
        turt.left(30)
        turt.forward(60)
        turt.backward(60)
        turt.right(60)
        turt.forward(60)
        turt.backward(60)
        turt.left(30)

        # go to Home

        turt.penup()
        turt.home()
        turt.color("yellow")
        new.bgcolor("blue")
        # setting second row

        turt.backward(300)
        turt.right(90)
        turt.forward(60)
        turt.left(180)

        # Display P

        turt.pendown()
        turt.forward(100)
        turt.right(90)
        turt.forward(50)
        turt.right(20)
        turt.forward(20)
        turt.right(70)
        turt.forward(40)
        turt.right(70)
        turt.forward(20)
        turt.right(20)
        turt.forward(50)
        turt.backward(50)
        turt.left(180)
        turt.right(20)
        turt.forward(20)
        turt.right(70)
        turt.forward(40)
        turt.right(70)
        turt.forward(20)
        turt.right(20)
        turt.forward(50)
        turt.right(90)
        turt.forward(10)

        # go to Home

        turt.penup()
        turt.home()

        # setting up

        turt.backward(200)
        turt.right(90)
        turt.forward(10)
        turt.left(90)
        turt.pendown()
        turt.forward(20)
        turt.penup()
        turt.home()

        # D

        turt.backward(150)
        turt.right(90)
        turt.forward(60)
        turt.pendown()
        turt.backward(100)
        turt.right(90)
        turt.forward(10)
        turt.backward(70)
        turt.left(180)
        turt.right(20)
        turt.forward(20)
        turt.right(70)
        turt.forward(88)
        turt.right(70)
        turt.forward(20)
        turt.right(20)
        turt.forward(70)
        turt.penup()
        turt.home()

        # set up for A

        turt.backward(50)
        turt.right(90)
        turt.forward(65)
        turt.left(90)

        # printing A

        turt.pendown()
        turt.left(70)
        turt.forward(110)
        turt.right(70)
        turt.right(70)
        turt.forward(110)
        turt.left(180)
        turt.forward(55)
        turt.left(70)
        turt.forward(38)
        turt.left(70)
        turt.penup()
        turt.forward(55)
        turt.left(110)
        turt.forward(100)

        # printing Y

        turt.pendown()
        turt.left(90)
        turt.forward(50)
        turt.left(30)
        turt.forward(60)
        turt.backward(60)
        turt.right(60)
        turt.forward(60)
        turt.backward(60)
        turt.left(30)

        #go to Home

        turt.penup()
        turt.home()
#/////////////////////////////////////////////
        today1 = datetime.datetime.now()
        tur.hideturtle()
        tur.penup()

        # Center the turtle at the top of the window
        tur.goto(0, tur.getscreen().window_height() / 3- 7)
        # Set text color
        tur.color("red")

        message = "Anwar! \nToday is " + today1.strftime("%A") + ', ' + today1.strftime("%d") \
                + ', ' + today1.strftime("%B") + ', ' + today1.strftime("%Y") 

        # Center the text
        tur.write(message, move=False, font=('arial', 15, 'bold'), align='center')

        turtle.exitonclick()
    elif r=='n':
        pass 
    else:
        print("please enter correct value")
while True:
    computer_count = 0
    user_count = 0

    play_game = int(input('''
                                Do you want to know your DOB ......
                                               Enter password to unlock GIFT
                                '''))

    if play_game == ord(''):
        # rounds_to_play = 3  # Adjust the number of rounds as needed

        # for _ in range(rounds_to_play):
        user_choice = int(input('''
CHOOSE ANY NUMBER
(1)\n(2) \n(3)                     
AND FIND OUT YOUR YEAR OF BIRTH (YYYY)
'''))
        if  user_choice <= 3:
            print("\n")
            # if user_choice in range(1,10):
            user_char = ord(characters[user_choice-1]) 
            computer_char = ord(random.choice(characters))
            print("Your Gussing ...", user_char)
            print("My Gussing...", computer_char)
            if user_char == computer_char:
                print("We are guessing equal" )
                computer_count += 1
                user_count += 1
                print("\n")
                f1()
                if r() == 'break':
                    break
            elif (user_char == ord('ߏ') and computer_char == ord('ߎ')) or \
                    (user_char == ord('ߎ') and computer_char == ord('ߐ')) or \
                    (user_char == ord('ߐ') and computer_char == ord('ߏ')):
                d=ord('ߨ')
                t=d-user_char
                print("You are right ","\nI thing Your age:-",t)
                print(ord(''),chr(47),ord(''),chr(47),user_char)
                user_count += 1
                print("\n")
                f1()
                if r() == 'break':
                    break
            else:
                d=ord('ߨ')
                w=d-computer_char
                computer_count += 1
                print("I am right","\nI thing Your age:-",w)
                print(ord(''),chr(47),ord(''),chr(47),computer_char)
                print("\n")
                f1()
                if r() == 'break':
                    break
        else: 
            print("Index out of range")
    else:
            print("please enter correct password")