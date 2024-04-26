# n, m = map(int,input().split())
# for i in range(n//2):
#     j = int((2*i)+1)
#     print(('.|.'*j).center(m, '-'))
# print('WELCOME'.center(m, '-'))
# for i in reversed(range(n//2)):
#     j = int((2*i)+1)
#     print(('.|.'*j).center(m, '-'))

def get_employee_salary():
    validInput = False
    while not validInput:
        salary = input("Enter Employee Salary: ")
        if salary.isdigit():
            validInput = True
        else:
            print("Error: Please enter a valid value.")
    return salary
print(get_employee_salary())