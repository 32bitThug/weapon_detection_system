import sqlite3
conn =sqlite3.connect('wds_db')
c=conn.cursor()
c.execute(" " " create table uid (username text ,email text ,password text)""")

conn.commit()
conn.close()
