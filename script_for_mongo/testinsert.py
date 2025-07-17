from pymongo import MongoClient
from bson.objectid import ObjectId
from datetime import datetime

client = MongoClient("mongodb://localhost:27017/")
db = client["mydatabase"]
collection = db["cases"]

document = {
    "_id": ObjectId("685d15d0672337145292b0dc"),
    "CrimeType": "Online Scam",
    "BankCaseID": "CASE123456",
    "user": {
        "prefix": "Mr",
        "firstName": "John",
        "lastName": "Doe",
        "idCard": "1234567890123",
        "email": "john@example.com",
        "phoneNumber": "0812345678",
        "phoneCarrier": "AIS",
        "birthDate": {
            "day": 1,
            "month": 1,
            "year": 1990
        },
        "idCardAddress": {
            "address": "123 Main St",
            "district": "Bangkok Noi",
            "subDistrict": "Arun Amarin",
            "province": "Bangkok",
            "postalCode": "10700"
        },
        "currentAddress": {
            "address": "456 Another St",
            "district": "Dusit",
            "subDistrict": "Dusit",
            "province": "Bangkok",
            "postalCode": "10300"
        }
    },
    "previousAgency": {
        "province": "Bangkok",
        "agencyName": "Central Police Station",
        "agencyType": "Police"
    },
    "avaliableAgency": {
        "province": "Bangkok",
        "agencyName": "Cyber Crime Division",
        "agencyType": "Cyber Police"
    },
    "crimeTitle": "Fraudulent Transfer",
    "crimeDescription": "Scammer tricked user to send money.",
    "tranfers": [
        {
            "_id": ObjectId("685d15d0672337145292b0dd"),
            "owner": "Jane Doe",
            "accountType": "Savings",
            "bankName": "Krungthai",
            "accessNumber": "123-456-7890",
            "accountName": "Jane Doe"
        },
        {
            "_id": ObjectId("685d15d0672337145292b0de"),
            "owner": "John Smith",
            "accountType": "Checking",
            "bankName": "Bangkok Bank",
            "accessNumber": "098-765-4321",
            "accountName": "John Smith"
        }
    ],
    "datetime": datetime.fromtimestamp(1750930893553 / 1000),
    "unit": "Cyber Unit",
    "amount": 5000,
    "frudDetails": "The scam was well-planned and deceptive.",
    "status": "pending",
    "createdAt": datetime.fromtimestamp(1750930896339 / 1000),
    "updatedAt": datetime.fromtimestamp(1750930896339 / 1000),
    "__v": 0
}

collection.insert_one(document)
print("✅ Inserted complex document successfully.")
