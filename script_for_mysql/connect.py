import pymysql

connection = pymysql.connect(
    host='localhost',      # หรือใช้ '127.0.0.1'
    user='root',           # หรือ user ที่คุณสร้าง
    password='1234',
    database='testdb',       # ชื่อ database ที่คุณกำหนดไว้
    port=3306              # พอร์ตที่เชื่อมต่อ (ต้องตรงกับ docker)
)

try:
    with connection.cursor() as cursor:
        cursor.execute("SELECT VERSION();")
        version = cursor.fetchone()
        print("Database version:", version[0])
finally:
    connection.close()
