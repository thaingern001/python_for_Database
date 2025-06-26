import pymysql
from db import get_connection
connection = get_connection()

try:
    with connection.cursor() as cursor:
        cursor.execute("SHOW TABLES;")
        tables = cursor.fetchall()
        print("Tables in the database:")
        for table in tables:
            print(table[0])
finally:
    connection.close()
