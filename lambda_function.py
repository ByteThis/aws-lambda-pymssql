import sys
import pymssql

rds_host  = "host"

def lambda_handler(*args, **kwargs):

    database = 'db'
    username = 'user'
    password = 'password'

    try:
        conn = pymssql.connect(rds_host, username, password, "dbname")
    except:
        print("ERROR: Could not connect to MSSQL instance.")
        sys.exit()

    print("SUCCESS: Connection to MSSQL instance succeeded")

    cursor = conn.cursor()
    cursor.execute('SELECT * FROM test')
    row = cursor.fetchone()

    while row:
        print("ID=%d, Name=%s" % (row[0], row[1]))
        row = cursor.fetchone()

    conn.close()

lambda_handler()