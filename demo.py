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

from shipment.entity.config_entity import ModelPusherConfig
from shipment.entity.artifacts_entity import ModelPusherArtifacts

if __name__ == "__main__":
    print("Testing Model Pusher Config & Artifact Entities...")

    # 1. Initialize configuration
    pusher_config = ModelPusherConfig()
    print(
        f"Pusher Artifact Dir Path: {pusher_config.MODEL_PUSHER_ARTIFACTS_DIR}")
    print(
        f"Production Best Model Dir Path: {pusher_config.BEST_MODEL_DIR_PATH}")
    print(
        f"Production Best Model File Path: {pusher_config.BEST_MODEL_FILE_PATH}")

    # 2. Initialize dummy artifact
    pusher_artifact = ModelPusherArtifacts(
        is_model_pushed=True,
        saved_model_path=pusher_config.BEST_MODEL_FILE_PATH
    )
    print("\nDummy Artifact Details:")
    print(f"Is Model Pushed: {pusher_artifact.is_model_pushed}")
    print(f"Saved Model Path: {pusher_artifact.saved_model_path}")
    print("All Model Pusher entities initialized successfully!")

# ----------------------------------------  ----------------------------------------

# from shipment.pipline.training_pipeline import TrainPipeline

# if __name__ == "__main__":
#     try:
#         print("Starting Training Pipeline (Ingestion + Validation + Transformation + Training + Evaluation)...")
#         pipeline = TrainPipeline()
#         pipeline.run_pipeline()
#         print("Training pipeline executed and model evaluated successfully!")
#     except Exception as e:
#         print(f"Pipeline execution failed: {e}")


# ----------------------------------------  ----------------------------------------

# from shipment.pipline.training_pipeline import TrainPipeline
# from shipment.entity.config_entity import ModelEvaluationConfig
# from shipment.entity.artifacts_entity import ModelEvaluationArtifacts

# if __name__ == "__main__":
#     print("Testing Model Evaluation Config & Artifact Entities...")

#     # 1. Initialize configuration
#     eval_config = ModelEvaluationConfig()
#     print(f"Report File Path: {eval_config.REPORT_FILE_PATH}")
#     print(f"Best Model File Path: {eval_config.BEST_MODEL_FILE_PATH}")
#     print(f"Trained Model File Path: {eval_config.TRAINED_MODEL_FILE_PATH}")

#     # 2. Initialize dummy artifact
#     eval_artifact = ModelEvaluationArtifacts(
#         is_model_accepted=True,
#         improved_score=0.035,
#         best_model_path=eval_config.BEST_MODEL_FILE_PATH,
#         trained_model_path=eval_config.TRAINED_MODEL_FILE_PATH
#     )
#     print("\nDummy Artifact Details:")
#     print(f"Is Model Accepted: {eval_artifact.is_model_accepted}")
#     print(f"Improved Score: {eval_artifact.improved_score}")
#     print("All entities initialized successfully!")

# ----------------------------------------  ----------------------------------------

# from shipment.pipline.training_pipeline import TrainPipeline

# if __name__ == "__main__":
#     print("Starting Complete Training Pipeline Run (Ingestion -> Validation -> Transformation -> Trainer)...")
#     pipeline = TrainPipeline()
#     pipeline.run_pipeline()
#     print("\nPipeline run completed successfully!")

# ----------------------------------------  ----------------------------------------

# from shipment.entity.config_entity import ModelTrainerConfig

# if __name__ == "__main__":
#     print("Testing Model Trainer Configuration Entity...")

#     # Config অবজেক্ট তৈরি করা
#     config = ModelTrainerConfig()

