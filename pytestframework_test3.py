from utilities.configuration_pyodbc import *
import pytest

@pytest.fixture(scope='module') # setup once for all tests
def cur():
    print('----------setup----------')
    conn = getConnection()
    curs = conn.cursor()
    yield curs
    print('----------closing database----------')
    curs.close()
    conn.close()


def test_db(cur):
    cur.execute('select * from Books')
    rows = cur.fetchall()
    assert len(rows) ==3
    for row in rows:
        print(row)




