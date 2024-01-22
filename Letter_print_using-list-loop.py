    # your code goes here
a="Anwar"
def print_rangoli(s):
    l=[]
    for r in range(s):
        K="-".join(a[r:s])
        l.append(K[::-1]+K[1:])
    w = len(l[0])
    for r in range(s-1, 0, -1):
        print(l[r].center(w, '-'))
    for r in range(s):
        print(l[r].center(w,'-'))
if __name__ == '__main__':
    n = int(input("Enter the Lenth Values"))
    print_rangoli(n) 