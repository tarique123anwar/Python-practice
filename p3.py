# import random
# import string
# import sqlite3

# class EmployeeManagementSystem:
#     def __init__(self):
#         self.employees = []

#     def generate_employee_id(self):
#         allowed_chars = string.digits
#         return ''.join(random.choice(allowed_chars) for _ in range(6))

#     def add_employee(self, name, position, salary, emp_joining_date, emp_dob):
#         emp_id = self.generate_employee_id()
#         employee = {"emp_id": emp_id, "name": name, "position": position, "salary": salary, "emp_joining_date": emp_joining_date, "emp_dob": emp_dob}
#         self.employees.append(employee)
#         print(f"Employee {name} added successfully with ID: {emp_id}")

#     def display_employees(self):
#         if not self.employees:
#             print("No employees to display.")
#         else:
#             print("\nEmployee List:")
#             for employee in self.employees:
#                 print(f"Employee ID: {employee['emp_id']}, Name: {employee['name']}, Position: {employee['position']}, Salary: {employee['salary']}, joining_date: {employee['emp_joining_date']}, DOB: {employee['emp_dob']}")

# def main():
#     emp_system = EmployeeManagementSystem()
#     conn = sqlite3.connect("AAJ.db")

#     # Create the employee table if it doesn't exist
#     conn.execute('''
#         CREATE TABLE IF NOT EXISTS employee (
#             emp_id TEXT,
#             emp_name TEXT,
#             emp_position TEXT,
#             emp_salary REAL,
#             emp_joining_date TEXT,
#             emp_dob TEXT
#         )
#     ''')

#     while True:
#         print("\nEmployee Management System")
#         print("1. Add Employee")
#         print("2. Display Employees")
#         print("3. Quit")

#         choice = input("Enter your choice (1/2/3): ")

#         if choice == "1":
#             try:
#                 name = input("Enter Employee Name: ")
#                 position = input("Enter Employee Position: ")
#                 salary = float(input("Enter Employee Salary: "))
#                 emp_joining_date = input("Enter Employee Joining Date (YYYY-MM-DD): ")
#                 emp_dob = input("Enter Employee Date of Birth (YYYY-MM-DD): ")
#                 emp_system.add_employee(name, position, salary, emp_joining_date, emp_dob)

#                 # Insert data into the database
#                 ins = f'''
#                     INSERT INTO employee (emp_id, emp_name, emp_position, emp_salary, emp_joining_date, emp_dob) VALUES 
#                     ('{emp_system.employees[-1]["emp_id"]}', '{name}', '{position}', '{salary}', '{emp_joining_date}', '{emp_dob}')
#                 '''
#                 conn.execute(ins)
#                 conn.commit()

#             except ValueError:
#                 print("Invalid input. Please enter a valid salary.")

#         elif choice == "2":
#             emp_system.display_employees()

#         elif choice == "3":
#             print("Exiting the Employee Management System. Goodbye!")
#             conn.close()
#             break

#         else:
#             print("Invalid choice. Please enter a valid option.")

# if __name__ == "__main__":
#     main()



        #////////////////////////////

# import random
# import string
# import sqlite3

# class EmployeeManagementSystem:
#     def __init__(self):
#         self.employees = []

#     def generate_employee_id(self, name, position):
#         allowed_chars = string.digits
#         emp_id = ''.join(random.choice(allowed_chars) for _ in range(6))
#         name_part = name[:2].upper()  # Take the first two letters of the name and convert to uppercase
#         return f"{name_part}{emp_id}{position[-1]}"

#     def add_employee(self, name, position, salary, emp_joining_date, emp_dob):
#         emp_id = self.generate_employee_id(name, position)
#         employee = {"emp_id": emp_id, "name": name, "position": position, "salary": salary, "emp_joining_date": emp_joining_date, "emp_dob": emp_dob}
#         self.employees.append(employee)
#         print(f"Employee {name} added successfully with ID: {emp_id}")

#     def display_employees(self):
#         if not self.employees:
#             print("No employees to display.")
#         else:
#             print("\nEmployee List:")
#             for employee in self.employees:
#                 print(f"Employee ID: {employee['emp_id']}, Name: {employee['name']}, Position: {employee['position']}, Salary: {employee['salary']}, Joining Date: {employee['emp_joining_date']}, DOB: {employee['emp_dob']}")

# def main():
#     emp_system = EmployeeManagementSystem()
#     conn = sqlite3.connect("AAJ.db")

#     # Create the employee table if it doesn't exist
#     conn.execute('''
#         CREATE TABLE IF NOT EXISTS employee (
#             emp_id TEXT,
#             emp_name TEXT,
#             emp_position TEXT,
#             emp_salary REAL,
#             emp_joining_date TEXT,
#             emp_dob TEXT
#         )
#     ''')

#     while True:
#         print("\nEmployee Management System")
#         print("1. Add Employee")
#         print("2. Display Employees")
#         print("3. Quit")

#         choice = input("Enter your choice (1/2/3): ")

#         if choice == "1":
#             try:
#                 name = input("Enter Employee Name: ")
#                 position = input("Enter Employee Position: ")
#                 salary = float(input("Enter Employee Salary: "))
#                 emp_joining_date = input("Enter Employee Joining Date (YYYY-MM-DD): ")
#                 emp_dob = input("Enter Employee Date of Birth (YYYY-MM-DD): ")
#                 emp_system.add_employee(name, position, salary, emp_joining_date, emp_dob)

#                 # Insert data into the database
#                 ins = f'''
#                     INSERT INTO employee (emp_id, emp_name, emp_position, emp_salary, emp_joining_date, emp_dob) VALUES 
#                     ('{emp_system.employees[-1]["emp_id"]}', '{name}', '{position}', '{salary}', '{emp_joining_date}', '{emp_dob}')
#                 '''
#                 conn.execute(ins)
#                 conn.commit()

#             except ValueError:
#                 print("Invalid input. Please enter a valid salary.")

#         elif choice == "2":
#             emp_system.display_employees()

#         elif choice == "3":
#             print("Exiting the Employee Management System. Goodbye!")
#             conn.close()
#             break

#         else:
#             print("Invalid choice. Please enter a valid option.")

# if __name__ == "__main__":
#     main()

            #(3)///////////////////
    

# import sqlite3

# class EmployeeManagementSystem:
#     def __init__(self):
#         self.employees = []

#     def generate_employee_id(self, name, position):
#         name_part = name[:2].upper()  # Take the first two letters of the name and convert to uppercase
#         return f"{name_part}{position}"

#     def add_employee(self, name, position, salary, emp_joining_date, emp_dob):
#         emp_id = self.generate_employee_id(name, position)
#         employee = {"emp_id": emp_id, "name": name, "position": position, "salary": salary, "emp_joining_date": emp_joining_date, "emp_dob": emp_dob}
#         self.employees.append(employee)
#         print(f"Employee {name} added successfully with ID: {emp_id}")

