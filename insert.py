import pymysql
from faker import Faker
import random
from db import get_connection

#blacklist
def insert_new_blacklist(id, name, status):
    connection = get_connection()
    try:
        cursor = connection.cursor()

        insert_sql = "INSERT INTO blacklist (id_card, name, status) VALUES (%s, %s, %s)"
        data = (id, name, status)
        cursor.execute(insert_sql, data)
        connection.commit()

        cursor.execute("SELECT * FROM blacklist")
        results = cursor.fetchall()

        for row in results:
            print(f"id_card: {row[0]}, name: {row[1]}, status: {row[2]}")
    finally:
        cursor.close()
        connection.close()

def generate_random_blacklist_user():
    fake = Faker('th_TH')
    id_card = ''.join([str(random.randint(0, 9)) for _ in range(13)])
    name = fake.name()
    status = random.choice(["blacklisted", "cleared", "under_review"])
    return id_card, name, status


#insert new user for bank
def insert_new_bank_user(bank_name, id_card, bank_num, name, balance):
    connection = get_connection()
    try:
        with connection.cursor() as cursor:
            insert_sql = f"""
            INSERT INTO {bank_name} (id_card, bank_num, name, balance)
            VALUES (%s, %s, %s, %s)
            """
            data = (id_card, bank_num, name, balance)
            cursor.execute(insert_sql, data)
            connection.commit()

            cursor.execute(f"SELECT * FROM {bank_name}")
            results = cursor.fetchall()

            for row in results:
                print(f"id_card: {row[0]}, bank_num: {row[1]}, name: {row[2]}, balance: {row[3]}")
    finally:
        connection.close()
        
def generate_random_bank_user():
    fake = Faker('en_US')
    id_card = ''.join([str(random.randint(0, 9)) for _ in range(13)])
    bank_num = ''.join([str(random.randint(0, 9)) for _ in range(13)])
    name = fake.name()
    balance = 10000
    return id_card, bank_num, name, balance



for _ in range(0):
    id_card, name, status = generate_random_blacklist_user()
    insert_new_blacklist(id_card, name, status)   
# data = ("0000000000001", "Sommai jaidee ", "blacklisted")
# insert_new_blacklist(data[0],data[1],data[2])

for _ in range(1):
    bank_name = "scb"
    id_card, bank_num, name, balance = generate_random_bank_user()
    insert_new_bank_user(bank_name,id_card, bank_num, name, balance)  