from pymongo import MongoClient

# ใช้ localhost เนื่องจาก Docker เปิดพอร์ต 27017 ออกมานอกเครื่องแล้ว
client = MongoClient("mongodb://localhost:27017/")

# ถ้ามี username/password: (ใส่ใน URL เช่น mongodb://user:pass@localhost:27017/)
# ถ้าคุณรัน Mongo โดยไม่ตั้งรหัสผ่านไว้ ก็ไม่ต้องใส่

# ทดสอบดูว่าเชื่อมต่อได้ไหม
print(client.list_database_names())

# สร้าง/เลือก database และ collection
db = client["mydatabase"]
collection = db["mycollection"]

# แทรกข้อมูลตัวอย่าง
collection.insert_one({"name": "Thaingern", "age": 21})

# อ่านข้อมูลทั้งหมด
for doc in collection.find():
    print(doc)
