# import random
# l=["a","b","c"]
# while True:
#     uc=int(input('''
# Game start.-.-.-.-.
# 1 Yes
# 2 No | Exit
# '''))
#     if uc==1:
#         for a in range(1,6):
#             ui=int(input('''
# 1 a
# 2 b
# 3 c
# '''))
#             if ui==1:
#                 uc="a"
#             elif ui==2:
#                 uc="b"
#             elif ui==3:
#                 uc="c"
#             cc=random.choice(l)
#             print(uc)
#             print(cc)

#/////////////

import random
l=["a","b","c"]
while True:
    computercount=0
    usercount=0
    i=int(input('''
Game Start ......
1 Yes 
2 No | Exit
'''))
    if i==1:
        for a in range(1,6):
            ui=int(input('''
1 a
2 b 
3 c
''' ))
            if ui==1:
                uc="a"
            elif ui==2:
                uc="b"
            elif ui==3:
                uc="c"
            cc=random.choice(l)
            print(uc)
            print(cc)
            #first draw case 
            if cc==uc:
                print("Computer Value",cc)
                print("User Value",uc)
                print("G Draw")
                computercount=computercount+1
                usercount=usercount+1

            #second draw case User ko win karne ka logic (or mean koi yek bhi condition match kiya to value print hoga )

            elif (uc=="a" and cc=="b") or (uc=="c" and cc=="a") or (uc=="b" and cc=="c"):
                 print("Computer Value",cc)
                 print("User Value",uc)
                 print("You Win ")
                 usercount=usercount+1

             #third case computer winnn ,(computercount=computercount+1) iska matlab ke jo jeeta use yek poit milega (c=c+1)
            else:
                 print("Computer Value",cc)
                 print("User Value",uc)
                 print("Computer Win ")
                 computercount=computercount+1

                 #final game round 
        if cc==uc:
            print("Final game draw ...")
            print("User score",usercount)
            print("Computer score ",computercount)
        elif uc>cc:
            print("Final Uh win the game ...")
            print("User score",usercount)
            print("Computer score ",computercount)
        else:
            print("Final computer win the game...")
            print("User score",usercount)
            print("Computer score ",computercount)

    else:
        break

#//////////////#
    
# import random 
# l=["r","s","p"]
# while True:
#     comc=0
#     userc=0
#     i=int(input('''
# GAME START...
# 1 Yes
# 2 No
# '''))
#     if i==1:
#         for a in range(1,6):
#             ui=int(input('''
# 1 r
# 2 s
# 3 p
# '''))
#             if ui==1:
#                 uc="r"
#             elif ui==2:
#                 uc="s"
#             elif ui==3:
#                 uc="p"
#                 cc=random.choice(l)
#                 print(uc)
#                 print(cc)
#             #second part
#                 if cc==uc:
#                         print("Game Draw.-.-..")
#                         print("Com..value",cc)
#                         print("Ur value",uc)
#                         comc=comc+1
#                         userc=userc+1            #(uc=="a" and cc=="b") or (uc=="c" and cc=="r") or (uc=="b" and cc=="b"):
#                 elif (uc=="r" and cc=="s") or (uc=="p" and cc=="r") or (uc=="s" and cc=="p"):  #(uc=="r" and cc=="s") or (uc=="p" and cc=="r") or (uc=="s" and cc=="p"):
#                         print("Com..value",cc)
#                         print("Ur value",uc) 
#                         print("Uh Win.-.-..")
#                         userc=userc+1
#                 else:
#                         print("Com value",cc)
#                         print("Ur value",uc)
#                         print("Com Win.-.-..")
#                         comc=comc+1
#                 if cc==uc:
#                         print("Final game draw.-.-..")
#                         print("Ur score",userc)
#                         print("Com score",comc)
#                 elif uc>cc:
#                         print("Uh win the final game .-.-..")
#                         print("Ur score",userc)
#                         print("Com score",comc)
#                 else:
#                         print("Com win the final game .-.-..")
#                         print("Ur score",userc)
#                         print("Com score",comc)
#     else:
#         break
# import random
# l=["water","fire","alarm"]
# while True:
#     uu=0
#     cc=0
#     i=int(input('''
#           START......
# 1 Press the start Game 
# 2 press the exit 
# '''))
#     if i==1:
#      for a in range(1,6):
#          userinput=int(input('''
# 1 water
# 2 fire
# 3 alarm
# '''))
#          if userinput==1:
#              us="water"
#          elif userinput==2:
#              us="fire"
#          elif userinput==3:
#              us="fire"
#              ucc=random.choice(l)
#              print("us")
#              print("ucc")

#              if us==ucc:
#                  print("game draw",us)
#                  print("user value",us)
#                  print("com value",us)
#                  uu=uu+1
#                  cc=cc+1
#              elif (us=="water" and ucc=="fire") or (us=="alarm" and ucc=="fire") or (us=="fire" and ucc=="alarm"):
#                  print("user win")
#                  print("user value",us)
#                  print("com value",ucc)
#                  uu=uu+1

#              else:
#                  print("com win")
#                  print("user value",us)
#                  print("com value",ucc)
#                  cc=cc+1
#                  #final game
#              if ucc==us:
#                  print("Final game draw win")
#                  print("user score",uu)
#                  print("com score",cc)
#              elif us>ucc:
#                  print("Final game uh win")
#                  print("user score",uu)
#                  print("com score",cc)
#              else:
#                   print("Final game com win")
#                   print("user score",uu)
#                   print("com score",cc)
#     else:
#         break   