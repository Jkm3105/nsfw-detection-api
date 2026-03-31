import os
from pymongo import MongoClient
from dotenv import load_dotenv

load_dotenv()

def get_db():
    client = MongoClient(
        os.getenv("MONGO_URI"),
        tls=True,
        tlsAllowInvalidCertificates=True
    )
    db = client[os.getenv("DB_NAME")]
    return db

db = get_db()
logs_collection = db["detection_logs"]

def save_log(log_entry: dict):
    logs_collection.insert_one(log_entry)