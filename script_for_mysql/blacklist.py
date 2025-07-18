import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
import requests
import pymysql
import hashlib
import time
import random
import datetime

from utils import insert_new_blacklist, split_name

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

def generate_hash_from_name(name):
    return hashlib.sha256(name.encode('utf-8')).hexdigest()

def generate_fake_id(name):
    hash_val = hashlib.sha256(name.encode('utf-8')).hexdigest()
    numeric_part = ''.join(filter(str.isdigit, hash_val))
    return numeric_part[:13].ljust(13, '0')  # เติม 0 ถ้าไม่ครบ

def generate_fake_id_v2(name):
    hash_val = hashlib.sha256(name.encode('utf-8')).hexdigest()
    numeric_part = ''.join(filter(str.isdigit, hash_val))
    
    id_raw = numeric_part[:12].ljust(12, '0')
    checksum = str(sum(int(digit) * (13 - i) for i, digit in enumerate(id_raw)) % 10)  # mock checksum
    return id_raw + checksum

def generate_unique_id(name):
    base_hash = hashlib.sha256(name.encode('utf-8')).hexdigest()
    numeric_part = ''.join(filter(str.isdigit, base_hash))
    id_candidate = numeric_part[:13].ljust(13, '0')

    # ตรวจสอบว่าซ้ำไหม
    retries = 0
    while id_card_exists(id_candidate):
        # ผสมเวลาและสุ่มเลขเข้าไปเพื่อไม่ให้ซ้ำ
        timestamp = datetime.datetime.utcnow().strftime("%f")  # microseconds
        random_digits = str(random.randint(100, 999))
        mixed = name + timestamp + random_digits
        new_hash = hashlib.sha256(mixed.encode('utf-8')).hexdigest()
        numeric_part = ''.join(filter(str.isdigit, new_hash))
        id_candidate = numeric_part[:13].ljust(13, '0')
        retries += 1
        if retries > 10:
            raise Exception("Failed to generate unique 13-digit ID after multiple attempts")
    
    return id_candidate

def sync_blacklist():
    print("start sync")
    try:
        response = requests.get(API_URL)
        response.raise_for_status()
        cases = response.json()
        
        print(f"Fetched {len(cases)} cases")

        for case in cases:
            tranfers = case.get("tranfers", [])
            for tf in tranfers:
                if tf.get("owner") == "ผู้ร้าย":
                    account_name = tf.get("accountName", "")
                    access_number = tf.get("accessNumber", "")
                    
                    # ใช้ชื่อแทน access number เพื่อ hash
                    hash_id = generate_unique_id(access_number)

                    first_name, last_name = split_name(account_name)
                    status = "warning"

                    if not id_card_exists(hash_id):
                        insert_new_blacklist(hash_id, first_name, last_name, status)
                        print(f"Inserted blacklist (from criminal): {hash_id} {first_name} {last_name}")
                    else:
                        print(f"Skipped (duplicate): {hash_id}")

    except Exception as e:
        print("Error while syncing:", e)

if __name__ == "__main__":
    # sync_blacklist()

    while True:
        sync_blacklist()
        # break
        time.sleep(1)
