
import streamlit as st
import sqlite3

class EmployeeManagementSystem:
    def __init__(self):
        self.conn = sqlite3.connect("aapka.db")
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

    def add_employee(self, name, position, emp_mobile, emp_dob, emp_joining_date, salary):
        emp_id = self.generate_employee_id(name, position, emp_dob)
        ins = '''
            INSERT INTO employee (emp_id, emp_name, emp_position, emp_mobile, emp_dob, emp_joining_date, emp_salary) VALUES 
            (?, ?, ?, ?, ?, ?, ?)
        '''
        self.cur.execute(ins, (emp_id, name, position, emp_mobile, emp_dob, emp_joining_date, salary))
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
                emp_id, name, position, emp_mobile, emp_dob, emp_joining_date, salary = row
                print(f"Employee ID: {emp_id}\nName: {name}\nPosition: {position} \nMobile: {emp_mobile}\nDOB: {emp_dob}\nJoining Date: {emp_joining_date} \nSalary: {salary}\n")

    def show_employee_by_id(self, emp_id):
        self.cur.execute("SELECT * FROM employee WHERE emp_id = ?", (emp_id,))
        row = self.cur.fetchone()
        if row:
            emp_id, name, position, emp_mobile, emp_dob, emp_joining_date, salary = row
            print("\nEmployee Details:")
            print(f"Employee ID: {emp_id}\nName: {name}\nPosition: {position}\nMobile: {emp_mobile}\nDOB: {emp_dob}\nJoining Date: {emp_joining_date} \nSalary: {salary}\n")
        else:
            print(f"No employee found with ID {emp_id}.")

    def edit_employee(self, emp_id, new_name, new_position,new_mobile, new_dob,new_joining_date,new_salary):
        update_query = '''
            UPDATE employee
            SET emp_name=?, emp_position=?, emp_salary=?, emp_joining_date=?, emp_dob=?, emp_mobile=?
            WHERE emp_id=?
        '''
        self.cur.execute(update_query, (new_name, new_position, new_mobile, new_dob, new_joining_date,emp_id,new_salary))
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

        if choice == "1":
            try:
                name = input("Enter Employee Name: ")
                position = input("Enter Employee Position: ")
                emp_mobile = input("Enter Employee Mobile Number: ")
                emp_dob = input("Enter Employee Date of Birth (YYYY-MM-DD): ")
                emp_joining_date = input("Enter Employee Joining Date (YYYY-MM-DD): ")
                salary = (input("Enter Employee Salary: "))

                emp_system.add_employee(name, position, emp_mobile, emp_dob, emp_joining_date, salary)

            except ValueError:
                print("Invalid input. Please enter a valid salary.")
 
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
                new_salary = (input("Enter the new Employee Salary: "))

                emp_system.edit_employee(emp_id_to_edit, new_name, new_position,new_mobile ,new_dob, new_joining_date ,new_salary)

            except ValueError:
                print("Invalid input. Please enter a valid salary.")
                
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


        #//////////////////////




        ##///////////////

# from tkinter import *
# import tkinter.messagebox

# def validate():
#     name= entry_1.get()
#     email= entry_2.get()
#     country= c.get()
#     programming= var2.get()
#     gender= var.get()
#     if (name=="" or email=="" or country== 'Select your country'or programming == 0 or gender == 0):
#         tkinter.messagebox.showinfo('Invalid Message Alert',"Fields cannot be left empty!")

#     else:
#         tkinter.messagebox.showinfo('Success Message',"Successfully registered!")
        

   
# root = Tk()
# root.geometry('500x500')
# root.title("Registration Form")


# label_0 = Label(root, text="Registration form",width=20,font=("bold", 20))
# label_0.place(x=90,y=53)

# label_1 = Label(root, text="Full Name",width=20,font=("bold", 10))
# label_1.place(x=80,y=130)

# entry_1 = Entry(root)
# entry_1.place(x=240,y=130)

# label_2 = Label(root, text="Email",width=20,font=("bold", 10))
# label_2.place(x=68,y=180)

# entry_2 = Entry(root)
# entry_2.place(x=240,y=180)

# label_3 = Label(root, text="Gender",width=20,font=("bold", 10))
# label_3.place(x=70,y=230)
# var = IntVar()
# Radiobutton(root, text="Male",padx = 5, variable=var, value=1).place(x=235,y=230)
# Radiobutton(root, text="Female",padx = 20, variable=var, value=2).place(x=290,y=230)

# label_4 = Label(root, text="Country",width=20,font=("bold", 10))
# label_4.place(x=70,y=280)

# list1 = ['Canada','India','UK','Nepal','Iceland','South Africa']
# c=StringVar()
# droplist=OptionMenu(root,c, *list1)
# droplist.config(width=15)
# c.set('Select your country') 
# droplist.place(x=240,y=280)

# label_4 = Label(root, text="Programming",width=20,font=("bold", 10))
# label_4.place(x=85,y=330)
# var1 = IntVar()
# Checkbutton(root, text="C++", variable=var1).place(x=235,y=330)
# var2 = IntVar()
# Checkbutton(root, text="Python", variable=var2).place(x=290,y=330)

# Button(root, text='Submit',width=20,bg='green',fg='white', command = validate).place(x=180,y=380)

# root.mainloop()


#//////////

