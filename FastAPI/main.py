from fastapi import FastAPI, Query
from typing import Optional
from pymongo import MongoClient
from bson.json_util import dumps
from datetime import datetime

# เชื่อม MongoDB
client = MongoClient("mongodb://localhost:27017/")
db = client["mydatabase"]
collection = db["cases"]

app = FastAPI()

@app.get("/")
def read_root():
    return {"message": "FastAPI connected!"}

@app.get("/cases/latest")
def get_latest_cases(since: Optional[str] = Query(None, description="ISO8601 timestamp (e.g. 2025-06-25T10:00:00Z)")):
    try:
        if since:
            since_dt = datetime.fromisoformat(since.replace("Z", "+00:00"))
            query = {"updatedAt": {"$gt": since_dt}}
        else:
            query = {}

        docs = collection.find(query)

        # ใช้ bson.json_util.dumps เพื่อแปลง ObjectId และ datetime
        json_data = json.loads(dumps(docs))  # แปลงเป็น Python JSON พร้อมใช้งาน

        return json_data

    except Exception as e:
        import traceback
        traceback.print_exc()
        return {"error": str(e)}

