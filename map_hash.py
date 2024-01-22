if __name__ == '__main__':
    n = int(input("Enter the Integer Values"))
    i= tuple(map(int, input().split()))
    print(hash(i))
