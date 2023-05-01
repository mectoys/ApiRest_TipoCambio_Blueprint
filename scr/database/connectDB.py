import mysql.connector
# pip install mysql-connector-python
#freemysqlhosting
def get_connection():
    try:
        return mysql.connector.connect(
            host='sql10.freemysqlhosting.net',
            user='sql10595745',
            password='EwL2iKizxC',
            database='sql10595745'
        )
    except mysql.connector.Error as  err:
        raise err