#     def display_employees(self):
#         if not self.employees:
#             print("No employees to display.")
#         else:
#             print("\nEmployee List:")
#             for employee in self.employees:
#                 print(f"Employee ID: {employee['emp_id']}, Name: {employee['name']}, Position: {employee['position']}, Salary: {employee['salary']}, Joining Date: {employee['emp_joining_date']}, DOB: {employee['emp_dob']}")

# def main():
#     emp_system = EmployeeManagementSystem()
#     conn = sqlite3.connect("AAJ.db")

#     # Create the employee table if it doesn't exist
#     conn.execute('''
#         CREATE TABLE IF NOT EXISTS employee (
#             emp_id TEXT,
#             emp_name TEXT,
#             emp_position TEXT,
#             emp_salary REAL,
#             emp_joining_date TEXT,
#             emp_dob TEXT
#         )
#     ''')

#     while True:
#         print("\nEmployee Management System")
#         print("1. Add Employee")
#         print("2. Display Employees")
#         print("3. Quit")

#         choice = input("Enter your choice (1/2/3): ")

#         if choice == "1":
#             try:
#                 name = input("Enter Employee Name: ")
#                 position = input("Enter Employee Position: ")
#                 salary = float(input("Enter Employee Salary: "))
#                 emp_joining_date = input("Enter Employee Joining Date (YYYY-MM-DD): ")
#                 emp_dob = input("Enter Employee Date of Birth (YYYY-MM-DD): ")
#                 emp_system.add_employee(name, position, salary, emp_joining_date, emp_dob)

#                 # Insert data into the database
#                 ins = f'''
#                     INSERT INTO employee (emp_id, emp_name, emp_position, emp_salary, emp_joining_date, emp_dob) VALUES 
#                     ('{emp_system.employees[-1]["emp_id"]}', '{name}', '{position}', '{salary}', '{emp_joining_date}', '{emp_dob}')
#                 '''
#                 conn.execute(ins)
#                 conn.commit()

#             except ValueError:
#                 print("Invalid input. Please enter a valid salary.")

#         elif choice == "2":
#             emp_system.display_employees()

#         elif choice == "3":
#             print("Exiting the Employee Management System. Goodbye!")
#             conn.close()
#             break

#         else:
#             print("Invalid choice. Please enter a valid option.")

# if __name__ == "__main__":
#     main()


        #///////////////////////////

# import sqlite3
# from datetime import datetime

# class EmployeeManagementSystem:
#     def __init__(self):
#         self.employees = []

#     def generate_employee_id(self, name, position):
#         name_part = name[:2].upper()  # Take the first two letters of the name and convert to uppercase
#         today = datetime.today()
#         date_part = today.strftime("%m%d")  # Get the current month and day as a two-digit string
#         return f"{name_part}{position}{date_part}"

#     def add_employee(self, name, position, salary, emp_joining_date, emp_dob):
#         emp_id = self.generate_employee_id(name, position)
#         employee = {"emp_id": emp_id, "name": name, "position": position, "salary": salary, "emp_joining_date": emp_joining_date, "emp_dob": emp_dob}
#         self.employees.append(employee)
#         print(f"Employee {name} added successfully with ID: {emp_id}")

#     def display_employees(self):
#         if not self.employees:
#             print("No employees to display.")
#         else:
#             print("\nEmployee List:")
#             for employee in self.employees:
#                 print(f"Employee ID: {employee['emp_id']}, Name: {employee['name']}, Position: {employee['position']}, Salary: {employee['salary']}, Joining Date: {employee['emp_joining_date']}, DOB: {employee['emp_dob']}")

# def main():
#     emp_system = EmployeeManagementSystem()
#     conn = sqlite3.connect("AAJ.db")

#     # Create the employee table if it doesn't exist
#     conn.execute('''
#         CREATE TABLE IF NOT EXISTS employee (
#             emp_id TEXT,
#             emp_name TEXT,
#             emp_position TEXT,
#             emp_salary REAL,
#             emp_joining_date TEXT,
#             emp_dob TEXT
#         )
#     ''')

#     while True:
#         print("\nEmployee Management System")
#         print("1. Add Employee")
#         print("2. Display Employees")
#         print("3. Quit")

#         choice = input("Enter your choice (1/2/3): ")

#         if choice == "1":
#             try:
#                 name = input("Enter Employee Name: ")
#                 position = input("Enter Employee Position: ")
#                 salary = float(input("Enter Employee Salary: "))
#                 emp_joining_date = input("Enter Employee Joining Date (YYYY-MM-DD): ")
#                 emp_dob = input("Enter Employee Date of Birth (YYYY-MM-DD): ")
#                 emp_system.add_employee(name, position, salary, emp_joining_date, emp_dob)

#                 # Insert data into the database
#                 ins = f'''
#                     INSERT INTO employee (emp_id, emp_name, emp_position, emp_salary, emp_joining_date, emp_dob) VALUES 
#                     ('{emp_system.employees[-1]["emp_id"]}', '{name}', '{position}', '{salary}', '{emp_joining_date}', '{emp_dob}')
#                 '''
#                 conn.execute(ins)
#                 conn.commit()

#             except ValueError:
#                 print("Invalid input. Please enter a valid salary.")

#         elif choice == "2":
#             emp_system.display_employees()

#         elif choice == "3":
#             print("Exiting the Employee Management System. Goodbye!")
#             conn.close()
#             break

#         else:
#             print("Invalid choice. Please enter a valid option.")

# if __name__ == "__main__":
#     main()


            ###/////////////////////////

# import sqlite3
# from datetime import datetime

# class EmployeeManagementSystem:
#     def __init__(self):
#         self.employees = []

#     def generate_employee_id(self, name, position):
#         name_part = name[:2].upper()  # Take the first two letters of the name and convert to uppercase
#         position_part = position[:2].upper()  # Take the first two letters of the position and convert to uppercase
#         today = datetime.today()
#         date_part = today.strftime("%m%d")  # Get the current month and day as a two-digit string
#         return f"{name_part}{position_part}{date_part}"

#     def add_employee(self, name, position, salary, emp_joining_date, emp_dob):
#         emp_id = self.generate_employee_id(name, position)
#         employee = {"emp_id": emp_id, "name": name, "position": position, "salary": salary, "emp_joining_date": emp_joining_date, "emp_dob": emp_dob}
#         self.employees.append(employee)
#         print(f"Employee {name} added successfully with ID: {emp_id}")

#     def display_employees(self):
#         if not self.employees:
#             print("No employees to display.")
#         else:
#             print("\nEmployee List:")
#             for employee in self.employees:
#                 print(f"Employee ID: {employee['emp_id']}, Name: {employee['name']}, Position: {employee['position']}, Salary: {employee['salary']}, Joining Date: {employee['emp_joining_date']}, DOB: {employee['emp_dob']}")

