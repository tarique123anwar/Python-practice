import json 
file =open ("posts.json","r")
x=file.read()
filandata=json.loads(x)
for a in filandata:
    print(a['title'],a['userad'])
