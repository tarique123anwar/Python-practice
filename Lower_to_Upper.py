# def swap_case(s):
#     new_s=':-'
#     for i in s:
#         if i.isupper():
#             new_s+=i.lower()
#         else:
#             new_s+=i.upper()
#     return new_s

# if __name__ == '__main__':
#     s = input("Enter the Input")
#     result = swap_case(s)
#     print(result)

#  #different method
# def swap_case(s):

#     string = ""
#     for i in s:
#         if i.isupper() == True:
#             string+=(i.lower())
#         else:
#             string+=(i.upper())
#     return string
# if __name__ == '__main__':

#     s = input()

#     result = swap_case(s)

#     print(result)
 
# def swap(s):
#     ns=""
#     for a in s:
#         if a.isupper():
#             ns+=a.lower()
#         else:
#             ns+=a.upper()
#     return ns
# if __name__ == '__main__':
#     s = input("Enter the Input")
#     result = swap(s)
#     print(result)


def l(s):
    d=""
    for f in s:
        if f.isupper():
            d+=f.lower()
        else:
            d+=f.upper()
    return d
if __name__ == '__main__':
    s = input("Enter the Input")
    result = l(s)
    print(result)



    
    