from pymongo import MongoClient

def get_collection():
    client = MongoClient("mongodb://localhost:27017/")
    db = client["mydatabase"]
    return db["cases"]

if __name__ == "__main__":
    collection = get_collection()
    result = collection.delete_many({})
    print(f"Deleted {result.deleted_count} documents.")
