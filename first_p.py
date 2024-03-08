import sqlite3
conn=sqlite3.connect("aapka.db")
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
# ins='''
#         insert into employee(emp_name,emp_position,emp_salary,emp_join_date) VALUES 
#                     ('anwar','ss','4222','22')
#     '''
# conn.execute(ins)
# conn.commit()
# conn.close()
