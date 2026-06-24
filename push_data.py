import os
import sys
import pandas as pd
from pymongo import MongoClient
from dotenv import load_dotenv

load_dotenv()

MONGO_DB_URL = os.getenv("MONGO_DB_URL")
if not MONGO_DB_URL:
    print("Error: MONGO_DB_URL is not set in .env file.")
    sys.exit(1)

DB_NAME = "ShipmentPriceDB"
COLLECTION_NAME = "shipment_price_collection"
DATA_FILE_PATH = "data/Shipment-data.csv"

try:
    print(f"Reading data from {DATA_FILE_PATH}...")
    df = pd.read_csv(DATA_FILE_PATH)
    print(f"Loaded {df.shape[0]} rows and {df.shape[1]} columns.")

    data_dict = df.to_dict(orient="records")

    print("Connecting to MongoDB Atlas...")
    client = MongoClient(MONGO_DB_URL)
    db = client[DB_NAME]
    collection = db[COLLECTION_NAME]

    print("Dropping existing collection if any...")
    collection.drop()

    print("Uploading data to MongoDB Atlas...")
    collection.insert_many(data_dict)
    print("Data uploaded successfully to MongoDB Atlas!")

except Exception as e:
    print(f"An error occurred: {e}")
