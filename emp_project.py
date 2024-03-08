# class Employee:
#     def __init__(self, emp_id, name, position):
#         self.emp_id = emp_id
#         self.name = name
#         self.position = position

# class EmployeeManagementSystem:
#     def __init__(self):
#         self.employees = []

#     def add_employee(self, emp_id, name, position):
#         employee = Employee(emp_id, name, position)
#         self.employees.append(employee)
#         print(f"Employee {name} added successfully.")

#     def display_employees(self):
#         if not self.employees:
#             print("No employees in the system.")
#         else:
#             print("Employee List:")
#             for employee in self.employees:
#                 print(f"ID: {employee.emp_id}, Name: {employee.name}, Position: {employee.position}")

# def main():
#     emp_management = EmployeeManagementSystem()

#     while True:
#         print("\nEmployee Management System")
#         print("1. Add Employee")
#         print("2. Display Employees")
#         print("3. Exit")

#         choice = input("Enter your choice (1/2/3): ")

#         if choice == "1":
#             emp_id = int(input("Enter Employee ID: "))
#             name = input("Enter Employee Name: ")
#             position = input("Enter Employee Position: ")
#             emp_management.add_employee(emp_id, name, position)

#         elif choice == "2":
#             emp_management.display_employees()

#         elif choice == "3":
#             print("Exiting the Employee Management System. Goodbye!")
#             break

#         else:
#             print("Invalid choice. Please enter a valid option.")

# if __name__ == "__main__":
#     main()

    #////////////////////////
# employees = []

# def add_employee(emp_id, name, position):
#     employee = {"ID": emp_id, "Name": name, "Position": position}
#     employees.append(employee)
#     print(f"Employee {name} added successfully.")

# def display_employees():
#     if not employees:
#         print("No employees in the system.")
#     else:
#         print("\nEmployee List:")
#         for employee in employees:
#             print(f"ID: {employee['ID']}, Name: {employee['Name']}, Position: {employee['Position']}")

# def main():
#     while True:
#         print("\nEmployee Management System")
#         print("1. Add Employee")
#         print("2. Display Employees")
#         print("3. Exit")

#         choice = input("Enter your choice (1/2/3): ")

#         if choice == "1":
#             emp_id = int(input("Enter Employee ID: "))
#             name = input("Enter Employee Name: ")
#             position = input("Enter Employee Position: ")
#             add_employee(emp_id, name, position)

#         elif choice == "2":
#             display_employees()

#         elif choice == "3":
#             print("Exiting the Employee Management System. Goodbye!")   
#             break

#         else:
#             print("Invalid choice. Please enter a valid option.")

# if __name__ == "__main__":
#     main()


        #////////////////
# from flask import Flask, jsonify, request

# app = Flask(__name__)

# # Sample data (replace with your data source)
# employees = [
#     {"id": 1, "name": "John", "position": "Developer"},
#     {"id": 2, "name": "Jane", "position": "Designer"}
# ]

# # API endpoint to get all employees
# @app.route('/api/employees', methods=['GET'])
# def get_employees():
#     return jsonify(employees)

# # API endpoint to get a specific employee by ID
# @app.route('/api/employees/<int:emp_id>', methods=['GET'])
# def get_employee(emp_id):
#     employee = next((e for e in employees if e['id'] == emp_id), None)
#     if employee:
#         return jsonify(employee)
#     else:
#         return jsonify({"error": "Employee not found"}), 404

# # API endpoint to add a new employee
# @app.route('/api/employees', methods=['POST'])
# def add_employee():
#     new_employee = request.json
#     employees.append(new_employee)
#     return jsonify({"message": "Employee added successfully"}), 201

# if __name__ == '__main__':
#     app.run(debug=True)


# import random

# def guess_the_number():
#     print("Welcome to the Guess the Number Game!")
    
#     # Generate a random number between 1 and 20
#     secret_number = random.randint(1, 20)
    
#     attempts = 0
#     max_attempts = 5
    
#     while attempts < max_attempts:
#         try:
#             # Get the player's guess
#             guess = int(input("Enter your guess (between 1 and 20): "))
            
#             # Check the guess
#             if guess == secret_number:
#                 print("Congratulations! You guessed the correct number.")
#                 break
#             elif guess < secret_number:
#                 print("Too low! Try again.")
#             else:
#                 print("Too high! Try again.")
            
#             attempts += 1

#         except ValueError:
#             print("Invalid input. Please enter a valid number.")
    
#     if attempts == max_attempts:
#         print(f"Sorry, you've run out of attempts. The correct number was {secret_number}.")

# if __name__ == "__main__":
#     guess_the_number()


# #///////////////////////
    
# a=int(input("Enter the any number.1_99"))
# print(a)
# b=int(input("add 3"))
# print(b)
# c=int(input("multiple the 2"))
# print(c)
# d=int(input("divide the 2"))
# print(d)
# e=int(input("and minus firts gaven number"))
# print(e)


    #////////////////////
