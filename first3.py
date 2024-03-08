import sqlite3
conn=sqlite3.connect("pro.db")
conn.execute('''
         Create table employee (
             emp_id INT AUTO_INCREMENT PRIMARY KEY,
             emp_name VARCHAR(50),
             emp_position VARCHAR(50),
             emp_salary VARCHAR(20),
             emp_date VARCHAR(10)
            )

        ''')
conn.close()