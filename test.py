import math
import turtle as turt

def hearta(k):
    return 15 * math.sin(k) ** 3

def heartb(k):
    return 12 * math.cos(k) - 5 * \
           math.cos(2 * k) - 2 * \
           math.cos(3 * k) - \
           math.cos(4 * k)
turt.penup()
# turt.goto(hearta(0) + 200, heartb(0))  # Adjust the x-coordinate to move to the right
turt.pendown()
turt = turt.Turtle()
turt.screen.bgcolor("black")
turt.speed(4)

# Draw the heart shape
for i in range(30 + 1 + 25):
    turt.goto(hearta(i) * 2, heartb(i) * 2)
    for j in range(5):
        turt.color("#f73487")
    turt.goto(0, 0)

#//////////////////////////////

# # # Move the turtle to the right side
# # turt.penup()
# # turt.goto(250, 0)  # Adjust the x-coordinate to move it further right
# # turt.pendown()

# # # Display text on the right side
# # turt.color("white")
# # turt.write("Right Side", align="center", font=("Arial", 16, "normal"))

# # turt.done()


# import turtle

# def write_text(text, y_position):
#     turtle.penup()
#     turtle.goto(0, y_position)
#     turtle.pendown()
#     turtle.write(text, align="center", font=("Arial", 16, "normal"))

# # Create a turtle
# turt = turtle.Turtle()
# turt.speed(1)

# # Write text on different lines 
# write_text("Line 1", 50)
# write_text("Line 2", 0)
# write_text("Line 3", -50)

# # Keep the window open
# turtle.done()
    
    #////////////////////

# import turtle as t

# print("Anwar")
# t.write(font=("Arial", 50,"bold","italic"))

# t.hideturtle()
# t.done()

# from turtle import *
# import turtle
# import datetime

# tur = turtle.Turtle()

# today1 = datetime.datetime.now()
# tur.hideturtle()
# tur.penup()

# tur.backward((tur.getscreen().window_width() / 2) - 10)
# message = "Anwar! \nToday is " + today1.strftime("%A") + ', ' + today1.strftime("%d") \
#            + ', ' + today1.strftime("%B") + ', ' + today1.strftime("%Y") 

# tur.write(message,move=False, font=('arial',10,'bold'),align='left')
# turtle.exitonclick()


# from turtle import *
# import turtle
# import datetime
# import turtle
# import math
# tur = turtle.Turtle()

# today1 = datetime.datetime.now()
# tur.hideturtle()
# tur.penup()

# # Center the turtle at the top of the window
# tur.goto(0, tur.getscreen().window_height() / 4- 10)

# # Set text color
# tur.color("red")

# message = "Anwar! \nToday is " + today1.strftime("%A") + ', ' + today1.strftime("%d") \
#            + ', ' + today1.strftime("%B") + ', ' + today1.strftime("%Y") 

# # Center the text
# tur.write(message, move=False, font=('arial', 15, 'bold'), align='center')

# turtle.exitonclick()

# import turtle
# import math

# def hearta(k):
#     return 16 * math.sin(k) ** 3

# def heartb(k):
#     return 13 * math.cos(k) - 5 * math.cos(2 * k) - 2 * math.cos(3 * k) - math.cos(4 * k)

# def draw_heart():
#     turtle.color("red")
#     turtle.begin_fill()
    
#     turtle.penup()
#     turtle.goto(hearta(0), heartb(0))
#     turtle.pendown()

#     for i in range(360):
#         k = math.radians(i)
#         x = hearta(k)
#         y = heartb(k)
#         turtle.goto(x, y)

#     turtle.end_fill()

# # Create a turtle
# turt = turtle.Turtle()
# turt.speed(2)

# # Draw the heart
# draw_heart()

# # Keep the window open
# turtle.done()

# import turtle
# import math

# def hearta(k):
#     return 16 * math.sin(k) ** 3

# def heartb(k):
#     return 13 * math.cos(k) - 5 * math.cos(2 * k) - 2 * math.cos(3 * k) - math.cos(4 * k)

# def draw_heart():
#     turtle.color("red")
#     turtle.begin_fill()
    
#     turtle.penup()       #changes
#     turtle.goto(hearta(0) + 150, heartb(0))  # Adjust the x-coordinate to move to the right
#     turtle.pendown()

#     for i in range(360):
#         k = math.radians(i)
#         x = hearta(k) + 200  # Adjust the x-coordinate to move to the right
#         y = heartb(k)
#         turtle.goto(x, y)

#     turtle.end_fill()

# # Create a turtle
# turt = turtle.Turtle()
# turt.speed(4)

# # Draw the heart on the right side
# draw_heart()

# # Keep the window open
# turtle.done()
# turtle.exitonclick()
# # try:
#   s=int(input("Enter the value "))
# except NameError:
#   print("Variable x is not defined")
# except:
#   print("Something else went wrong")

# import turtle
# import time

# def draw_heartbeat(scale_factor):
#     turtle.clear()
#     turtle.penup()
#     turtle.goto(0, 0)
#     turtle.pendown()

#     turtle.color("red")
#     turtle.width(3)

#     turtle.forward(50 * scale_factor)
#     turtle.backward(100 * scale_factor)
#     turtle.forward(50 * scale_factor)

#     turtle.hideturtle()
#     turtle.update()
#     time.sleep(0.5)  # Adjust the delay time for the heartbeat effect

# # Create a turtle
# turt = turtle.Turtle()
# turt.speed(1)

# # Heartbeat animation
# for scale in [1, 1.5, 1]:
#     draw_heartbeat(scale)

# # Keep the window open
# turtle.done()