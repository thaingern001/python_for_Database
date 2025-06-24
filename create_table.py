import pymysql
from db import get_connection

connection = get_connection()


def create_blacklist_table():
    try:
        with connection.cursor() as cursor:
            create_table_sql = """
            CREATE TABLE IF NOT EXISTS blacklist (
                id_card VARCHAR(13) PRIMARY KEY,
                name VARCHAR(100) NOT NULL,
                status VARCHAR(20) NOT NULL
            );
            """
            cursor.execute(create_table_sql)
            connection.commit()
            print("Table 'blacklist' created successfully.")
    finally:
        connection.close()



def create_bank_table(bank_name):
    connection = get_connection()
    try:
        with connection.cursor() as cursor:
            create_table_sql = f"""
            CREATE TABLE IF NOT EXISTS {bank_name} (
                id_card VARCHAR(13) PRIMARY KEY,
                bank_num VARCHAR(13) NOT NULL,
                name VARCHAR(100) NOT NULL,
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