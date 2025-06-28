from pymongo import MongoClient
from bson.objectid import ObjectId
from datetime import datetime
from faker import Faker
import random

fake = Faker('en_TH')  # ใช้ locale ไทย

def random_phone_number():
    return "0" + str(random.choice([6,8,9])) + ''.join([str(random.randint(0, 9)) for _ in range(8)])

def random_id_card():
    return ''.join([str(random.randint(0, 9)) for _ in range(13)])

def random_bank_name():
    return random.choice(["Krungthai", "Bangkok Bank", "SCB", "Kasikorn", "TMB", "BAAC", "UOB"])

def random_account_type():
    return random.choice(["Savings", "Checking", "Fixed"])

def generate_case():
    now = datetime.now()
    person = fake.simple_profile()

    first = fake.first_name()
    last = fake.last_name()
    email = person["mail"]
    phone = random_phone_number()
    idcard = random_id_card()
    birthdate = fake.date_of_birth()
    address = fake.address().split("\n")[0]

    return {
        "_id": ObjectId(),
        "CrimeType": "Online Scam",
        "BankCaseID": "CASE" + str(ObjectId())[-6:],
        "user": {
            "prefix": random.choice(["Mr", "Ms", "Mrs"]),
            "firstName": first,
            "lastName": last,
            "idCard": idcard,
            "email": email,
            "phoneNumber": phone,
            "phoneCarrier": random.choice(["AIS", "DTAC", "True"]),
            "birthDate": {
                "day": birthdate.day,
                "month": birthdate.month,
                "year": birthdate.year
            },
            "idCardAddress": {
                "address": address,
                "district": fake.city(),
                "subDistrict": fake.city_suffix(),
                "province": fake.province(),
                "postalCode": fake.postcode()
            },
            "currentAddress": {
                "address": fake.street_address(),
                "district": fake.city(),
                "subDistrict": fake.city_suffix(),
                "province": fake.province(),
                "postalCode": fake.postcode()
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
                "_id": ObjectId(),
                "owner": fake.name(),
                "accountType": random_account_type(),
                "bankName": random_bank_name(),
                "accessNumber": fake.bban(),
                "accountName": fake.name()
            },
            {
                "_id": ObjectId(),
                "owner": fake.name(),
                "accountType": random_account_type(),
                "bankName": random_bank_name(),
                "accessNumber": fake.bban(),
                "accountName": fake.name()
            }
        ],
        "datetime": now,
        "unit": "Cyber Unit",
        "amount": random.randint(1000, 50000),
        "frudDetails": "The scam was well-planned and deceptive.",
        "status": "pending",
        "createdAt": now,
        "updatedAt": now,
        "__v": 0
    }

# ใช้งานจริง
if __name__ == "__main__":
    client = MongoClient("mongodb://localhost:27017/")
    db = client["mydatabase"]
    collection = db["cases"]

    document = generate_case()
    collection.insert_one(document)
    print(" Inserted random generated case for:", document["user"]["firstName"], document["user"]["lastName"])
