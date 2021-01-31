from utilities.configuration_pyodbc import *
import pytest
import sys

@pytest.fixture(scope='module') # setup once for all tests
def cur():
    print('----------setup----------')
    conn = getConnection()
    curs = conn.cursor()
    yield curs
    print('----------closing database----------')
    curs.close()
    conn.close()

@pytest.mark.select
def test_db(cur):
    cur.execute('select * from Books')
    rows = cur.fetchall()
    assert len(rows) ==3
    for row in rows:
        print(row)

@pytest.mark.skipif(sys.version_info < (3,3), reason='Do not run the skipped decorator test')
def test_db(cur):
    cur.execute('select * from Books')
    rows = cur.fetchall()
    assert len(rows) ==3
    for row in rows:
        print(row)

@pytest.mark.select
def test_db(cur):
    cur.execute('select * from Books')
    rows = cur.fetchone()
    assert len(rows) ==1
    for row in rows:
        print(row)