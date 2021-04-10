import mysql.connector
#host, database, user, password
conn = mysql.connector.connect(host='localhost',database='PythonAutomation', user='root', password='masterkey')
print(conn.is_connected())
cursor=conn.cursor()
cursor.execute('select * from customerInfo')
rows=cursor.fetchall()
print(type(rows))

sum=0
for row in rows:
    sum=sum+row[2]
print(sum)

query="update CustomerInfo Info set Location=%s where CourseName=%s"
data=("UK", "Jmeter")
cursor.execute(query,data)
conn.commit()


conn.close()