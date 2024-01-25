
per=int(input("Enter the Mark"))
if per>=60:
           print("First")
elif per>=45:
           print("Second")
elif per>=35:
           print("Third")
else:
           print("Fail") 

           for _ in range(int(input())):
            print(re.search(r'^([-\+])?\d*\.\d+$', input()) is not None)