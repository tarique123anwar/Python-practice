l=[]
while True:
    c=int(input('''
            1 push
            2 pop
            3 front
            4 last
            5 dis Q
            6 exit
            '''))
    if c==1:
        n=input("Enter the Value:- ");
        l.append(n)
        print(l)
    elif c==2:
        if len(l)==0:
            print("Empty Q")
        else:
            del l[0]
            print(l)
    elif c==3:
        if len(l)==0:
            print("Empty Q")
        else:
            print("First Q Value",l[0])
    elif c==4:
        if len(l)==0:
            print("Empty Q")
        else:
            print("Last  Q Value",l[-1])
    elif c==5:
            print("Dis Q",l)
    elif c==6:
        break
    else:
        print("Invalid Opr....")