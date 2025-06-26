import pymysql
from db import get_connection

connection = get_connection()


def create_blacklist_table():
    try:
        with connection.cursor() as cursor:
            # สร้างตารางใหม่แยก first_name และ last_name
            create_table_sql = """
            CREATE TABLE blacklist (
                id_card VARCHAR(13) PRIMARY KEY,
                first_name VARCHAR(50) NOT NULL,
                last_name VARCHAR(50) NOT NULL,
                status VARCHAR(20) NOT NULL
            );
            """
            cursor.execute(create_table_sql)
            connection.commit()
            print("Table 'blacklist' created successfully.")
    finally:
        connection.close()

# create_blacklist_table()



        
def create_bank_table(bank_name):
    connection = get_connection()
    try:
        with connection.cursor() as cursor:
            # cursor.execute(f"DROP TABLE IF EXISTS {bank_name};")
            create_table_sql = f"""
            CREATE TABLE {bank_name} (
                id_card VARCHAR(13) PRIMARY KEY,
                bank_num VARCHAR(13) NOT NULL,
                first_name VARCHAR(50) NOT NULL,
                last_name VARCHAR(50) NOT NULL,
                balance INT NOT NULL
            );
            """
            cursor.execute(create_table_sql)
            connection.commit()
            print(f"Table '{bank_name}' created successfully.")
    finally:
        connection.close()


#ทำไปละ
bank_names = [
    "scb",       # ธนาคารไทยพาณิชย์ (Siam Commercial Bank)
    "kbank",     # ธนาคารกสิกรไทย (Kasikornbank)
    "ktb",       # ธนาคารกรุงไทย (Krungthai Bank)
    "bbl",       # ธนาคารกรุงเทพ (Bangkok Bank)
    "bay",       # ธนาคารกรุงศรีอยุธยา (Bank of Ayudhya)
    "gsb",       # ธนาคารออมสิน (Government Savings Bank)
]



# for bank_name in bank_names:
#     print(bank_name)
#     create_bank_table(bank_name)

# create_bank_table("thaingern")