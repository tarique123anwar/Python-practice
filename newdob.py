# import random

# options = ['ߏ', 'ߎ']

# while True:
#     user_count = 0
#     computer_count = 0

#     user_choice = int(input('''
# Game Start ......
# 1 Yes 
# 2 No | Exit
# '''))

#     if user_choice == 1:
#         for a in range(1,2):
#             user_age_choice =int(input('''
# If are you under 26 , press 1
# If are you under 25 , press 2
# ''' ))

#         if user_age_choice == 1:
#             user_char = 'ߎ'
#         elif user_age_choice == 2:
#             user_char = 'ߏ'

#         computer_char = random.choice(options)
#         print("User Value:", ord(user_char))
#         print("Computer Value:", ord(computer_char))

#         if computer_char == user_char:
#             print("We are guessing equal. Please try again.")
#         elif ord(user_char) > ord(computer_char):
#             age_difference = ord('ߨ') - ord(user_char)
#             print("You win! Your age:", age_difference)
#             # user_count = user_count+1
#         else:
#             age_difference = ord('ߨ') - ord(computer_char)
#             print("Computer wins! Age difference:", age_difference)
#             # computer_count = computer_count+1

#     else:
#         break

# import random
# l=['ߏ','ߎ']
# while True:
#     computercount=0
#     usercount=0
#     i=int(input('''
# Game Start ......
# 1 Yes 
# 2 No | Exit
# '''))
#     if i==1:
#         for a in range(1,4):
#             ui=int(input('''
# If are you under 26 , press 1
# If are you under 25 , press 2
# ''' ))

#             if ui==1:
#                 uc=ord('ߎ')
#             elif ui==2:
#                 uc= ord('ߏ')
#             cc=random.choice(l)
#             print(uc)
#             print(cc)
#             #first draw case 
#             if cc==uc:
#                 print("Computer Value",ord(cc))
#                 print("User Value",uc)
#                 print("We are guessing eql")
#                 print("\n")
#                 print("Pl try agian... ")
#                 computercount=computercount+1
#                 computercount=computercount+1
#             elif ord(uc> cc):
#                 r=ord('ߨ')
#                 k=r-uc
#                 print("Computer Value",ord(cc))
#                 print("User Value",uc)
#                 print("Uh win","Yr age:-",k)
#                 computercount=computercount+1
#                 print("\n")
#                 print("R u not sure, then play again..")
#             else:
#                 t=ord('ߨ')
#                 q=t-uc
#                 print("Computer Value",ord(cc))
#                 print("User Value",uc)
#                 print("Computer Win",q)
#                 computercount=computercount+1
#                 print("\n")
#                 print("R u not sure, then play again..")

#     else:
#         break

# import random
# l= ['ߎ','ߏ', 'ߐ']
# while True:
#     computercount=0
#     usercount=0
#     i=int(input('''
# Game Start ......
# 1 Yes 
# 2 No | Exit
# '''))
#     if i==1:
#         for a in range(1,2):
#             ui=int(input('''
# 1 a ߏ
# 2 b ߎ
# 3 c ߐ
# ''' ))
#             if ui==1:
#                  uc=ord('ߏ')
#             elif ui==2:
#                 uc=ord('ߎ')
#             elif ui==3:
#                  uc=ord('ߐ')
#             cc=random.choice(l)
#             print(uc)
#             print(cc)
#             #first draw case 
#             if cc==uc:
#                 print("Computer Value",ord(cc))
#                 print("User Value",ord(uc))
#                 print("G Draw")
#                 computercount=computercount+1
#                 usercount=usercount+1

#             #second draw case User ko win karne ka logic (or mean koi yek bhi condition match kiya to value print hoga )

#             elif (uc==ord('ߏ')and cc=='ߎ') or (uc==ord('ߎ') and cc==ord('ߐ')) or (uc==ord('ߐ') and cc=='ߏ'):
#                  print("Computer Value",ord(cc))
#                  print("User Value",uc)
#                  print("You Win ")
#                  usercount=usercount+1

#              #third case computer winnn ,(computercount=computercount+1) iska matlab ke jo jeeta use yek poit milega (c=c+1)
#             else:
#                  print("Computer Value",ord(cc))
#                  print("User Value",uc)
#                  print("Computer Win ")
#                  computercount=computercount+1

