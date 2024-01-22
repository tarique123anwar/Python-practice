# insert()
# append()
# extends()

# insert() ye kahin bhi add kar sakte hain 
l=[55,66,77,88]
l.insert(1,100)
print(l)
# append() ye last me add hota hai 
l=[55,66,77,88]
t=[98,76]
l.append(t)
print(l)
# extends() andar ki value me add hota hai nested list nhi bnata 
l=[55,66,77,88]
n=[22,30]
l.extend(n)
print(l)