# def main():
#     emp_system = EmployeeManagementSystem()
#     conn = sqlite3.connect("AAJ.db")

#     # Create the employee table if it doesn't exist
#     conn.execute('''
#         CREATE TABLE IF NOT EXISTS employee (
#             emp_id TEXT,
#             emp_name TEXT,
#             emp_position TEXT,
#             emp_salary REAL,
#             emp_joining_date TEXT,
#             emp_dob TEXT
#         )
#     ''')

#     while True:
#         print("\nEmployee Management System")
#         print("1. Add Employee")
#         print("2. Display Employees")
#         print("3. Quit")

#         choice = input("Enter your choice (1/2/3): ")

#         if choice == "1":
#             try:
#                 name = input("Enter Employee Name: ")
#                 position = input("Enter Employee Position: ")
#                 salary = float(input("Enter Employee Salary: "))
#                 emp_joining_date = input("Enter Employee Joining Date (YYYY-MM-DD): ")
#                 emp_dob = input("Enter Employee Date of Birth (YYYY-MM-DD): ")
#                 emp_system.add_employee(name, position, salary, emp_joining_date, emp_dob)

#                 # Insert data into the database
#                 ins = f'''
#                     INSERT INTO employee (emp_id, emp_name, emp_position, emp_salary, emp_joining_date, emp_dob) VALUES 
#                     ('{emp_system.employees[-1]["emp_id"]}', '{name}', '{position}', '{salary}', '{emp_joining_date}', '{emp_dob}')
#                 '''
#                 conn.execute(ins)
#                 conn.commit()

#             except ValueError:
#                 print("Invalid input. Please enter a valid salary.")

#         elif choice == "2":
#             emp_system.display_employees()

#         elif choice == "3":
#             print("Exiting the Employee Management System. Goodbye!")
#             conn.close()
#             break

#         else:
#             print("Invalid choice. Please enter a valid option.")

# if __name__ == "__main__":
#     main()

#@////////////////////

# import sqlite3
# # from datetime import datetime

# class EmployeeManagementSystem:
#     def __init__(self):
#         self.employees = []

#     def generate_employee_id(self, name, position, dob):
#         name_part = name[:2].upper()  # Take the first two letters of the name and convert to uppercase
#         position_part = position[:1].upper()  # Take the first one letters of the position and convert to uppercase
#         dob_part = dob[5:7] + dob[8:10]  # Take the month and day part from the DOB
#         return f"{name_part}{dob_part}{position_part}"

#     def add_employee(self, name, position, salary, emp_joining_date, emp_dob,emp_mobile):
#         emp_id = self.generate_employee_id(name, position, emp_dob)
#         employee = {"emp_id": emp_id, "name": name, "position": position, "salary": salary, "emp_joining_date": emp_joining_date, "emp_dob": emp_dob,"emp_mobile":emp_mobile}
#         self.employees.append(employee)
#         print(f"Employee {name} added successfully with ID: {emp_id}")

#     def display_employees(self):
#         if not self.employees:
#             print("No employees to display.")
#         else:
#             print("\nEmployee List:")
#             for employee in self.employees:
#                 print(f"Employee ID: {employee['emp_id']}, Name: {employee['name']}, Position: {employee['position']}, Salary: {employee['salary']}, Joining Date: {employee['emp_joining_date']}, DOB: {employee['emp_dob']}")

# def main():
#     emp_system = EmployeeManagementSystem()
#     conn = sqlite3.connect("aapka.db")

#     # Create the employee table if it doesn't exist
#     conn.execute('''
#         CREATE TABLE IF NOT EXISTS employee (
#             emp_id TEXT,
#             emp_name TEXT,
#             emp_position TEXT,
#             emp_salary REAL,
#             emp_joining_date TEXT,
#             emp_mobile TEXT,
#             emp_dob TEXT
#         )
#     ''')

#     while True:
#         print("\nEmployee Management System")
#         print("1. Add Employee")
#         print("2. Display Employees")
#         print("3. Quit")

#         choice = input("Enter your choice (1/2/3): ")

#         if choice == "1":
#             try:
#                 name = input("Enter Employee Name: ")
#                 position = input("Enter Employee Position: ")
#                 salary = float(input("Enter Employee Salary: "))
#                 emp_joining_date = input("Enter Employee Joining Date (YYYY-MM-DD): ")
#                 emp_dob = input("Enter Employee Date of Birth (YYYY-MM-DD): ")
#                 emp_mobile = input("Enter Employee Mobile Number: ")
#                 emp_system.add_employee(name, position, salary, emp_joining_date, emp_dob , emp_mobile)

#                 # Insert data into the database
#                 ins = f'''
#                     INSERT INTO employee (emp_id, emp_name, emp_position, emp_salary, emp_joining_date, emp_dob ,emp_mobile) VALUES 
#                     ('{emp_system.employees[-1]["emp_id"]}', '{name}', '{position}', '{salary}', '{emp_joining_date}', '{emp_dob}',{emp_mobile})
#                 '''
#                 conn.execute(ins)
#                 conn.commit()

#             except ValueError:
#                 print("Invalid input. Please enter a valid salary.")

#         elif choice == "2":
#             emp_system.display_employees()

#         elif choice == "3":
#             print("Exiting the Employee Management System. Goodbye!")
#             conn.close()
#             break

#         else:
#             print("Invalid choice. Please enter a valid option.")

# if __name__ == "__main__":
#     main()


    
# import sqlite3

# class EmployeeManagementSystem:
#     def __init__(self):
#         self.employees = []

#     def generate_employee_id(self, name, position, dob):
#         name_part = name[:2].upper()  # Take the first two letters of the name and convert to uppercase
#         position_part = position[:1].upper()  # Take the first one letters of the position and convert to uppercase
#         dob_part = dob[5:7] + dob[8:10]  # Take the month and day part from the DOB
#         return f"{name_part}{dob_part}{position_part}"

#     def add_employee(self, name, position, salary, emp_joining_date, emp_dob, emp_mobile):
#         emp_id = self.generate_employee_id(name, position, emp_dob)
#         employee = {"emp_id": emp_id, "name": name, "position": position, "salary": salary, "emp_joining_date": emp_joining_date, "emp_dob": emp_dob, "emp_mobile": emp_mobile}
#         self.employees.append(employee)
#         print(f"Employee {name} added successfully with ID: {emp_id}")

#     def display_employees(self):
#         if not self.employees:
#             print("No employees to display.")
#         else:
#             print("\nEmployee List:")
#             for employee in self.employees:
#                 print(f"Employee ID: {employee['emp_id']}, Name: {employee['name']}, Position: {employee['position']}, Salary: {employee['salary']}, Joining Date: {employee['emp_joining_date']}, DOB: {employee['emp_dob']}, Mobile: {employee['emp_mobile']}")

