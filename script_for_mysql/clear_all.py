import pymysql
from db import get_connection


def delete_all_blacklist_users():
    connection = get_connection()
    try:
        with connection.cursor() as cursor:
            delete_sql = "DELETE FROM blacklist"
            cursor.execute(delete_sql)
            connection.commit()
            print("Delete all blacklist complete")
    finally:
        connection.close()


delete_all_blacklist_users()
