a=int(input("Enter the dob "))
if (a ==ord("") or a ==ord("") or a ==ord('ߎ')):#or a==ord("ߏ") or a==ord("ߍ")):
    # x = ord("ߨ")                                    #or a ==ord("ߏ") or a ==ord("ߏ")):
    # s = ord("ߎ")
    # f=x-s
    # print("ߨ")
    # i = ord("ߏ")
    # s = ord("ߎ")
    # q=i-s
    # o = ord("ߍ")
    # s = ord("ߎ")
    # v=o-s
    t=[72,65,80,80,89,95,66,73,82,84,72,95,68,65,89]
    for r in t:
        print(chr(r), end=' ')
    print('\n')
    print("Congratulations your age is ",f)
    print('\n')
    import datetime
    d=datetime.datetime.now() 
    m=d.strftime("%b")            #%b,%B,%m,%y,%Y,%H,%I,%p,%M
    print(m,'-',d)
    print('\n')
else:
    print("Pl enter the correct DOB") 
    