#     def delete_employee(self, emp_id):
#         for employee in self.employees:
#             if employee['emp_id'] == emp_id:
#                 self.employees.remove(employee)
#                 print(f"Employee {employee['name']} with ID {emp_id} deleted successfully.")
#                 return True
#         print(f"No employee found with ID {emp_id}. Deletion unsuccessful.")
#         return False

# def main():
#     emp_system = EmployeeManagementSystem()
#     conn = sqlite3.connect("aapka.db")

#     # Create the employee table if it doesn't exist
#     conn.execute('''
#         CREATE TABLE IF NOT EXISTS employee (
#             emp_id TEXT,
#             emp_name TEXT,
#             emp_position TEXT,
#             emp_salary REAL,
#             emp_joining_date TEXT,
#             emp_mobile TEXT,
#             emp_dob TEXT
#         )
#     ''')

#     while True:
#         print("\nEmployee Management System")
#         print("1. Add Employee")
#         print("2. Display Employees")
#         print("3. Delete Employee")
#         print("4. Quit")

#         choice = input("Enter your choice (1/2/3/4): ")

#         if choice == "1":
#             try:
#                 name = input("Enter Employee Name: ")
#                 position = input("Enter Employee Position: ")
#                 salary = float(input("Enter Employee Salary: "))
#                 emp_joining_date = input("Enter Employee Joining Date (YYYY-MM-DD): ")
#                 emp_dob = input("Enter Employee Date of Birth (YYYY-MM-DD): ")
#                 emp_mobile = input("Enter Employee Mobile Number: ")
#                 emp_system.add_employee(name, position, salary, emp_joining_date, emp_dob, emp_mobile)

#                 # Insert data into the database
#                 ins = f'''
#                     INSERT INTO employee (emp_id, emp_name, emp_position, emp_salary, emp_joining_date, emp_dob ,emp_mobile) VALUES 
#                     ('{emp_system.employees[-1]["emp_id"]}', '{name}', '{position}', '{salary}', '{emp_joining_date}', '{emp_dob}', '{emp_mobile}')
#                 '''
#                 conn.execute(ins)
#                 conn.commit()

#             except ValueError:
#                 print("Invalid input. Please enter a valid salary.")

#         elif choice == "2":
#             emp_system.display_employees()

#         elif choice == "3":
#             emp_id_to_delete = input("Enter the Employee ID to delete: ")
#             emp_system.delete_employee(emp_id_to_delete)

#             # Delete data from the database
#             delete_query = f"DELETE FROM employee WHERE emp_id = '{emp_id_to_delete}'"
#             conn.execute(delete_query)
#             conn.commit()

#         elif choice == "4":
#             print("Exiting the Employee Management System. Goodbye!")
#             conn.close()
#             break

#         else:
#             print("Invalid choice. Please enter a valid option.")

# if __name__ == "__main__":
#     main()


#////////////////

# import streamlit as st
# import sqlite3

# class EmployeeManagementSystem:
#     def __init__(self):
#         self.conn = sqlite3.connect("aapka.db")

#         self.cur = self.conn.cursor()

#     def generate_employee_id(self, name, position, dob):
#         name_part = name[:2].upper()
#         position_part = position[:1].upper()
#         dob_part = dob[5:7] + dob[8:10]
#         return f"{name_part}{dob_part}{position_part}"
    
            #/////////////
# import sqlite3
# class EmployeeManagementSystem:
#     def __init__(self):
#         self.conn = sqlite3.connect("Anwar.db")
#         self.cur = self.conn.cursor()

#     def generate_employee_id(self, name, position, dob):
#         # Split the name into first name and last name
#         first_name, last_name = name.split()
        
#         # Extract the first letters of the first and last names
#         first_name_initial = first_name[0].upper()
#         last_name_initial = last_name[0].upper()
        
#         # Extract the relevant parts of the date of birth
#         dob_part = dob[5:7] + dob[8:10]
        
#         # Extract the first letter of the position
#         position_part = position[:1].upper()
        
#         # Combine the initials and dob parts to generate the employee ID
#         return f"{first_name_initial}{last_name_initial}{dob_part}{position_part}"
#             #////////////

#     def add_employee(self, name, position, salary, emp_joining_date, emp_dob, emp_mobile):
#         emp_id = self.generate_employee_id(name, position, emp_dob)
#         ins = '''
#             INSERT INTO employee (emp_id, emp_name, emp_position, emp_salary, emp_joining_date, emp_dob, emp_mobile) VALUES 
#             (?, ?, ?, ?, ?, ?, ?)
#         '''
#         self.cur.execute(ins, (emp_id, name, position, salary, emp_joining_date, emp_dob, emp_mobile))
#         self.conn.commit()
#         print(f"Employee {name} added successfully with ID: {emp_id}")

#     def display_employees(self):
#         self.cur.execute("SELECT * FROM employee")  #//////////// cur is a cursor / .execute is the database execution 
#         rows = self.cur.fetchall()
#         if not rows:
#             print("No employees to display.")
#         else:
#             print("\nEmployee List:")
#             for row in rows:
#                 emp_id, name, position, salary, emp_joining_date, emp_dob, emp_mobile = row
#                 print(f"Employee ID: {emp_id}\nName: {name}\nPosition: {position}\nSalary: {salary}\nJoining Date: {emp_joining_date}\nDOB: {emp_dob}\nMobile: {emp_mobile}\n")

#     def show_employee_by_id(self, emp_id):
#         self.cur.execute("SELECT * FROM employee WHERE emp_id = ?", (emp_id,))
#         row = self.cur.fetchone()
#         if row:
#             emp_id, name, position, salary, emp_joining_date, emp_dob, emp_mobile = row
#             print("\nEmployee Details:")
#             print(f"Employee ID: {emp_id}\nName: {name}\nPosition: {position}\nSalary: {salary}\nJoining Date: {emp_joining_date}\nDOB: {emp_dob}\nMobile: {emp_mobile}\n")
#         else:
#             print(f"No employee found with ID {emp_id}.")

#     def edit_employee(self, emp_id, new_name, new_position, new_salary, new_joining_date, new_dob, new_mobile):
#         update_query = '''
#             UPDATE employee
#             SET emp_name=?, emp_position=?, emp_salary=?, emp_joining_date=?, emp_dob=?, emp_mobile=?
#             WHERE emp_id=?
#         '''
#         self.cur.execute(update_query, (new_name, new_position, new_salary, new_joining_date, new_dob, new_mobile, emp_id))
#         if self.cur.rowcount > 0:
#             print(f"Employee with ID {emp_id} updated successfully.")
#             self.conn.commit()
#         else:
#             print(f"No employee found with ID {emp_id}. Update unsuccessful.")

