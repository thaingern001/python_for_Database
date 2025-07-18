# utils.py

from db import get_connection

def split_name(full_name):
    parts = full_name.strip().split()
    first_name = parts[0] if parts else ''
    last_name = ' '.join(parts[1:]) if len(parts) > 1 else ''
    return first_name, last_name

def insert_new_blacklist(id_card, first_name, last_name, status):
    connection = get_connection()
    try:
        with connection.cursor() as cursor:
            sql = "INSERT INTO blacklist (id_card, first_name, last_name, status) VALUES (%s, %s, %s, %s)"
            cursor.execute(sql, (id_card, first_name, last_name, status))
        connection.commit()
    finally:
        connection.close()

