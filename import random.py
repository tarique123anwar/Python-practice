import random
l=["r","s","p"]
while True:
    ccount=0
    ucount=0
    uc=int(input('''
Game Start.....
1 Yes  
2 No | Exit
        '''))
    if uc==1:
            for a in range(1,6):
                ui=int(input('''
1 R
2 S
3 P
'''))
    if ui==1:
            uc="r"
    elif ui==2:
            uc="s"
    elif ui==3:
            uc="p"
    cc=random.choice(1)
    if cc==uc:
            print("Computer Value",cc)
            print("User Value",uc)
            print("Game Draw")
            ucount=ucount+1
            ccount=ccount+1
    elif(uc=="r" and cc=="s") or (uc=="p"and cc=="r") or (cc=="s" and cc=="p"):
            print("Computer Value",cc)
            print("User Value",uc)
            print("You win")
            ucount=ucount+1
    else:
            print("Computer Value",cc)
            print("User Value",uc)
            print("Computer win")
            ccount=ccount+1
    if ucount==ucount:
            print("Final Game Draw...")
            print("User Value",uc)
            print("Computer Score",cc)
    elif ucount==ccount:
            print("Final You win the Game...")
            print("User Score ",uc)
            print("Computer Score",cc)
    else:
            print("Final Computer win the Game...")
            print("User Score ",uc)
            print("Computer Score",cc)
    break