# Mind Reading Game

# Get the initial number from the user
# a = int(input("Enter any number between 1 and 99: "))
# print("You entered:", a)

# # Perform operations based on user input
# b = int(input("Add 3 to the number: "))
# print("After adding 3:", a + b)

# c = int(input("Multiply the result by 2: "))
# print("After multiplying by 2:", (a + b) * c)

# d = int(input("Divide the result by 2: "))
# print("After dividing by 2:", ((a + b) * c) / d)

# e = int(input("Subtract the original number: "))
# result = ((a + b) * c) / d - e
# print("Your given number is....:", result)


#//////////////////////

# first = int(input("Enter any number between 1 and 99: "))
# print("You entered:", first)

# # Perform operations based on user input
# second= int(input("Add 3 to the number: "))
# print("After adding 3:", first + second)


# third  = int(input("Multiply the result by 2: "))
# print("After multiplying by 2:", (first + second) * third)

# fourth = int(input("Divide the result by 2: "))
# print("After dividing by 2:", ((first + second) * third) / fourth)

# fifth = int(input("Subtract the original number: "))
# result =  ((first + second) * third) / fourth- fifth
# print("Your given number is....:", result)


#/////////////////////////

# '''
# Mad Libs Generator
# -------------------------------------------------------------
# '''

# # Questions for the user to answer

# noun = input('Choose a noun: ')

# p_noun = input('Choose a plural noun: ')

# noun2 = input('Choose a noun: ')

# place = input('Name a place: ')

# adjective = input('Choose an adjective (Describing word): ')

# noun3 = input('Choose a noun: ')

# # Print a story from the user input

# print('------------------------------------------')

# print('Be kind to your', noun, '- footed', p_noun)

# print('For a duck may be somebody\'s', noun2, ',')

# print('Be kind to your', p_noun, 'in', place)

# print('Where the weather is always', adjective, '. \n')

# print('You may think that is this the', noun3, ',')

# print('Well it is.')

# print('------------------------------------------')

#//////////////////////////////////
# import random

# class Bank:
#     def __init__(self):
#         self.accounts = {}

#     def create_account(self, name, balance):
#         account_number = random.randint(1000, 9999)
#         pin = random.randint(999, 9999)
#         account = Account(name, account_number, pin, balance)
#         self.accounts[account_number] = account
#         print(f"Account created successfully. Account Number: {account_number}")

#     def login(self, account_number, pin):
#         if account_number in self.accounts and self.accounts[account_number].pin == pin:
#             return self.accounts[account_number]
#         else:
#             return None

# class Account:
#     def __init__(self, name, account_number, pin, balance):
#         self.name = name
#         self.account_number = account_number
#         self.pin = pin
#         self.balance = balance

#     def display_balance(self):
#         print(f"Account Balance: Rs {self.balance}")

#     def deposit(self, amount):
#         self.balance += amount
#         print(f"Rs {amount} deposited successfully.")
#         self.display_balance()

#     def withdraw(self, amount):
#         if amount <= self.balance:
#             self.balance -= amount
#             print(f"Rs {amount} withdrawn successfully.")
#         else:
#             print("Insufficient funds.")
#         self.display_balance()

# def main():
#     bank = Bank()

#     while True:
#         print("\nCreate a Bank A/C for Servicepack.ai")
#         print("1. Create Account")
#         print("2. Login")
#         print("3. Quit")

#         choice = input("Enter your choice (1/2/3): ")

#         if choice == "1":
#             name = input("Enter your name: ")
#             initial_balance = float(input("Enter initial balance: "))
#             bank.create_account(name, initial_balance)

#         elif choice == "2":
#             account_number = int(input("Enter your account number: "))
#             pin = int(input("Enter your PIN: "))
#             user_account = bank.login(account_number, pin)

#             if user_account:
#                 while True:
#                     print("\nAccount Menu")
#                     print("1. Display Balance")
#                     print("2. Deposit")
#                     print("3. Withdraw")
#                     print("4. Logout")

#                     option = input("Enter your option (1/2/3/4): ")

#                     if option == "1":
#                         user_account.display_balance()
#                     elif option == "2":
#                         amount = float(input("Enter the deposit amount: "))
#                         user_account.deposit(amount)
#                     elif option == "3":
#                         amount = float(input("Enter the withdrawal amount: "))
#                         user_account.withdraw(amount)
#                     elif option == "4":
#                         print("Logout successful.")
#                         break
#                     else:
#                         print("Invalid option. Please enter a valid choice.")

#             else:
#                 print("Invalid account number or PIN. Please try again.")

#         elif choice == "3":
#             print("Exiting the Bank Management System. Goodbye!")
#             break

#         else:
#             print("Invalid choice. Please enter a valid option.")

# if __name__ == "__main__":
#     main()


        ##/////////////
# import uuid

