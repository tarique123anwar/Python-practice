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



                #/////////////////////
    
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
    

import sqlite3

class EmployeeManagementSystem:
    def __init__(self):
        self.conn = sqlite3.connect("aapka.db")
        self.cur = self.conn.cursor()

    def generate_employee_id(self, name, position, dob):
        name_part = name[:2].upper()  # Take the first two letters of the name and convert to uppercase
        position_part = position[:1].upper()  # Take the first one letter of the position and convert to uppercase
        dob_part = dob[5:7] + dob[8:10]  # Take the month and day part from the DOB
        return f"{name_part}{dob_part}{position_part}"

    def add_employee(self, name, position, salary, emp_joining_date, emp_dob, emp_mobile):
        emp_id = self.generate_employee_id(name, position, emp_dob)
        ins = f'''
            INSERT INTO employee (emp_id, emp_name, emp_position, emp_salary, emp_joining_date, emp_dob, emp_mobile) VALUES 
            (?, ?, ?, ?, ?, ?, ?)
        '''
        self.cur.execute(ins, (emp_id, name, position, salary, emp_joining_date, emp_dob, emp_mobile))
        self.conn.commit()
        print(f"Employee {name} added successfully with ID: {emp_id}")

    def display_employees(self):
        self.cur.execute("SELECT * FROM employee")
        rows = self.cur.fetchall()
        if not rows:
            print("No employees to display.")
        else:
            print("\nEmployee List:")
            for row in rows:
                emp_id, name, position, salary, emp_joining_date, emp_dob, emp_mobile = row
                print(f"Employee ID: {emp_id}\nName: {name}\nPosition: {position}\nSalary: {salary}\nJoining Date: {emp_joining_date}\nDOB: {emp_dob}\nMobile: {emp_mobile}\n")

    def show_employee_by_id(self, emp_id):
        self.cur.execute("SELECT * FROM employee WHERE emp_id = ?", (emp_id,))
        row = self.cur.fetchone()
        if row:
            emp_id, name, position, salary, emp_joining_date, emp_dob, emp_mobile = row
            print("\nEmployee Details:")
            print(f"Employee ID: {emp_id}\nName: {name}\nPosition: {position}\nSalary: {salary}\nJoining Date: {emp_joining_date}\nDOB: {emp_dob}\nMobile: {emp_mobile}\n")
        else:
            print(f"No employee found with ID {emp_id}.")

    def delete_employee(self, emp_id):
        self.cur.execute("DELETE FROM employee WHERE emp_id = ?", (emp_id,))
        if self.cur.rowcount > 0:
            print(f"Employee with ID {emp_id} deleted successfully.")
            self.conn.commit()
        else:
            print(f"No employee found with ID {emp_id}. Deletion unsuccessful.")

def main():
    emp_system = EmployeeManagementSystem()

    while True:
        print("\nEmployee Management System")
        print("1. Add Employee")
        print("2. Display Employees")
        print("3. Show Employee by ID")
        print("4. Delete Employee")
        print("5. Quit")

        choice = input("Enter your choice (1/2/3/4/5): ")

        if choice == "1":
            try:
                name = input("Enter Employee Name: ")
                position = input("Enter Employee Position: ")
                salary = float(input("Enter Employee Salary: "))
                emp_joining_date = input("Enter Employee Joining Date (YYYY-MM-DD): ")
                emp_dob = input("Enter Employee Date of Birth (YYYY-MM-DD): ")
                emp_mobile = input("Enter Employee Mobile Number: ")
                emp_system.add_employee(name, position, salary, emp_joining_date, emp_dob, emp_mobile)

            except ValueError:
                print("Invalid input. Please enter a valid salary.")

        elif choice == "2":
            emp_system.display_employees()

        elif choice == "3":
            emp_id_to_show = input("Enter the Employee ID to show: ")
            emp_system.show_employee_by_id(emp_id_to_show)

        elif choice == "4":
            emp_id_to_delete = input("Enter the Employee ID to delete: ")
            emp_system.delete_employee(emp_id_to_delete)

        elif choice == "5":
            print("Exiting the Employee Management System. Goodbye!")
            emp_system.conn.close()
            break

        else:
            print("Invalid choice. Please enter a valid option.")

if __name__ == "__main__":
    main()