#     def delete_employee(self, emp_id):
#         self.cur.execute("DELETE FROM employee WHERE emp_id = ?", (emp_id,))
#         if self.cur.rowcount > 0:
#             print(f"Employee with ID {emp_id} deleted successfully.")
#             self.conn.commit()
#         else:
#             print(f"No employee found with ID {emp_id}. Deletion unsuccessful.")

# def main():
#     emp_system = EmployeeManagementSystem()

#     while True:
#         print("\nEmployee Management System")
#         print("1. Add Employee")
#         print("2. Display All Employees")               
#         print("3. Show Employee by ID")
#         print("4. Edit Employee")
#         print("5. Delete Employee")
#         print("6. Quit")

#         choice = input("Enter your choice (1/2/3/4/5/6): ")

#         if choice == "1":
#             try:
#                 name = input("Enter Employee Name: ")
#                 position = input("Enter Employee Position: ")
#                 emp_mobile = input("Enter Employee Mobile Number: ")
#                 emp_dob = input("Enter Employee Date of Birth (YYYY-MM-DD): ")
#                 emp_joining_date = input("Enter Employee Joining Date (YYYY-MM-DD): ")
#                 salary = float(input("Enter Employee Salary: "))

#                 emp_system.add_employee(name, position, emp_mobile , emp_dob , emp_joining_date , salary)

#             except ValueError:
#                 print("Invalid input. Please enter a valid salary.")
 
#         elif choice == "2":
#             emp_system.display_employees()

#         elif choice == "3":
#             emp_id_to_show = input("Enter the Employee ID to show: ")
#             emp_system.show_employee_by_id(emp_id_to_show)

#         elif choice == "4":
#             try:
#                 emp_id_to_edit = input("Enter the Employee ID to edit: ")
#                 new_name = input("Enter the new Employee Name: ")
#                 new_position = input("Enter the new Employee Position: ")
#                 new_mobile = input("Enter the new Employee Mobile Number: ")
#                 new_dob = input("Enter the new Employee Date of Birth (YYYY-MM-DD): ") 
#                 new_joining_date = input("Enter the new Employee Joining Date (YYYY-MM-DD): ")
#                 new_salary = float(input("Enter the new Employee Salary: "))

#                 emp_system.edit_employee(emp_id_to_edit, new_name, new_position,new_mobile, new_dob,new_joining_date,new_salary)

#             except ValueError:
#                 print("Invalid input. Please enter a valid salary.")
                
#         elif choice == "5":
#             emp_id_to_delete = input("Enter the Employee ID to delete: ")
#             emp_system.delete_employee(emp_id_to_delete)

#         elif choice == "6":
#             print("Exiting the Employee Management System. Goodbye!")
#             emp_system.conn.close()
#             break

#         else:
#             print("Invalid choice. Please enter a valid option.")

# if __name__ == "__main__":
#     main()

        ##///////////////

import sqlite3
from datetime import datetime
class EmployeeManagementSystem:
    def __init__(self, db_name):
        self.conn = sqlite3.connect("data2.db")
        self.cur = self.conn.cursor()
        self.create_table()

    def create_table(self):
        self.cur.execute('''
        
            CREATE TABLE IF NOT EXISTS employee (
                emp_id VARCHAR(10),
                emp_name TEXT,
                emp_position TEXT,
                emp_mobile VARCHAR(15),
                emp_dob DATE,
                emp_joining_date DATE,
                emp_salary DECIMAL(10, 2)
            )
        ''')
        self.conn.commit()

    def generate_employee_id(self, emp_name,emp_position, emp_dob):
        first_name = emp_name.split()
        last_name = emp_name.split()
            
        dob_part = emp_dob[5:7] + emp_dob[8:10]
        position_part = emp_position[:1].upper()
        return f"{first_name_initial}{last_name_initial}{dob_part}{position_part}"

    def add_employee(self, emp_name, emp_position, emp_mobile, emp_dob, emp_joining_date, salary):
        emp_id = self.generate_employee_id(emp_name, emp_position, emp_dob)
        ins = '''
            INSERT INTO employee (emp_id, emp_name, emp_position, emp_mobile, emp_dob, emp_joining_date, emp_salary) VALUES 
            (?, ?, ?, ?, ?, ?, ?)
        '''
        self.cur.execute(ins, (emp_id, emp_name, emp_position, emp_mobile, emp_dob, emp_joining_date, salary))
        self.conn.commit()
        print(f"Employee {emp_name} added successfully with ID: {emp_id}")

    def display_employees(self):
        self.cur.execute("SELECT * FROM employee")
        rows = self.cur.fetchall()
        if not rows:
            print("No employees to display.")
        else:
            print("\nEmployee List:")
            for row in rows:
                emp_id, emp_name, emp_position, emp_mobile, emp_dob, emp_joining_date, salary = row
                print(f"Employee ID: {emp_id}\nName: {emp_name}\nPosition: {emp_position}\nMobile: {emp_mobile}\nDOB: {emp_dob}\nJoining Date: {emp_joining_date}\nSalary: {salary}\n")

    def show_employee_by_id(self, emp_id):
        self.cur.execute("SELECT * FROM employee WHERE emp_id = ?", (emp_id,))
        row = self.cur.fetchone()
        if row:
            emp_id, emp_name, emp_position, emp_mobile, emp_dob, emp_joining_date, salary = row
            print("\nEmployee Details:")
            print(f"Employee ID: {emp_id}\nName: {emp_name}\nPosition: {emp_position}\nMobile: {emp_mobile}\nDOB: {emp_dob}\nJoining Date: {emp_joining_date}\nSalary: {salary}\n")
        else:
            print(f"No employee found with ID {emp_id}.")

    def edit_employee(self, emp_id, new_name, new_position, new_mobile, new_dob, new_joining_date, new_salary):
        update_query = '''
            UPDATE employee
            SET emp_name=?, emp_position=?, emp_mobile=?, emp_dob=?, emp_joining_date=?, emp_salary=?
            WHERE emp_id=?
        '''
        self.cur.execute(update_query, (new_name, new_position, new_mobile, new_dob, new_joining_date, new_salary, emp_id))
        if self.cur.rowcount > 0:
            print(f"Employee with ID {emp_id} updated successfully.")
            self.conn.commit()
        else:
            print(f"No employee found with ID {emp_id}. Update unsuccessful.")

    def delete_employee(self, emp_id):
        self.cur.execute("DELETE FROM employee WHERE emp_id = ?", (emp_id,))
        if self.cur.rowcount > 0:
            print(f"Employee with ID {emp_id} deleted successfully.")
            self.conn.commit()
        else:
            print(f"No employee found with ID {emp_id}. Deletion unsuccessful.")

