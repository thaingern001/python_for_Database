from pymongo import MongoClient

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
        full_name = f"{user.get('prefix', '')} {user.get('firstName', '')} {user.get('lastName', '')}"
        id_card = user.get("idCard", "N/A")
        status = doc.get("status", "N/A")
        print(f"Name: {full_name}, ID Card: {id_card}, Status: {status}")

if __name__ == "__main__":
    print("=== Minimal Case Info ===")
    show_minimal()

    # print("\n=== Full Case Info ===")
    # show_full()

