import random
l=[1999,1998]
while True:
    computercount=0
    usercount=0
    i=int(input('''
Game Start ......
1 Yes 
2 No | Exit
'''))
    if i==1:
        for a in range(1,2):
            ui=int(input('''
1 a 1999
2 b 1998
''' ))
            if ui==1:
                uc=1999
            elif ui==2:
                uc=1998
            # elif ui==3:
            #     uc=1997
            cc=random.choice(l)
            print(uc)
            print(cc)
            #first draw case 
            if uc>=cc:
                r=2024
                k=r-uc
                print("Computer Value",cc)
                print("User Value",uc)
                print("Uh win","Yr age:-",k)
                print("\n")
                print("R u not sure then play again ")
                # print("R u not sure then play again ")
                computercount=computercount+1
                usercount=usercount+1
                # print("\n")
            #second draw case User ko win karne ka logic (or mean koi yek bhi condition match kiya to value print hoga )

            # elif (uc==1999 and cc==1998) or (uc==1998 and cc==1997) or (uc==1999 and cc==1997):
                #  print("Computer Value",cc)
                #  print("User Value",uc)
                #  print("You Win ")
                #  usercount=usercount+1

             #third case computer winnn ,(computercount=computercount+1) iska matlab ke jo jeeta use yek poit milega (c=c+1)
            else:
                t=2024
                q=t-cc
                print("Computer Value",cc)
                print("User Value",uc)
                print("Computer Win",q)
                computercount=computercount+1

        #          #final game round  
        # if cc==uc:
        #     print("Final game draw ...")
        #     print("User score",usercount)
        #     print("Computer score ",computercount)
        # elif uc>cc:
        #     print("Final Uh win the game ...")
        #     print("User score",usercount)
        #     print("Computer score ",computercount)
        # else:
        #     print("Final computer win the game...")
        #     print("User score",usercount)
        #     print("Computer score ",computercount)

    else:
        break