def main():
    db_name = "aapka.db"
    emp_system = EmployeeManagementSystem(db_name)

    while True:
        print("\nEmployee Management System")
        print("1. Add Employee")
        print("2. Display All Employees")
        print("3. Show Employee by ID")
        print("4. Edit Employee")
        print("5. Delete Employee")
        print("6. Quit")

        choice = input("Enter your choice (1/2/3/4/5/6): ")

        #////////////////////
            
            # is_flag =True
            # while is_flag:
            #     try:
            #         name = (input("Enter Employee Full_Name: "))
            #         is_flag = False
            #     except Exception as e:
            #         print("pl enter the char")
            #         is_flag = True
                    #return None
            # flagName = False
            # while not flagName:
            #         name = input("Enter Employee Full_Name: ")
            #         if name != '':
            #             flagName = True
            #         else:
            #             print('Error: Employee name cannot be empty.')
            #         return name  # Return the valid input name
        def get_employee_name():
            validInteger = False
            while not validInteger:
                name = input("enter the full_name:")
                if name.isalpha():
                    validInteger = True
                    return name
                else:
                    print('Pl enter the valid name')

            # print('You are ' + str(age))

                #//////////
        def get_employee_position():
            validInteger = False
            while not validInteger:
                position = input("Enter Employee Position: ")
                if position.isalpha():
                    validInteger=True
                    return position
                else:
                    print("Pl enter the valid value")

                #/////

        def get_employee_mobile():
            validInteger = False
            while not validInteger: 
                emp_mobile = input("Enter Employee Mobile Number: ")
                if emp_mobile.isdigit():
                    validInteger=True
                    return emp_mobile
                else:
                    print("Pl enter the valid value")

            # try:
            #     emp_mobile = int(input("Enter Employee Mobile Number: "))
            #     return emp_mobile
            # except Exception as e:
            #     print(f"Error: {e}")
                #return None

        def get_employee_dob():
            while True:
                emp_dob = input("Enter Employee Date of Birth (YYYY-MM-DD): ")
                try:
                    datetime.strptime(emp_dob, "%Y-%m-%d")
                    return emp_dob  # Return the valid date input
                except ValueError:
                    print("Please enter a valid date in the format YYYY-MM-DD")

# Example usage
                # employee_dob = get_employee_dob()
                # print("Employee Date of Birth:", employee_dob)



                #return None

        def get_employee_joining_date():
            while True:
                emp_joining_date = input("Enter Employee_joining_date (YYYY-MM-DD): ")
                try:
                    datetime.strptime(emp_joining_date, "%Y-%m-%d")
                    return emp_joining_date  # Return the valid date input
                except ValueError:
                    print("Please enter a valid date in the format YYYY-MM-DD")

# Example usage
                # joining_date = get_employee_joining_date()
                # # print("Employee joining_date:", joining_date)

        # def get_employee_salary():
        #     validInteger=False
        #     while not validInteger:
        #         salary = (input("Enter Employee Salary:"))
        #         if salary.isdigit():
        #             validInteger=True
        #         else:
        #             print("Pl enter the valid value")

        def get_employee_salary():
            validInput = False
            while not validInput:
                salary = input("Enter Employee Salary: ")
                if salary.isdigit():
                    validInput = True
                    return salary
                else:
                    print("Error: Please enter a valid value.")
            # return salary

          ##///////////////////////////
        # if choice == "1":
        #     name = get_employee_name()
        #     position = get_employee_position()
        #     emp_mobile = get_employee_mobile()
        #     emp_dob = get_employee_dob()
        #     emp_joining_date = get_employee_joining_date()
        #     salary = get_employee_salary()

            # if all([name, position, emp_mobile, emp_dob, emp_joining_date, salary]):
            #         emp_system.add_employee(name, position, emp_mobile, emp_dob, emp_joining_date, salary)
           
        if choice == "1":
            emp_name = get_employee_name()
            emp_position = get_employee_position()
            emp_mobile = get_employee_mobile()
            emp_dob = get_employee_dob()
            emp_joining_date = get_employee_joining_date()
            salary = get_employee_salary()
            print("values", emp_name, emp_position, emp_mobile, emp_dob, emp_joining_date, salary)

            if all([emp_name, emp_position, emp_mobile, emp_dob, emp_joining_date, salary]):
                emp_system.add_employee(emp_name, emp_position, emp_mobile, emp_dob, emp_joining_date, salary)
            else:
                print("Error in input. Please try again.")

        elif choice == "2":
            emp_system.display_employees()

        elif choice == "3":
            emp_id_to_show = input("Enter the Employee ID to show: ")
            emp_system.show_employee_by_id(emp_id_to_show)

        elif choice == "4":
            # try:
                emp_id_to_edit = input("Enter the Employee ID to edit: ")
                new_name = input("Enter the new Employee Name: ")
                new_position = input("Enter the new Employee Position: ")
                new_mobile = input("Enter the new Employee Mobile Number: ")
                new_dob = input("Enter the new Employee Date of Birth (YYYY-MM-DD): ") 
                new_joining_date = input("Enter the new Employee Joining Date (YYYY-MM-DD): ")
                new_salary = (input("Enter the new Employee Salary: "))

                emp_system.edit_employee(emp_id_to_edit, new_name, new_position, new_mobile, new_dob, new_joining_date, new_salary)

            # # except ValueError as e:
            #     print(e)
                
        elif choice == "5":
            emp_id_to_delete = input("Enter the Employee ID to delete: ")
            emp_system.delete_employee(emp_id_to_delete)

        elif choice == "6":
            print("Exiting the Employee Management System. Goodbye!")
            emp_system.conn.close()
            break

        else:
            print("Invalid choice. Please enter a valid option.")

if __name__ == "__main__":
    main()


        ##///////////////////////
    



# import sqlite3

# class EmployeeManagementSystem:
#     def __init__(self, db_name):
#         self.conn = sqlite3.connect("Anwar.db")
#         self.cur = self.conn.cursor()
#         self.create_table()

#     def create_table(self):
#         self.cur.execute('''
#             CREATE TABLE IF NOT EXISTS employee (
#                 emp_id VARCHAR(10),
#                 first_name TEXT,
#                 last_name TEXT,
#                 emp_name TEXT,
#                 emp_position TEXT,
#                 emp_mobile VARCHAR(15),
#                 emp_dob DATE,
#                 emp_joining_date DATE,
#                 emp_salary DECIMAL(10, 2)
#             )
#         ''')
#         self.conn.commit()

#     def generate_employee_id(self, first_name, last_name, position, dob):
#         first_name_initial = first_name[0].upper()
#         last_name_initial = last_name[0].upper()
#         dob_part = dob[5:7] + dob[8:10]
#         position_part = position[:1].upper()
#         return f"{first_name_initial}{last_name_initial}{dob_part}{position_part}"

