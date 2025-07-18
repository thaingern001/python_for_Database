from pymongo import MongoClient
from datetime import datetime


def get_collection():
    client = MongoClient("mongodb://localhost:27017/")
    db = client["mydatabase"]
    return db["cases"]

def show_full():
    collection = get_collection()
    for doc in collection.find():
        print(doc)

def show_minimal():
    collection = get_collection()
    for doc in collection.find():
        user = doc.get("user", {})
        full_name = f"{user.get('prefix', '')} {user.get('firstName', '')} {user.get('lastName', '')}".strip()
        id_card = user.get("idCard", "N/A")
        created_at = doc.get("datetime", "N/A")
        status = doc.get("status", "N/A")
        print(f"Name: {full_name}, ID Card: {id_card}, Datetime: {created_at}, Status: {status}")

        
# def show_minimal():
#     collection = get_collection()
#     for doc in collection.find():
#         user = doc.get("user", {})
#         full_name = f"{user.get('prefix', '')} {user.get('firstName', '')} {user.get('lastName', '')}".strip()
#         id_card = user.get("idCard", "N/A")
#         created_at = doc.get("datetime")
#         updated_at = doc.get("updated_at")
#         status = doc.get("status", "N/A")

#         # แปลงวันที่ให้อ่านง่าย
#         def format_time(dt):
#             if isinstance(dt, datetime):
#                 return dt.strftime("%Y-%m-%d %H:%M")
#             return "N/A"

#         print(f"Name: {full_name}, ID Card: {id_card}, Created: {format_time(created_at)}, Updated: {format_time(updated_at)}, Status: {status}")

if __name__ == "__main__":
    print("=== Minimal Case Info ===")
    show_minimal()

    # print("\n=== Full Case Info ===")
    # show_full()

