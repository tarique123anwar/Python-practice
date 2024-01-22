l=[]
while True:
    c=int(input('''
            1 push
            2 pop
            3 peek
            4 dis
            5 exit
            '''))
    if c==1:
        n=input("Enter the Value:- ");
        l.append(n)
        print(l)
    elif c==2:
        if len(l)==0:
            print("Empty Stack")
        else:
            p=l.pop()
            print(p)
            print(l)
    elif c==3:
        if len(l)==0:
            print("Empty Stack")
        else:
            print("Last Stack Value",l[-1])
    elif c==4:
        print("Dis Stack",l)
    elif c==5:
        break;
    else:
        print("Invalid Opr....")