#     def add_employee(self, first_name, last_name, position, emp_mobile, emp_dob, emp_joining_date, salary):
#         emp_name = f"{first_name} {last_name}"
#         emp_id = self.generate_employee_id(first_name, last_name, position, emp_dob)
#         ins = '''
#             INSERT INTO employee (emp_id, first_name, last_name, emp_name, emp_position, emp_mobile, emp_dob, emp_joining_date, emp_salary) VALUES 
#             (?, ?, ?, ?, ?, ?, ?, ?, ?)
#         '''
#         self.cur.execute(ins, (emp_id, first_name, last_name, emp_name, position, emp_mobile, emp_dob, emp_joining_date, salary))
#         self.conn.commit()
#         print(f"Employee {emp_name} added successfully with ID: {emp_id}")

#     def display_employees(self):
#         self.cur.execute("SELECT * FROM employee")
#         rows = self.cur.fetchall()
#         if not rows:
#             print("No employees to display.")
#         else:
#             print("\nEmployee List:")
#             for row in rows:
#                 emp_id, first_name, last_name, emp_name, position, emp_mobile, emp_dob, emp_joining_date, salary = row
#                 print(f"Employee ID: {emp_id}\nFirst Name: {first_name}\nLast Name: {last_name}\nName: {emp_name}\nPosition: {position}\nMobile: {emp_mobile}\nDOB: {emp_dob}\nJoining Date: {emp_joining_date}\nSalary: {salary}\n")

#     def show_employee_by_id(self, emp_id):
#         self.cur.execute("SELECT * FROM employee WHERE emp_id = ?", (emp_id,))
#         row = self.cur.fetchone()
#         if row:
#             emp_id, first_name, last_name, emp_name, position, emp_mobile, emp_dob, emp_joining_date, salary = row
#             print("\nEmployee Details:")
#             print(f"Employee ID: {emp_id}\nFirst Name: {first_name}\nLast Name: {last_name}\nName: {emp_name}\nPosition: {position}\nMobile: {emp_mobile}\nDOB: {emp_dob}\nJoining Date: {emp_joining_date}\nSalary: {salary}\n")
#         else:
#             print(f"No employee found with ID {emp_id}.")

#     def edit_employee(self, emp_id, first_name, last_name, new_position, new_mobile, new_dob, new_joining_date, new_salary):
#         update_query = '''
#             UPDATE employee
#             SET first_name=?, last_name=?, emp_position=?, emp_mobile=?, emp_dob=?, emp_joining_date=?, emp_salary=?
#             WHERE emp_id=?
#         '''
#         self.cur.execute(update_query, (first_name, last_name, new_position, new_mobile, new_dob, new_joining_date, new_salary, emp_id))
#         if self.cur.rowcount > 0:
#             print(f"Employee with ID {emp_id} updated successfully.")
#             self.conn.commit()
#         else:
#             print(f"No employee found with ID {emp_id}. Update unsuccessful.")

#     def delete_employee(self, emp_id):
#         self.cur.execute("DELETE FROM employee WHERE emp_id = ?", (emp_id,))
#         if self.cur.rowcount > 0:
#             print(f"Employee with ID {emp_id} deleted successfully.")
#             self.conn.commit()
#         else:
#             print(f"No employee found with ID {emp_id}. Deletion unsuccessful.")

# def main():
#     db_name = "Anwar.db"
#     emp_system = EmployeeManagementSystem(db_name)

#     while True:
#         print("\nEmployee Management System")
#         print("1. Add Employee")
#         print("2. Display All Employees")
#         print("3. Show Employee by ID")
#         print("4. Edit Employee")
#         print("5. Delete Employee")
#         print("6. Quit")

#         choice = input("Enter your choice (1/2/3/4/5/6): ")

#         if choice == "1":
#             try:
#                 first_name = input("Enter Employee First Name: ")
#                 last_name = input("Enter Employee Last Name: ")
#                 position = input("Enter Employee Position: ")
#                 emp_mobile = input("Enter Employee Mobile Number: ")
#                 emp_dob = input("Enter Employee Date of Birth (YYYY-MM-DD): ")
#                 emp_joining_date = input("Enter Employee Joining Date (YYYY-MM-DD): ")
#                 salary = input("Enter Employee Salary: ")
#                 emp_system.add_employee(first_name, last_name, position, emp_mobile, emp_dob, emp_joining_date, salary)

#             except ValueError as e:
#                 print(e)
 
#         elif choice == "2":
#             emp_system.display_employees()

#         elif choice == "3":
#             emp_id_to_show = input("Enter the Employee ID to show: ")
#             emp_system.show_employee_by_id(emp_id_to_show)

#         elif choice == "4":
#             try:
#                 emp_id_to_edit = input("Enter the Employee ID to edit: ")
#                 new_first_name = input("Enter the new Employee First Name: ")
#                 new_last_name = input("Enter the new Employee Last Name: ")
#                 new_position = input("Enter the new Employee Position: ")
#                 new_mobile = input("Enter the new Employee Mobile Number: ")
#                 new_dob = input("Enter the new Employee Date of Birth (YYYY-MM-DD): ") 
#                 new_joining_date = input("Enter the new Employee Joining Date (YYYY-MM-DD): ")
#                 new_salary = input("Enter the new Employee Salary: ")

#                 emp_system.edit_employee(emp_id_to_edit, new_first_name, new_last_name, new_position, new_mobile, new_dob, new_joining_date, new_salary)

#             except ValueError:
#                 print("Invalid input. Please enter valid data.")
                
#         elif choice == "5":
#             emp_id_to_delete = input("Enter the Employee ID to delete: ")
#             emp_system.delete_employee(emp_id_to_delete)

#         elif choice == "6":
#             print("Exiting the Employee Management System. Goodbye!")
#             emp_system.conn.close()
#             break

#         else:
#             print("Invalid choice. Please enter a valid option.")

# if __name__ == "__main__":
#     main()

#         ##////////////