#                  #final game round 
#         if cc==uc:
#             print("Final game draw ...")
#             # print("User score",uc)
#             # print("Computer score ",ord(cc))
#         elif uc>ord(cc):
#             print("Final Uh win the game ...")
#             # print("User score",uc)
#             # print("Computer score ",ord(cc))
#         else:
#             print("Final computer win the game...")
#             # print("User score",uc)
#             # print("Computer score ",ord(cc))

#     else:
#         break
# from turtle import *
# import turtle as tur
import random
from turtle import *
import math 
from turtle import*
import turtle
import random
    
import turtle as tur

characters = ['ߎ', 'ߏ', 'ߐ']

while True:
    computer_count = 0
    user_count = 0

    play_game = int(input('''
                                Do you want to know your DOB ......
                                           Enter the password for unlock the GIFT
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
        # elif (user_choice >=1) or (user_choice >=2) or (user_choice >=3):
        #     print("Please enter (1-3) numbers ")

            print("Your Gussing ...", user_char)
            print("My Gussing...", computer_char)

            if user_char == computer_char:
                print("We are gussing equal" )
                computer_count += 1
                user_count += 1
                print("\n")
                print("If you are not sure ,then play agian ")
                # e=str(input("Sure ,Press (Y)"))
                # print(e)
            elif (user_char == ord('ߏ') and computer_char == ord('ߎ')) or \
                    (user_char == ord('ߎ') and computer_char == ord('ߐ')) or \
                    (user_char == ord('ߐ') and computer_char == ord('ߏ')):
                d=ord('ߨ')
                t=d-user_char
                print("You are right ","\nI thing Your age:-",t)
                print(ord(''),chr(47),ord(''),chr(47),user_char)
                user_count += 1
                print("\n")
                print("If you are not sure ,then play agian") 
                # e=str(input("Sure ,Press (Y)"))
                # print(e)
            else:
                d=ord('ߨ')
                w=d-computer_char
                computer_count += 1
                print("I am right","\nI thing Your age:-",w)
                print(ord(''),chr(47),ord(''),chr(47),computer_char)
                print("\n")
                print("If you are not sure ,then play agian")
                    # e=str(input("Sure ,Press (Y)"))
                    # print(e)
                    # print("Please enter the correct password.")
                    # e=str(input("Sure ,Press (Y)"))
                    # print(e)
                    # Python3 code to calculate age in years
        
        else: 
            print("Index out of range")
    else:
        print("please enter correct password")

    # import turtle
    # import random

    # sets background

# from turtle import *

# # Create a turtle object
# t = Turtle()

# # Set the position for left-justified text
# # t.penup()
# # t.goto(-200, 0)
# # t.pendown()

# # # Write left-justified text
# # t.write("Left-justified", align="left", font=("Arial", 12, "normal"))

# # # Set the position for right-justified text
# # t.penup()
# # t.goto(200, 0)
# # t.pendown()

# # # Write right-justified text
# # t.write("Right-justified", align="right", font=("Arial", 12, "normal"))

# # # Keep the window open
# # done()



        # from datetime import date

        # def calculateAge(birthDate):
        #     today = date.today()
        #     age = today.year - birthDate.year - ((today.month, today.day) <
        #         (birthDate.month, birthDate.day))

        #     return age
            
        # # Driver code 
        # print(calculateAge(date(1997, 2, 3)), "years")


            # print("\nEnd of Rounds. Scores:")     need=['',95,'']
            # print("User: ", user_count)
            # print("Computer: ", computer_count)

            # Final game round logic
            # if user_count > computer_count:
            #     print("Final You win the game...")
            # elif user_count < computer_count:
            #     print("Final Computer win the game...")
            # else:
            #     print("Final game draw...")
                        
                # break
                        # t=str(input("Sure ,Press (Y)"))
                        # if t=='Y':
                        # def hearta(k):
                            
                        #         return 15*math.sin(k)**3
                        # def heartb(k):
                                
                        #         return 12*math.cos(k)-5*\
                        #             math.cos(2*k)-2*\
                        #             math.cos(3*k)-\
                        #             math.cos(4*k)
                        # speed(4)
                        # bgcolor("black")
                        # for i in range(30+1+26):
                        #     goto(hearta(i)*5,heartb(i)*5)
                        #     for j in range(5):
                        #         (color("#f73487"))
                        #     goto(0,0)
                        # done()
                        # e=str(input("Sure ,Press (Y)"))
                        # print(e)
