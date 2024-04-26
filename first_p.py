# import sqlite3
# conn=sqlite3.connect("aapka.db")
# conn.execute('''
#          Create table employee (
#              emp_id VARCHAR(10),
#              emp_name VARCHAR(50),
#              emp_position VARCHAR(50),
#              emp_mobile VARCHAR(10),
#              emp_dob VARCHAR(50),
#              emp_joining_date VARCHAR(10),
#              emp_salary VARCHAR(20)
#             )

#         ''')
# conn.close()
import sqlite3

conn = sqlite3.connect("data2.db")
conn.execute('''
         CREATE TABLE employee (
             emp_id VARCHAR(10),
             emp_name TEXT,
             emp_position TEXT,
             emp_mobile VARCHAR(15),
             emp_dob DATE,
             emp_joining_date DATE,
             emp_salary DECIMAL(10, 2)
            )
        ''')
conn.close()




# ins='''
#         insert into employee(emp_name,emp_position,emp_salary,emp_join_date) VALUES 
#                     ('anwar','ss','4222','22')
#     '''
# conn.execute(ins)
# conn.commit()
# conn.close()


# from flask import Flask, render_template
# from p3 import EmployeeManagementSystem  # Replace with the actual filename of your Python script

# app = Flask(__name__)
# emp_system = EmployeeManagementSystem()

# @app.route('/')
# def hello_world():
#     return render_template('index.html')

# @app.route('/products')
# def products():
#     return 'This is my product page'

# # Add more routes as needed for your Python program
# # For example, you can add routes for adding, displaying, editing, or deleting employees

# if __name__ == "__main__":
#     app.run(debug=True)