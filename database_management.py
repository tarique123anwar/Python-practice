import sqlite3
conn=sqlite3.connect("manage.db")
conn.execute('''
         Create table employee (
             emp_id VARCHAR(10),
             emp_name VARCHAR(50),
             emp_position VARCHAR(50),
             emp_mobile VARCHAR(10),
             emp_dob VARCHAR(50),
             emp_joining_date VARCHAR(10),
             emp_salary VARCHAR(20)
            )

        ''')
conn.close()