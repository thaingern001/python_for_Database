from fastapi import FastAPI, Query
from typing import Optional
from pymongo import MongoClient
from bson.json_util import dumps
from datetime import datetime
import json
import os

client = MongoClient("mongodb://localhost:27017/")
db = client["mydatabase"]
collection = db["cases"]

app = FastAPI()

LAST_SYNC_FILE = "last_sync.json"

# อ่านเวลาจากไฟล์
def read_last_sync_time(path=LAST_SYNC_FILE):
    if not os.path.exists(path):
        return None
    try:
        with open(path, "r") as f:
            data = json.load(f)
            return data["last_updated"]
    except:
        return None

# เขียนเวลาใหม่ลงไฟล์
def save_last_sync_time(timestamp: datetime, path=LAST_SYNC_FILE):
    with open(path, "w") as f:
        json.dump({"last_updated": timestamp.isoformat() + "Z"}, f)

@app.get("/")
def read_root():
    return {"message": "✅ FastAPI MongoDB running"}

# ดึงข้อมูลใหม่จาก updatedAt และอัปเดตเวลาในไฟล์
@app.get("/cases/latest")
def get_latest_cases():
    try:
        last_time_str = read_last_sync_time()
        if last_time_str:
            since_dt = datetime.fromisoformat(last_time_str.replace("Z", "+00:00"))
            query = {"updatedAt": {"$gt": since_dt}}
        else:
            query = {}

        # ดึงและเรียงจากเวลาน้อย → มาก
        docs = list(collection.find(query).sort("updatedAt", 1))

        # ถ้ามีข้อมูลใหม่ ให้เก็บ updatedAt ล่าสุดไว้
        if docs:
            latest_time = docs[-1]["updatedAt"]
            if isinstance(latest_time, datetime):
                save_last_sync_time(latest_time)

        return json.loads(dumps(docs))

    except Exception as e:
        return {"error": str(e)}
