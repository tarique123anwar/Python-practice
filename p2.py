import random
import string
import sqlite3

class EmployeeManagementSystem:
    def __init__(self):
        self.employees = []

    def generate_employee_id(self):
        allowed_chars = string.digits
        return ''.join(random.choice(allowed_chars) for _ in range(6))

    def add_employee(self, name, position, salary, emp_joining_date):
        emp_id = self.generate_employee_id()
        employee = {"emp_id": emp_id, "name": name, "position": position, "salary": salary, "emp_joining_date": emp_joining_date}
        self.employees.append(employee)
        print(f"Employee {name} added successfully with ID: {emp_id}")

    def display_employees(self):
        if not self.employees:
            print("No employees to display.")
        else:
            print("\nEmployee List:")
            for employee in self.employees:
                print(f"Employee ID: {employee['emp_id']}, Name: {employee['name']}, Position: {employee['position']}, Salary: {employee['salary']}, emp_joining_date: {employee['emp_joining_date']}")

def main():
    emp_system = EmployeeManagementSystem()
    conn = sqlite3.connect("AAJ.db")

    # Create the employee table if it doesn't exist
    conn.execute('''
        CREATE TABLE IF NOT EXISTS employee (
            emp_id TEXT,
            emp_name TEXT,
            emp_position TEXT,
            emp_salary REAL,
            emp_date INTEGER
        )
    ''')

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
                emp_joining_date = input("Enter Employee gjoining_date: ")
                emp_system.add_employee(name, position, salary, emp_joining_date)

                # Insert data into the database
                ins = f'''
                    INSERT INTO employee (emp_id, emp_name, emp_position, emp_salary, emp_date) VALUES 
                    ('{emp_system.employees[-1]["emp_id"]}', '{name}', '{position}', '{salary}', '{emp_joining_date}')
                '''
                conn.execute(ins)
                conn.commit()

            except ValueError:
                print("Invalid input. Please enter a valid salary.")

        elif choice == "2":
            emp_system.display_employees()

        elif choice == "3":
            print("Exiting the Employee Management System. Goodbye!")
            conn.close()
            break

        else:
            print("Invalid choice. Please enter a valid option.")

if __name__ == "__main__":
    main()



        #////////////////////////
# import string
# import sqlite3

# class EmployeeManagementSystem:
#     def __init__(self):
#         self.employees = []

#     def generate_employee_id(self, position, doj):
#         allowed_chars = string.digits
#         position_first_letter = position[0].upper()
#         day_number = str(doj.day).zfill(2)
#         month_number = str(doj.month).zfill(2)
#         random_number = ''.join(random.choice(allowed_chars) for _ in range(3))
#         return f'{day_number}{month_number}{position_first_letter}{random_number}'

#     def add_employee(self, name, position, salary, dob, doj):
#         emp_id = self.generate_employee_id(position, doj)
#         employee = {"emp_id": emp_id, "name": name, "position": position, "salary": salary, "dob": dob, "doj": doj}
#         self.employees.append(employee)
#         print(f"Employee {name} added successfully with ID: {emp_id}")

#     def display_employees(self):
#         if not self.employees:
#             print("No employees to display.")
#         else:
#             print("\nEmployee List:")
#             for employee in self.employees:
#                 print(f"Employee ID: {employee['emp_id']}, Name: {employee['name']}, Position: {employee['position']}, Salary: {employee['salary']}, DOB: {employee['dob']}, DOJ: {employee['doj']}")

# def main():
#     emp_system = EmployeeManagementSystem()
#     conn = sqlite3.connect("rrr.db")

#     # Create the employee table if it doesn't exist
#     conn.execute('''
#         CREATE TABLE IF NOT EXISTS employee (
#             emp_id TEXT,
#             emp_name TEXT,
#             emp_position TEXT,
#             emp_salary REAL,
#             emp_dob TEXT,
#             emp_doj TEXT
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
#                 dob = input("Enter Date of Birth (YYYY-MM-DD): ")
#                 doj = input("Enter Date of Joining (YYYY-MM-DD): ")
#                 emp_system.add_employee(name, position, salary, dob, doj)

#                 # Insert data into the database
#                 ins = f'''
#                     INSERT INTO employee (emp_id, emp_name, emp_position, emp_salary, emp_dob, emp_doj) VALUES 
#                     ('{emp_system.employees[-1]["emp_id"]}', '{name}', '{position}', '{salary}', '{dob}', '{doj}')
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