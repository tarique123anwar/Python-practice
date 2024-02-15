import sqlite3
c=sqlite3.connect("sqlite.db")
ins='''
insert into student(st_name,st_class,st_email) VALUES ('Md','B.tech','md@gmail.com')
'''
c.execute(ins)
c.commit()
c.close()
