import random
from turtle import *
import math 
from turtle import*
import turtle
import random
import turtle as tur
import datetime
def f1():
          print("If you are not sure,press any key to play again.. ")
characters = ['ߎ', 'ߏ', 'ߐ']
def r():
    r=input("If you sure,press (y) and find the GIFT in your taskbar.\n")
    if r=='y':
        #time
        today1 = datetime.datetime.now()
        tur.hideturtle()
        tur.penup()

        # Center the turtle at the top of the window
        tur.goto(0, tur.getscreen().window_height() / 3- 7)
        # Set text color
        tur.color("red")

        message = "Nitheesha Sanikommu! \nMay ALLAH give uh long life and fulfill all ur wishes & make the coming days good.\n\nToday is " + today1.strftime("%A") + ', ' + today1.strftime("%d") \
                + ', ' + today1.strftime("%B") + ', ' + today1.strftime("%Y") 

        # Center the text
        tur.write(message, move=False, font=('arial', 12, 'bold'), align='center')

        #happy
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
        new.bgcolor("black")
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
        turt.right(90)
        # turt.forward(215)
        # turt.right(20)
        # turt.forward(200)
        # turt.right(90)

        #color

        turt.color("blue")
        new.bgcolor("black")

        # setup
        turt.penup()
        turt.left(90)
        turt.forward(80)
        turt.left(90)
        turt.forward(7)

        turt.forward(100)

        # design

        #design pattern
        turt.home()
        turt.forward(200)
        turt.pendown()
        turt.color("PURPLE")
        turt.width(3)
        turt.speed(0)

        def squre(length, angle):

            turt.forward(length)
            turt.right(angle)
            turt.forward(length)
            turt.right(angle)

            turt.forward(length)
            turt.right(angle)
            turt.forward(length)
            turt.right(angle)

        squre(80, 90) 

        for i in range(30):
            turt.right(10)
            squre(80, 90)

        # tur.mainloop()
        def hearta(k):
            return 16 * math.sin(k) ** 3

        def heartb(k):
            return 13 * math.cos(k) - 5 * math.cos(2 * k) - 2 * math.cos(3 * k) - math.cos(4 * k)

        def draw_heart():
            turtle.color("red")
            turtle.begin_fill()

            turtle.penup()       #changes
            turtle.goto(hearta(0) + 200, heartb(0))  # Adjust the x-coordinate to move to the right
            turtle.pendown()

            for i in range(360):
                k = math.radians(i)
                x = hearta(k) + 200  # Adjust the x-coordinate to move to the right
                y = heartb(k)
                turtle.goto(x, y)

            turtle.end_fill()

        # Create a turtle
        turt = turtle.Turtle()
        turt.speed(3)

        # Draw the heart on the right side
        draw_heart()
        # Keep the window open
        # turtle.done()
        # turtle.exitonclick()
        #/////////////////////////////
    elif r=='n':
        pass 
    # else:
    #     print("Please enter correct value")
while True:
    computer_count = 0
    user_count = 0
    p = int(input('''
                                Do you want to know your DOB ......
                                               Enter password to unlock GIFT.
                                '''))
    if p == ord(''):
        # for _ in range(rounds_to_play): 
        
        user_choice = int(input('''
CHOOSE ANY NUMBER AND FIND OUT YOUR YEAR OF BIRTH (YYYY)
                        
Isn't ur year of birth nineteen ninety eight ? press (1)
                                
        Isn't ur year of birth nineteen ninety nine ? press (2)
                                
                Isn't ur year of birth two thousand ? press (3)
'''))
        if  user_choice <= 3:
            print("\n")
            # if user_choice in range(1,10):
            user_char = ord(characters[user_choice-1]) 
            computer_char = ord(random.choice(characters))
            print("\nThis is your value ...", user_char)
            print("\nI guessed value...", computer_char)
            if user_char == computer_char:
                print("\nWe have entered the same values" )
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
                print("\nAre you right ?","\nI thing Your age:-",t)
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
                print("\nAm i right ?","\nI think your age is  :-",w)
                print(ord(''),chr(47),ord(''),chr(47),computer_char)
                print("\n")
                f1()
                if r() == 'break':
                    break
        else: 
            print("Index out of range")
    else:
            print("\nThis is a wrong pswd : Please enter correct pswd")