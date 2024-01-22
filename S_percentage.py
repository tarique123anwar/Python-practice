if __name__ == '__main__':
    n = int(input("Enter the value"))
    
    s = {}

    for _ in range(n):

        name, *line = input().split()

        sc= list(map(float, line))

        s[name] = sc

    query_name = input()

    l1 = list(s[query_name]) 

    addition = sum(l1)

    result = addition/len(l1)

    print('%.2f'% result)
