import pyodbc
import pytest
from utilities.configuration_pyodbc import *
def test_db():
    conn = getConnection()
    cursor = conn.cursor()
    cursor.execute('select * from Books')
    rows = cursor.fetchall()
    assert len(rows) ==3
    for row in rows:
        print(row)

    conn.close()
def test_2():
    print("Hello World!")

def test_add():
    print("Hello The World!")



