import random
l=['ߏ','ߎ']
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
If are you under 26 , press 1
If are you under 25 , press 2
''' ))

            if ui==1:
                uc=ord('ߎ')
            elif ui==2:
                uc= ord('ߏ')
            cc=random.choice(l)
            print(uc)
            print(cc)
            #first draw case 
            if cc==uc:
                print("Computer Value",ord(cc))
                print("User Value",uc)
                print("We are guessing eql")
                print("\n")
                print("Pl try agian... ")
                # computercount=computercount+1
            elif uc > ord(cc):
                r=ord('ߨ')
                k=r-uc
                print("Computer Value",ord(cc))
                print("User Value",uc)
                print("Uh win","Yr age:-",k)
                # computercount=computercount+1
                print("\n")
                print("R u not sure, then play again..")
            else:
                t=ord('ߨ')
                q=t-uc
                print("Computer Value",ord(cc))
                print("User Value",uc)
                print("Computer Win",q)
                # computercount=computercount+1
                print("\n")
                print("R u not sure, then play again..")

    else:
        break
