import pymysql
from faker import Faker
import random
from db import get_connection

def split_name(full_name):
    parts = full_name.strip().split()
    if len(parts) == 0:
        return "", ""
    elif len(parts) == 1:
        return parts[0], ""
    else:
        return parts[0], " ".join(parts[1:])  # first word = first_name, rest = last_name

# blacklist
def insert_new_blacklist(id_card, first_name, last_name, status):
    connection = get_connection()
    try:
        cursor = connection.cursor()
        insert_sql = "INSERT INTO blacklist (id_card, first_name, last_name, status) VALUES (%s, %s, %s, %s)"
        data = (id_card, first_name, last_name, status)
        cursor.execute(insert_sql, data)
        connection.commit()

        cursor.execute("SELECT * FROM blacklist")
        results = cursor.fetchall()
        for row in results:
            print(f"id_card: {row[0]}, first_name: {row[1]}, last_name: {row[2]}, status: {row[3]}")
    finally:
        cursor.close()
        connection.close()

def generate_random_blacklist_user():
    fake = Faker('en_US')
    id_card = ''.join([str(random.randint(0, 9)) for _ in range(13)])
    full_name = fake.name()
    first_name, last_name = split_name(full_name)
    status = random.choice(["blacklisted", "cleared", "under_review"])
    return id_card, first_name, last_name, status

# bank user
def insert_new_bank_user(bank_name, id_card, bank_num, first_name, last_name, balance):
    connection = get_connection()
    try:
        with connection.cursor() as cursor:
            insert_sql = f"""
            INSERT INTO {bank_name} (id_card, bank_num, first_name, last_name, balance)
            VALUES (%s, %s, %s, %s, %s)
            """
            data = (id_card, bank_num, first_name, last_name, balance)
            cursor.execute(insert_sql, data)
            connection.commit()

            cursor.execute(f"SELECT * FROM {bank_name}")
            results = cursor.fetchall()
            for row in results:
                print(f"id_card: {row[0]}, bank_num: {row[1]}, first_name: {row[2]}, last_name: {row[3]}, balance: {row[4]}")
    finally:
        connection.close()

def generate_random_bank_user():
    fake = Faker('en_US')
    id_card = ''.join([str(random.randint(0, 9)) for _ in range(13)])
    bank_num = ''.join([str(random.randint(0, 9)) for _ in range(13)])
    full_name = fake.name()
    first_name, last_name = split_name(full_name)
    balance = 10000
    return id_card, bank_num, first_name, last_name, balance


# # Example usage
# for _ in range(1):
#     id_card, first_name, last_name, status = generate_random_blacklist_user()
#     insert_new_blacklist(id_card, first_name, last_name, status)

for _ in range(1):
    bank_name = "kbank"
    id_card, bank_num, first_name, last_name, balance = generate_random_bank_user()
    insert_new_bank_user(bank_name, id_card, bank_num, first_name, last_name, balance)
