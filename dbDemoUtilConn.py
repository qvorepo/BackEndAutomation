import mysql.connector
#host, database, user, password
from utilities.configurations import *

conn = getConnection()
print(conn.is_connected())
cursor=conn.cursor()
cursor.execute('select * from customerInfo')
row=cursor.fetchone()
print(row)
print(row[3])
rowAll=cursor.fetchall() #list of tuples [('Protractor', datetime.date(2020, 12, 19), 45, 'Africa'), ('Appium', datetime.date(2020, 12, 19), 99, 'Asia'), etc.
print(rowAll)

conn.close()