# ----------------------------------------  ----------------------------------------
# ----------------------------------------  ----------------------------------------
# ----------------------------------------  ----------------------------------------
# ----------------------------------------  ----------------------------------------
# ----------------------------------------  ----------------------------------------
# ----------------------------------------  ----------------------------------------
# ----------------------------------------  ----------------------------------------
# ----------------------------------------  ----------------------------------------
# ----------------------------------------  ----------------------------------------
# ----------------------------------------  ----------------------------------------
# ----------------------------------------  ----------------------------------------
# ----------------------------------------  ----------------------------------------
# ----------------------------------------  ----------------------------------------
# ----------------------------------------  ----------------------------------------
# ----------------------------------------  ----------------------------------------
# ----------------------------------------  ----------------------------------------
# ----------------------------------------  ----------------------------------------
# ----------------------------------------  ----------------------------------------
# ----------------------------------------  ----------------------------------------
# ----------------------------------------  ----------------------------------------
# ----------------------------------------  ----------------------------------------
# ----------------------------------------  ----------------------------------------
# ----------------------------------------  ----------------------------------------
# ----------------------------------------  ----------------------------------------
# ----------------------------------------  ----------------------------------------
# ----------------------------------------  ----------------------------------------
# ----------------------------------------  ----------------------------------------
# ----------------------------------------  ----------------------------------------


# import os
# from shipment.utils.main_utils import MainUtils

# if __name__ == "__main__":
#     print("Testing write_json_to_yaml_file utility method...")

#     # স্যাম্পল ডিকশনারি বা JSON ডাটা
#     dummy_report = {
#         "validation_status": True,
#         "drift_detected": False,
#         "metrics": {
#             "n_features": 15,
#             "n_drifted_features": 0
#         }
#     }

#     test_file_path = "config/test_report.yaml"

#     # Utilities অবজেক্ট তৈরি
#     utils = MainUtils()

#     try:
#         # YAML ফাইলে রাইট করা
#         utils.write_json_to_yaml_file(
#             json_file=dummy_report, yaml_file_path=test_file_path)
#         print(
#             f"\n[SUCCESS] Successfully written dummy report to {test_file_path}!")

#         # পুনরায় রিড করে চেক করা
#         read_data = utils.read_yaml_file(test_file_path)
#         print("Read Data from generated YAML:")
#         print(read_data)

#         # টেস্ট ফাইলটি মুছে ফেলা
#         if os.path.exists(test_file_path):
#             os.remove(test_file_path)

#     except Exception as e:
#         print(f"[ERROR] Test failed: {e}")

# ----------------------------------------  ----------------------------------------

# from shipment.pipline.training_pipeline import TrainPipeline

# if __name__ == "__main__":
#     print("Starting Training Pipeline run...")
#     pipeline = TrainPipeline()
#     pipeline.run_pipeline()
#     print("\nTraining pipeline run completed successfully!")

# ----------------------------------------  ----------------------------------------

# from shipment.entity.config_entity import DataIngestionConfig

# if __name__ == "__main__":
#     print("Testing Data Ingestion Configuration Entity...")

#     # Config অবজেক্ট তৈরি করা
#     config = DataIngestionConfig()

#     print("\n[SUCCESS] Config object successfully initialized!")
#     print(f"Database Name: {config.DB_NAME}")
#     print(f"Collection Name: {config.COLLECTION_NAME}")
#     print(f"Columns to drop: {config.DROP_COLS}")
#     print(f"Ingestion Artifact Dir: {config.DATA_INGESTION_ARTIFCATS_DIR}")
#     print(f"Train File Path: {config.TRAIN_DATA_FILE_PATH}")
#     print(f"Test File Path: {config.TEST_DATA_FILE_PATH}")

# ----------------------------------------  ----------------------------------------

# from shipment.configuration.mongo_operations import MongoDBOperation
# from shipment.constants import DB_NAME, COLLECTION_NAME

# if __name__ == "__main__":
#     print("Testing MongoDB Atlas read connection...")

#     # Operations অবজেক্ট তৈরি
#     mongo_op = MongoDBOperation()

#     # কালেকশন ডেটাফ্রেমে লোড করা
#     df = mongo_op.get_collection_as_dataframe(
#         db_name=DB_NAME, collection_name=COLLECTION_NAME)

#     print("\nData successfully fetched from MongoDB!")
#     print("First 5 rows:")
#     print(df.head())
#     print(f"\nDataFrame Shape: {df.shape}")

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
