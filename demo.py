from shipment.configuration.mongo_operations import MongoDBOperation
from shipment.constants import DB_NAME, COLLECTION_NAME

if __name__ == "__main__":
    print("Testing MongoDB Atlas read connection...")

    # Operations অবজেক্ট তৈরি
    mongo_op = MongoDBOperation()

    # কালেকশন ডেটাফ্রেমে লোড করা
    df = mongo_op.get_collection_as_dataframe(
        db_name=DB_NAME, collection_name=COLLECTION_NAME)

    print("\nData successfully fetched from MongoDB!")
    print("First 5 rows:")
    print(df.head())
    print(f"\nDataFrame Shape: {df.shape}")

# ----------------------------------------  ----------------------------------------


# import sys
# from shipment.logger import logging
# from shipment.exception import shippingException
# from shipment.utils.main_utils import MainUtils

# ----------------------------------------  ----------------------------------------
# ১. লগার টেস্ট
# logging.info("Testing logging module - This is an info message from demo.py")

# ----------------------------------------  ----------------------------------------

# ২. ইউটিলিটি ও YAML রিডার টেস্ট
# try:
#     obj = MainUtils()
#     data = obj.read_yaml_file('config/model.yaml')
#     print("YAML Content successfully read:")
#     print(data)
# except Exception as e:
#     logging.info(f"Failed to read yaml file: {e}")

# ----------------------------------------  ----------------------------------------

# ৩. কাস্টম এক্সেপশন হ্যান্ডলার টেস্ট (০ দিয়ে ভাগ করার চেষ্টা)
# try:
#     logging.info(
#         "Attempting to divide by zero to test custom exception handler...")
#     result = 1 / 0
# except Exception as e:
#     raise shippingException(e, sys) from e
