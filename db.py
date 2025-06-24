import pymysql

def get_connection():
    return pymysql.connect(
        host='localhost',
        user='root',
        password='1234',
        database='testdb',
        port=3306
    )
