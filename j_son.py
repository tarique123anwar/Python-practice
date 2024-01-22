    #json(javascript object notation) iksa use ham (API ke liye karte hain data ko access kartne ke liye (dumps) and (loads) fun ke zariye 
# import json
# d={
#     'name':'Anwar', 'id':10
#  }
# f= json.dumps(d)
# print(type(f))
# print(f)

    #/////////////

# import json 
# k={"naam":"abc","realnaam":"xyz"}
# d=json.dumps(k)
# print(type(k))
# print(k)

    #////////////

# import json
# u={"d":"f","ww":"q"}
# r=json.dumps(u)
# print(r) 

    #/////////// using loads fun ,loads()

# import json
# d='{"sname:":"anwar","rollno:":321}'
# x=json.loads(d)
# print(x)
# print(type(x))
# for a in x:
#     print(a,x[a])

#   #////////
# import json
# d='[{"sname:":"anwar","rollno:":321}]'
# x=json.loads(d)
# print(x)
# print(type(x))
# for a in x:
#     print(a,x[a])

# import json 
# f={'n':'a','t':3}
# g=json.dumps(f)
# print(type(f))
# print(g)
# for a in g:
#     print(a,g[a])


# import json
# r={
#     'name':'tarique' , 
#     'roll': 33
# }
# t=json.dumps(r)
# print(t)
# print(type(r))

import json
y='{"Name:-":"Jameel","Roll:-":55, "Branch:-":"Cse"}'
f=json.loads(y)
print(f)
print(type(y))
for a in f:
    print(a,f[a])
    #/////////
    #iska use ham json file ko access karne ke liye karte hain (r) data read karna 
import json
file=open("post.json","r") #this is json type file 
x=file.read()
fdata=json.loads(x)
for a in fdata:
    print(a['name'],a['roll'])


    #////////
import json
file=open("filename","r")
f=file.read()
fdata=json.loads(f)
for a in fdata:
    print(a['name'],a['roll'])