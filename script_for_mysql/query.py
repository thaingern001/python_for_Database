from db import get_connection

def get_all_blacklist():
    conn = get_connection()
    try:
        with conn.cursor() as cursor:
            cursor.execute("SELECT * FROM blacklist")
            results = cursor.fetchall()
            return results
    finally:
        conn.close()

# ตัวอย่างการใช้งาน
if __name__ == "__main__":
    for row in get_all_blacklist():
        print(f"ID: {row[0]}, Fname: {row[1]} Lname: {row[2]}, Status: {row[3]}")
    # print(get_all_blacklist())
