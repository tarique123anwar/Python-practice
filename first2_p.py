# import sqlite3
# conn=sqlite3.connect("read.db")
# inss='''
#         insert into employee (emp_name , emp_position , emp_salary , emp_date) VALUES 
#                     ('Ashraf','anno','20000','23')
                    
#     '''
# inss='''
#         insert into employee (emp_name , emp_position , emp_salary , emp_date) VALUES 
#                     ('Ali','anno','15000','22')
                    
#     '''
# conn.execute(inss)
# conn.commit()
# conn.close()


import sqlite3

conn = sqlite3.connect("read.db")

# Get user input
name = input("Enter Employee Name: ")
position = input("Enter Employee Position: ")
salary = input("Enter Employee Salary: ")
date = input("Enter Join Date: ")

# Insert user input into the employee table
ins = f'''
    INSERT INTO employee (emp_name, emp_position, emp_salary, emp_date) VALUES 
    ('{name}', '{position}', '{salary}', '{date}')
'''

conn.execute(ins)
conn.commit()
conn.close()
