# s={10,20,30}
# for a in s:
#     print(a)  

    #set()Fun List ko set me convert karne ke liye 
l=[10,20,30]
s=set(l)
print(s)    
    #add() sets me new Value add karne ke liye 
s={20,40, 68}
s.add(70)
print(s)
    #pop() rondamly value ko delete karta hai 
s={20,40, 68}
print(s.pop())
print(s)
    #remove() ise bhi value ko remove karne ke liye use karte hain 
s={20,40, 68}
s.remove(68)
print(s)
    #discard()ise bhi value ko remove karne ke liye use karte hain 
s={20,40, 68}
s.discard(68)
print(s)
    #clear() ye all data ko clear karta hai aur set() retunt karta hai 
s={20,40, 68}
s.clear()
print(s)
    #update() ki help se data ko SIRF insert kar sakte hain naki delete and change.
s={20,40, 68}
l=[50,66,788]
s.update(l)
print(s)