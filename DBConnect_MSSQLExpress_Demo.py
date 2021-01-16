import pyodbc
from utilities.configuration_pyodbc import *

conn = getConnection()
cursor=conn.cursor()
cursor.execute('select * from Books')
rows=cursor.fetchall()
for row in rows:
    print(row)


conn.close()