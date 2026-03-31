import os
from pymongo import MongoClient
from dotenv import load_dotenv

load_dotenv()

client = MongoClient(os.getenv("DB_URL"))
db = client[os.getenv("DB_NAME")]
logs_collection = db["detection_logs"]

def save_log(log_entry: dict):
    logs_collection.insert_one(log_entry)