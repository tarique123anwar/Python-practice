    #n=random.randint(2,8) ye all values ko print karega (ye sab randomlly value ko print karta hai )
import random 
n=random.randint(2,8)
print(n)
    #n1=random.randrange(3,9) ye range ke hisaab se work karega (3,8) tak
n1=random.randrange(3,9)
print(n1) 
    #k=random.choice ye koi bhi value randomlly print kar sakta hai 
l=[10,20,30,40,50]
k=random.choice(l)
print(k)

    #practice 

import random
e=random.randint(4,8)
print(e)

f=random.randrange(2,10)
print(f)

j=[20,78,89,76,90]
f=random.choice(j)
print(f)

    #random, 0 aur 1 ke beech ki koi bhi float value chahiye to ise use karte hain (isme koi parameter dene ki zaroorat nahi hai by defualt leta hai )
r=random.random()
print(r)

    #random. shuffle ye koi bhi elements  ya value ko ksi number pe bhi khisak ke aa sakta hai 
l=[50,89,70,60]
random. shuffle(l)
print(l)

    #uniform , ye float value return karta hai like 8.0 ,5.34
u=random.uniform(3,9)
print(u)