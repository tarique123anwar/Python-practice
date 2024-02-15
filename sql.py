import sqlite3
c=sqlite3.connect("sql.db")
c.execute('''
Create table student (
           st_id INT AUTO_INCREMENT PRIMARY KEY,
           st_name VARCHAR(80),
           st_class VARCHAR(20),
           st_email VARCHAR(40)
        )
    ''')
c.close()

#///////////////////////////
import sqlite3
d=sqlite3.connect("ee.db")
d.execute('''


''') 