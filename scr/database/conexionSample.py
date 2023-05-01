import mysql.connector
#pip install mysql-connector-python
def get_connection():
    print("dfgdfg")
    try:
        return mysql.connector.connect(
            host='your_hostname',
            user='user_name',
            password='password',
            database='database'
        )
    except mysql.connector.Error as err:
        raise err