# class Employee:
#     def __init__(self, emp_id, name, position, salary):
#         self.emp_id = emp_id
#         self.name = name
#         self.position = position
#         self.salary = salary

# class EmployeeManagementSystem:
#     def __init__(self):
#         self.employees = []

#     def generate_employee_id(self):
#         return str(uuid.uuid4().fields[-1])[:6]  # Extracting the last part of the UUID and taking the first 6 characters

#     def add_employee(self, name, position, salary):
#         emp_id = self.generate_employee_id()
#         employee = Employee(emp_id, name, position, salary)
#         self.employees.append(employee)
#         print(f"Employee {name} added successfully with ID: {emp_id}")

#     def display_employees(self):
#         if not self.employees:
#             print("No employees to display.")
#         else:
#             print("\nEmployee List:")
#             for employee in self.employees:
#                 print(f"Employee ID: {employee.emp_id}, Name: {employee.name}, Position: {employee.position}, Salary: {employee.salary}")

# def main():
#     emp_system = EmployeeManagementSystem()

#     while True:
#         print("\nEmployee Management System")
#         print("1. Add Employee")
#         print("2. Display Employees")
#         print("3. Quit")

#         choice = input("Enter your choice (1/2/3): ")

#         if choice == "1":
#             name = input("Enter Employee Name: ")
#             position = input("Enter Employee Position: ")
#             salary = float(input("Enter Employee Salary: "))
#             emp_system.add_employee(name, position, salary)

#         elif choice == "2":
#             emp_system.display_employees()

#         elif choice == "3":
#             print("Exiting the Employee Management System. Goodbye!")
#             break

#         else:
#             print("Invalid choice. Please enter a valid option.")

# if __name__ == "__main__":
#     main()


# import uuid

# # Generate a random UUID
# random_uuid = uuid.uuid4()
# print(random_uuid)


        #///////////////////

# import uuid
# import sqlite3
# conn=sqlite3.connect("empl.db")
# ins='''
# insert into employee(emp_name,emp_position,emp_salary,join_date) VALUES ('RAM','ss','4222','22')
# '''
# conn.execute(ins)
# conn.commit
# conn.close

        # /////////////////


import uuid
import sqlite3
import uuid
import string
import random
conn = sqlite3.connect("fil.db")
# Get user input
# name = input("Enter Employee Name: ")
# position = input("Enter Employee Position: ")
# salary = input("Enter Employee Salary: ")
# date = input("Enter Join Date: ")

# Insert user input into the employee table
# ins = f'''
#     INSERT INTO employee (emp_name, emp_position, emp_salary, emp_date) VALUES 
#     ('{name}', '{position}', '{salary}', '{date}')
# '''

# conn.execute(inss)
# conn.commit()
# conn.close()
        ##/////////////////
class EmployeeManagementSystem:
    def __init__(self):
        self.employees = []
        # pass_len=6
    def generate_employee_id(self):
                # return str(uuid.uuid4().fields[-1])[:5] 
                #   return string.ascii_letters + string.digits + string.punctuation
                # allowed_chars =string.digits
                allowed_chars = string.digits
                return ''.join(random.choice(allowed_chars) for _ in range(6))
    
    def add_employee(self, name, position, salary ,date,id):
        emp_id = self.generate_employee_id()
        employee = {"emp_id": emp_id, "name": name, "position": position, "salary": salary , "date":date,"id":id}
        self.employees.append(employee)
        print(f"Employee {name} added successfully with your ID :{emp_id}")


    def display_employees(self):
        if not self.employees:
            print("No employees to display.")
        else:
            print("\nEmployee List:")
            for employee in self.employees:

                print(f"Employee ID: {employee['emp_id']}, Name: {employee['name']}, Position: {employee['position']}, Salary: {employee['salary']},date: {employee['date']},")

def main():
    emp_system = EmployeeManagementSystem()

    while True:
        print("\nEmployee Management System")
        print("1. Add Employee")
        print("2. Display Employees")
        print("3. Quit")

        choice = input("Enter your choice (1/2/3): ")

        if choice == "1":
            try:
                name = input("Enter Employee Name: ")
                position = input("Enter Employee Position: ")
                salary = float(input("Enter Employee Salary: "))
                date=int(input("Enter the joining date "))
                emp_system.add_employee(name, position, salary,date)
            except ValueError:
                print("Invalid input. Please enter a valid salary.")
        ins = f'''
            INSERT INTO employee (emp_name, emp_position, emp_salary, emp_date) VALUES 
            ('{name}', '{position}', '{salary}', '{date}','{id}')
        '''
        if choice == "2":
            emp_system.display_employees()
            conn.execute(ins)
            conn.commit()
            conn.close()

        elif choice == "3":
            print("Exiting the Employee Management System. Goodbye!")
            break

        else:
            print("Invalid choice. Please enter a valid option.")
if __name__ == "__main__":
    main()
# conn.execute(ins)
# conn.commit()
# conn.close()