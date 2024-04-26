import sqlite3
from datetime import datetime
class EmployeeManagementSystem:
    def __init__(self):
        self.conn = sqlite3.connect("Anwar.db")
        self.cur = self.conn.cursor()

    def generate_employee_id(self, name, position, dob):
        # Split the name into first name and last name
        first_name, last_name = name.split()
        
        # Extract the first letters of the first and last names
        first_name_initial = first_name[0].upper()
        last_name_initial = last_name[0].upper()
        
        # Extract the relevant parts of the date of birth
        dob_part = dob[5:7] + dob[8:10]
        
        # Extract the first letter of the position
        position_part = position[:1].upper()
        
        # Combine the initials and dob parts to generate the employee ID  
        return f"{first_name_initial}{last_name_initial}{dob_part}{position_part}"
            #////////////

    def add_employee(self, name, position, emp_mobile , emp_dob,emp_joining_date,salary):
        emp_id = self.generate_employee_id(name, position, emp_dob)
        ins = '''
            INSERT INTO employee (emp_id, emp_name, emp_position, emp_salary, emp_joining_date, emp_dob, emp_mobile) VALUES 
            (?, ?, ?, ?, ?, ?, ?)
        '''
        self.cur.execute(ins, (emp_id, name, position, salary, emp_joining_date, emp_dob, emp_mobile))
        self.conn.commit()
        print(f"Employee {name} added successfully with ID: {emp_id}")

    def display_employees(self):
        self.cur.execute("SELECT * FROM employee")  #//////////// cur is a cursor / .execute is the database execution 
        rows = self.cur.fetchall()
        if not rows:
            print("No employees to display.")
        else:
            print("\nEmployee List:")
            for row in rows:
                emp_id, emp_name, emp_position, salary, emp_joining_date, emp_dob, emp_mobile = row
                print(f"Employee ID: {emp_id}\nName: {emp_name}\nPosition: {emp_position}\nSalary: {salary}\nJoining Date: {emp_joining_date}\nDOB: {emp_dob}\nMobile: {emp_mobile}\n")

    def show_employee_by_id(self, emp_id):
        self.cur.execute("SELECT * FROM employee WHERE emp_id = ?", (emp_id,))
        row = self.cur.fetchone()
        if row:
            emp_id, emp_name, emp_position, salary, emp_joining_date, emp_dob, emp_mobile = row
            print("\nEmployee Details:")
            print(f"Employee ID: {emp_id}\nName: {emp_name}\nPosition: {emp_position}\nSalary: {salary}\nJoining Date: {emp_joining_date}\nDOB: {emp_dob}\nMobile: {emp_mobile}\n")
        else:
            print(f"No employee found with ID {emp_id}.")

    def edit_employee(self, emp_id, new_name, new_position, new_salary, new_joining_date, new_dob, new_mobile):
        update_query = '''
            UPDATE employee
            SET emp_name=?, emp_position=?, emp_salary=?, emp_joining_date=?, emp_dob=?, emp_mobile=?
            WHERE emp_id=?
        '''
        self.cur.execute(update_query, (new_name, new_position, new_salary, new_joining_date, new_dob, new_mobile, emp_id))
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
    emp_system = EmployeeManagementSystem()

    while True:
        print("\nEmployee Management System")
        print("1. Add Employee")
        print("2. Display All Employees")               
        print("3. Show Employee by ID")
        print("4. Edit Employee")
        print("5. Delete Employee")
        print("6. Quit")

        choice = input("Enter your choice (1/2/3/4/5/6): ")
        def get_employee_name():
            # validInteger = False
            # while not validInteger:
                input("enter the full_name:")
                # if name.isalpha():
                #     validInteger = True
                #     return name
                # else:
                #     print('Pl enter the valid name')

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
                salary = (input("Enter Employee Salary: "))
                if salary.isdigit():
                    validInput = True
                return salary
                # else:
                #     print("Error: Please enter a valid value.")

        if choice == "1":
            # try:
                # if choice == "1":
                    # name = get_employee_name()
                    emp_name = get_employee_name()
                    emp_position = get_employee_position()
                    emp_mobile = get_employee_mobile()
                    emp_dob = get_employee_dob()
                    emp_joining_date = get_employee_joining_date()
                    salary = get_employee_salary()

                    print("values", emp_name, emp_position, emp_mobile, emp_dob, emp_joining_date, salary)

                    emp_system.add_employee(emp_name, emp_position, emp_mobile , emp_dob , emp_joining_date , salary)

            # except ValueError:
            #     print("Invalid input. Please enter a valid values.")
 
        elif choice == "2":
            emp_system.display_employees()

        elif choice == "3":
            emp_id_to_show = input("Enter the Employee ID to show: ")
            emp_system.show_employee_by_id(emp_id_to_show)

        elif choice == "4":
            try:
                emp_id_to_edit = input("Enter the Employee ID to edit: ")
                new_name = input("Enter the new Employee Name: ")
                new_position = input("Enter the new Employee Position: ")
                new_mobile = input("Enter the new Employee Mobile Number: ")
                new_dob = input("Enter the new Employee Date of Birth (YYYY-MM-DD): ") 
                new_joining_date = input("Enter the new Employee Joining Date (YYYY-MM-DD): ")
                new_salary = float(input("Enter the new Employee Salary: "))

                emp_system.edit_employee(emp_id_to_edit, new_name, new_position,new_mobile, new_dob,new_joining_date,new_salary)

            except ValueError:
                print("Invalid input. Please enter a valid values.")
                
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
