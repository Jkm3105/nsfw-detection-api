import os
from pymongo import MongoClient
from dotenv import load_dotenv

load_dotenv()

DB_URL = os.environ.get("DB_URL", "mongodb://localhost:27017")
DB_NAME = os.environ.get("DB_NAME", "nsfw_logs")

def get_db():
    client = MongoClient(
        DB_URL,
        tls=True,
        tlsAllowInvalidCertificates=True,
        serverSelectionTimeoutMS=5000
    )
    db = client[DB_NAME]
    return db

try:
    db = get_db()
    logs_collection = db["detection_logs"]
    print(f"✅ Connected to MongoDB: {DB_NAME}")
except Exception as e:
    print(f"❌ MongoDB connection failed: {e}")
    logs_collection = None

def save_log(log_entry: dict):
    if logs_collection is not None:
        logs_collection.insert_one(log_entry)
    else:
        print("⚠️ MongoDB not available, skipping log")