# from selenium import webdriver
# from selenium.webdriver.common.by import By
# from selenium.webdriver.common.keys import Keys
# import time
# def perform_actions():
#     # Initialize Chrome WebDriver
#     driver = webdriver.Chrome()
#     driver.maximize_window()
#     driver.get("http://live.curengo.in/login")
#     time.sleep(3)
#     # Find the username input field and enter the username
#     number_field = driver.find_element(By.XPATH, "//input[@id='mobile_number']")
#     number_field.send_keys("6301214546")
#     # Find the password input field and enter the password
#     password_field = driver.find_element(By.XPATH, "//input[@id='password']")
#     password_field.send_keys("Ucchvas@123")
#     time.sleep(2)
#     # Find the submit button and click it to log in
#     login_button = driver.find_element(By.XPATH, "(//span[@class='MuiButton-label'])[1]")
#     login_button.click()
#     time.sleep(2)
#     # Navigate to Appointments page
#     appointments_button = driver.find_element(By.XPATH, "(//*[name()='svg'][@class='MuiSvgIcon-root'])[2]")
#     appointments_button.click()
#     time.sleep(2)
#     # Select a date on the calendar
#     date = driver.find_element(By.XPATH, "//span[normalize-space()='13']")
#     date.click()
#     time.sleep(2)
#     # Click on "Add Appointment" button
#     add_appointment_button = driver.find_element(By.XPATH, "(//span[@class='MuiFab-label'])[1]")
#     add_appointment_button.click()
#     time.sleep(2)
#     # Select the clinic name
#     clinic_name_dropdown = driver.find_element(By.XPATH, "(//div[@id='demo-simple-select'])[1]")
#     clinic_name_dropdown.click()
#     select_clinic = driver.find_element(By.XPATH, "(//li[@name='Ucchvas Banjara Hills Unit 1'])[1]")
#     select_clinic.click()
#     time.sleep(1)
#     # Enter patient name
#     patient_name_field = driver.find_element(By.XPATH, "(//input[@id='auto-complete'])[1]")
#     patient_name_field.send_keys("hanishani")
#     patient_name_field.send_keys()
#     time.sleep(4)
#     # Select patient from dropdown
#     select_patient = driver.find_elements(By.XPATH, "(//input[@fdprocessedid='yjygp'])[2]")
#     patient = "hanishani"
#     for option in select_patient:
#         if option.text == patient:
#             option.send_keys(Keys.ENTER)
#     # time.sleep(10)
#     time.sleep(2)
#     # Enter service name
#     service_name_dropdown = driver.find_element(By.XPATH, "(//input[@type='text'])[3]")
#     service_name_dropdown.send_keys("Exercise Electrotherapy")
#     time.sleep(2)
#     driver.quit()
# # Call the function to perform the actions
# perform_actions()


#         #####

# from selenium import webdriver
# from selenium.webdriver.common.by import By
# from selenium.webdriver.common.keys import Keys
# import time

# def perform_actions():
#     # Initialize Chrome WebDriver
#     driver = webdriver.Chrome()
#     driver.maximize_window()
#     driver.get("http://live.curengo.in/login")
#     time.sleep(3)
#     # Find the username input field and enter the username
#     number_field = driver.find_element(By.ID, "mobile_number")
#     number_field.send_keys("6301214546")
#     # Find the password input field and enter the password
#     password_field = driver.find_element(By.ID, "password")
#     password_field.send_keys("Ucchvas@123")
#     time.sleep(2)
#     # Find the submit button and click it to log in
#     login_button = driver.find_element(By.XPATH, "//button[@type='submit']")
#     login_button.click()
#     time.sleep(2)
#     # Navigate to Appointments page
#     appointments_button = driver.find_element(By.XPATH, "(//svg[contains(@class,'MuiSvgIcon-root')])[2]")
#     appointments_button.click()
#     time.sleep(2)
#     # Select a date on the calendar
#     date = driver.find_element(By.XPATH, "//span[text()='13']")
#     date.click()
#     time.sleep(2)
#     # Click on "Add Appointment" button
#     add_appointment_button = driver.find_element(By.XPATH, "(//span[text()='Add Appointment'])[1]")
#     add_appointment_button.click()
#     time.sleep(2)
#     # Select the clinic name
#     clinic_name_dropdown = driver.find_element(By.XPATH, "(//div[@id='demo-simple-select'])[1]")
#     clinic_name_dropdown.click()
#     select_clinic = driver.find_element(By.XPATH, "//li[@name='Ucchvas Banjara Hills Unit 1']")
#     select_clinic.click()
#     time.sleep(1)
#     # Enter patient name
#     patient_name_field = driver.find_element(By.XPATH, "(//input[@id='auto-complete'])[1]")
#     patient_name_field.send_keys("hanishani")
#     time.sleep(4)
#     # Select patient from dropdown
#     select_patient = driver.find_element(By.XPATH, "//input[@fdprocessedid='yjygp']")
#     select_patient.send_keys(Keys.ENTER)
#     time.sleep(2)
#     # Enter service name
#     service_name_dropdown = driver.find_element(By.XPATH, "(//input[@type='text'])[3]")
#     service_name_dropdown.send_keys("Exercise Electrotherapy")
#     time.sleep(2)
#     driver.quit()

# # Call the function to perform the actions
# perform_actions()
            #/////////////////////////////////

# import unittest
# from selenium import webdriver
# from selenium.webdriver.common.by import By
# # Initialize Chrome WebDriver
# import time
# from selenium.webdriver.support.wait import WebDriverWait
# from selenium.webdriver.support import expected_conditions as EC
# import time
# class LoginTestCase(unittest.TestCase):
#     def setUp(self):
#         # Initialize the WebDriver
#         self.driver = webdriver.Chrome()
#         self.driver.maximize_window()
#         time.sleep(5)
#         # URL of the login page
#         self.login_url = "https://test.admin.experiense.ai/"
#     def test_successful_login(self):
#         # # Navigate to the login page
#         # self.driver.get(self.login_url)
#         # Find the username and password input fields and submit button
#         username_field = self.driver.find_element(By.CSS_SELECTOR, "#email-login")
#         password_field = self.driver.find_element(By.CSS_SELECTOR, "#-password-login")
#         login_button = self.driver.find_element(By.CSS_SELECTOR, "button[type='submit']")
#         # Enter the username and password
#         username_field.send_keys("superadmin")
#         password_field.send_keys("Experiense@123")
#         # Click on the login button
#         login_button.click()
#         # Check if login was successful by verifying the presence of a welcome message
#         welcome_message = self.driver.find_element_by_id("welcome-message")
#         self.assertTrue(welcome_message.is_displayed())
#     def test_invalid_login(self):
#         # Navigate to the login page
#         self.driver.get(self.login_url)
#         # Find the username and password input fields and submit button
#         username_field = self.driver.find_element(By.CSS_SELECTOR, "#email-login")
#         password_field = self.driver.find_element(By.CSS_SELECTOR, "#-password-login")
#         login_button = self.driver.find_element(By.CSS_SELECTOR, "button[type='submit']")
#         # Enter invalid username and password
#         username_field.send_keys("invalid_user")
#         password_field.send_keys("invalid_password")
#         # Click on the login button
#         login_button.click()
#         # Check if error message is displayed
#         error_message = self.driver.find_element(By.CSS_SELECTOR, "div[role='alert']")
#         self.assertTrue(error_message.is_displayed())
#     def tearDown(self):
#         # Close the browser
#         self.driver.quit()
# if __name__ == "__main__":
#     unittest.main()