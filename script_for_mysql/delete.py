import pymysql
from db import get_connection

def delete_blacklist_user(id_card):
    connection = get_connection()
    try:
        with connection.cursor() as cursor:
            delete_sql = "DELETE FROM blacklist WHERE id_card = %s"
            cursor.execute(delete_sql, (id_card,))
            connection.commit()
            print(f"ลบข้อมูลของ id_card: {id_card} สำเร็จแล้ว")
    finally:
        connection.close()
        

id_card_delete = ""
delete_blacklist_user(id_card_delete)