#     print("\n[SUCCESS] ModelTrainerConfig initialized successfully!")
#     print(
#         f"Data Transformation Artifact Dir: {config.DATA_TRANSFORMATION_ARTIFACT_DIR if hasattr(config, 'DATA_TRANSFORMATION_ARTIFACT_DIR') else config.DATA_TRANSFORMATION_ARTIFACTS_DIR}")
#     print(f"Model Trainer Artifact Dir: {config.MODEL_TRAINER_ARTIFACTS_DIR}")
#     print(
#         f"Preprocessor Object File Path: {config.PREPROCESSOR_OBJECT_FILE_PATH}")
#     print(f"Trained Model Save File Path: {config.TRAINED_MODEL_FILE_PATH}")


# ----------------------------------------  ----------------------------------------

# import os
# import glob
# from shipment.utils.main_utils import MainUtils

# if __name__ == "__main__":
#     print("Testing load_object utility method...")

#     # সর্বশেষ artifacts ফোল্ডারে জেনারেট হওয়া shipping_preprocessor.pkl ফাইলটি খুঁজে বের করা
#     preprocessor_files = glob.glob(
#         "artifacts/*/DataTransformationArtifacts/shipping_preprocessor.pkl")

#     if not preprocessor_files:
#         print("[ERROR] No preprocessor file found! Please run demo.py of Part 6b first.")
#         os._exit(1)

#     target_pkl_path = preprocessor_files[-1]
#     print(f"Found preprocessor object at: {target_pkl_path}")

#     # Utilities অবজেক্ট তৈরি
#     utils = MainUtils()

#     try:
#         # pkl অবজেক্ট লোড করা
#         preprocessor_obj = utils.load_object(target_pkl_path)
#         print(f"\n[SUCCESS] Successfully loaded preprocessor object!")
#         print(f"Object Type: {type(preprocessor_obj)}")

#     except Exception as e:
#         print(f"[ERROR] Test failed: {e}")

# ----------------------------------------  ----------------------------------------

# from shipment.pipline.training_pipeline import TrainPipeline

# if __name__ == "__main__":
#     print("Starting Training Pipeline (Ingestion + Validation + Transformation)...")
#     pipeline = TrainPipeline()
#     pipeline.run_pipeline()
#     print("\nPipeline run completed successfully!")


# ----------------------------------------  ----------------------------------------

# import os
# import numpy as np
# from shipment.utils.main_utils import MainUtils

# if __name__ == "__main__":
#     print("Testing save_numpy_array_data and save_object utility methods...")

#     # স্যাম্পল ডেটা তৈরি
#     dummy_array = np.array([[1, 2, 3], [4, 5, 6]])
#     dummy_object = {"model_name": "RandomForest",
#                     "hyperparameters": {"n_estimators": 100}}

#     array_file_path = "config/test_array.npy"
#     object_file_path = "config/test_object.pkl"

#     # Utilities অবজেক্ট তৈরি
#     utils = MainUtils()

#     try:
#         # ১. NumPy অ্যারে সেভ ও টেস্ট
#         utils.save_numpy_array_data(
#             file_path=array_file_path, array=dummy_array)
#         print(
#             f"[SUCCESS] Successfully saved dummy numpy array to {array_file_path}!")

#         # ২. অবজেক্ট সেভ ও টেস্ট (dill ব্যবহার করে)
#         utils.save_object(file_path=object_file_path, obj=dummy_object)
#         print(
#             f"[SUCCESS] Successfully saved dummy object to {object_file_path}!")

#         # তৈরি হওয়া টেস্ট ফাইলগুলো ডিলিট করে ফেলা (পরিস্কার রাখতে)
#         if os.path.exists(array_file_path):
#             os.remove(array_file_path)
#         if os.path.exists(object_file_path):
#             os.remove(object_file_path)

#     except Exception as e:
#         print(f"[ERROR] Test failed: {e}")
# ----------------------------------------  ----------------------------------------

# from shipment.pipline.training_pipeline import TrainPipeline

# if __name__ == "__main__":
#     print("Starting Training Pipeline (Ingestion + Validation)...")
#     pipeline = TrainPipeline()
#     pipeline.run_pipeline()
#     print("\nPipeline run completed successfully!")

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
