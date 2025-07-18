import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
import requests
import pymysql
# from db import get_connection
from utils import insert_new_blacklist, split_name
import time

API_URL = "http://127.0.0.1:8001/cases/latest"


def get_connection():
    return pymysql.connect(
        host='localhost',
        user='root',
        password='1234',
        database='testdb',
        port=3306
    )

def id_card_exists(id_card):
    connection = get_connection()
    try:
        cursor = connection.cursor()
        cursor.execute("SELECT COUNT(*) FROM blacklist WHERE id_card = %s", (id_card,))
        result = cursor.fetchone()
        return result[0] > 0
    finally:
        cursor.close()
        connection.close()

def sync_blacklist():
    print("start sync")
    try:
        response = requests.get(API_URL)
        response.raise_for_status()
        cases = response.json()
        
        print(f"Fetched {len(cases)} cases")

        for case in cases:
            # ตัวอย่างดึงจาก user field
            user = case.get("user", {})
            id_card = user.get("idCard")
            full_name = f"{user.get('firstName', '')} {user.get('lastName', '')}"
            first_name, last_name = split_name(full_name)

            if id_card and not id_card_exists(id_card):
                status = case.get("status", "under_review")
                insert_new_blacklist(id_card, first_name, last_name, status)
                print(f"Inserted new blacklist: {id_card} {first_name} {last_name}")
            else:
                print(f"Skipped (duplicate or missing id): {id_card}")

    except Exception as e:
        print("Error while syncing:", e)

if __name__ == "__main__":
    sync_blacklist()

    while True:
        sync_blacklist()
        time.sleep(10)
