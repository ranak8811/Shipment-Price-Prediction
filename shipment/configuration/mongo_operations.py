import sys
from pandas import DataFrame
from pymongo.database import Database
import pandas as pd
from pymongo import MongoClient
from shipment.constants import DB_URL
from shipment.exception import shippingException
from shipment.logger import logging


class MongoDBOperation:
    def __init__(self):
        self.DB_URL = DB_URL
        self.client = MongoClient(self.DB_URL)

    def get_database(self, db_name) -> Database:
        logging.info("Entered get_database method of MongoDB_Operation class")
        try:
            db = self.client[db_name]
            logging.info(f"Created/Accessed {db_name} database in MongoDB")
            logging.info("Exited get_database method MongoDB_Operation class")
            return db
        except Exception as e:
            raise shippingException(e, sys) from e

    def get_collection_as_dataframe(self, db_name, collection_name) -> DataFrame:
        logging.info(
            "Entered get_collection_as_dataframe method of MongoDB_Operation class"
        )
        try:
            database = self.get_database(db_name)
            collection = database.get_collection(name=collection_name)

            df = pd.DataFrame(list(collection.find()))

            if "_id" in df.columns.to_list():
                df = df.drop(columns=["_id"])

            logging.info("Converted collection to dataframe")
            logging.info(
                "Exited get_collection_as_dataframe method of MongoDB_Operation class"
            )
            return df
        except Exception as e:
            raise shippingException(e, sys) from e
