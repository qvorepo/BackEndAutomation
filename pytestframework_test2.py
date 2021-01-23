from utilities.configuration_pyodbc import *
conn=None
cursor = None
def setup_module(module):
    global conn
    global cursor
    print('----------setup----------')
    conn = getConnection()

def teardown_module(module):
    print('----------teardown----------')
    conn.close()

def test_db():
    conn = getConnection()
    cursor = conn.cursor()
    cursor.execute('select * from Books')
    rows = cursor.fetchall()
    assert len(rows) ==3
    for row in rows:
        print(row)




