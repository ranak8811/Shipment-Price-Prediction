import os
from shipment.logger import logging
import sys
from pandas import DataFrame
import numpy as np
import pandas as pd
from sklearn.compose import ColumnTransformer
from sklearn.preprocessing import OneHotEncoder, StandardScaler
from shipment.entity.config_entity import DataTransformationConfig
from shipment.entity.artifacts_entity import (
    DataIngestionArtifacts,
    DataTransformationArtifacts,
)
from shipment.exception import shippingException


class DataTransformation:
    def __init__(
        self,
        data_ingestion_artifacts: DataIngestionArtifacts,
        data_transformation_config: DataTransformationConfig,
    ):
        self.data_ingestion_artifacts = data_ingestion_artifacts
        self.data_transformation_config = data_transformation_config

        # Reading train.csv and test.csv from data ingestion artifacts
        self.train_set = pd.read_csv(
            self.data_ingestion_artifacts.train_data_file_path)
        self.test_set = pd.read_csv(
            self.data_ingestion_artifacts.test_data_file_path)

    def get_data_transformer_object(self) -> object:
        logging.info(
            "Entered get_data_transformer_object method of Data_Ingestion class"
        )
        try:
            numerical_columns = self.data_transformation_config.SCHEMA_CONFIG[
                "numerical_columns"
            ]
            original_onehot_columns = self.data_transformation_config.SCHEMA_CONFIG[
                "onehot_columns"
            ]
            binary_columns = self.data_transformation_config.SCHEMA_CONFIG[
                "binary_columns"
            ]
            onehot_columns = [
                col for col in original_onehot_columns if col not in binary_columns
            ]
            logging.info(
                "Got numerical cols, one hot cols, binary cols from schema config"
            )

            numeric_transformer = StandardScaler()
            oh_transformer = OneHotEncoder(
                handle_unknown="ignore", sparse_output=False)
            binary_transformer = OneHotEncoder(
                handle_unknown="ignore", drop="if_binary", sparse_output=False
            )
            logging.info(
                "Initialized StandardScaler, OneHotEncoder, binary OneHotEncoder for binary cols"
            )

            transformers = []
            if onehot_columns:
                transformers.append(
                    ("OneHotEncoder", oh_transformer, onehot_columns))
            if binary_columns:
                transformers.append(
                    ("BinaryEncoder", binary_transformer, binary_columns))
            transformers.append(
                ("StandardScaler", numeric_transformer, numerical_columns))

            preprocessor = ColumnTransformer(transformers)
            logging.info("Created preprocessor object from ColumnTransformer")

            logging.info(
                "Exited get_data_transformer_object method of Data_Ingestion class"
            )
            return preprocessor

        except Exception as e:
            raise shippingException(e, sys) from e

    @staticmethod
    def _outlier_capping(col, df: DataFrame) -> DataFrame:
        logging.info(
            "Entered _outlier_capping method of Data_Transformation class")
        try:
            logging.info(
                "Performing _outlier_capping for columns in the dataframe")
            percentile25 = df[col].quantile(0.25)
            percentile75 = df[col].quantile(0.75)

            iqr = percentile75 - percentile25
            upper_limit = percentile75 + 1.5 * iqr
            lower_limit = percentile25 - 1.5 * iqr

            df.loc[(df[col] > upper_limit), col] = upper_limit
            df.loc[(df[col] < lower_limit), col] = lower_limit
            logging.info(
                "Performed _outlier_capping method of Data_Transformation class"
            )

            logging.info(
                "Exited _outlier_capping method of Data_Transformation class")
            return df

        except Exception as e:
            raise shippingException(e, sys) from e

    def initiate_data_transformation(self) -> DataTransformationArtifacts:
        logging.info(
            "Entered initiate_data_transformation method of Data_Transformation class"
        )
        try:
            os.makedirs(
                self.data_transformation_config.DATA_TRANSFORMATION_ARTIFACTS_DIR,
                exist_ok=True,
            )
            logging.info(
                f"Created artifacts directory for {os.path.basename(self.data_transformation_config.DATA_TRANSFORMATION_ARTIFACTS_DIR)}"
            )

            preprocessor = self.get_data_transformer_object()
            logging.info("Got the preprocessor object")

            target_column_name = self.data_transformation_config.SCHEMA_CONFIG[
                "target_column"
            ]
            numerical_columns = self.data_transformation_config.SCHEMA_CONFIG[
                "numerical_columns"
            ]
            logging.info(
                "Got target column name and numerical columns from schema config"
            )

            continuous_columns = [
                feature
                for feature in numerical_columns
                if len(self.train_set[feature].unique()) >= 25
            ]
            logging.info("Got a list of continuous_columns")
            [self._outlier_capping(col, self.train_set)
             for col in continuous_columns]
            logging.info("Outlier capped in train df")
            [self._outlier_capping(col, self.test_set)
             for col in continuous_columns]
            logging.info("Outlier capped in test df")

            input_feature_train_df = self.train_set.drop(
                columns=[target_column_name], axis=1
            )
            target_feature_train_df = self.train_set[target_column_name]
            logging.info("Got train features and test feature")

            input_feature_test_df = self.test_set.drop(
                columns=[target_column_name], axis=1
            )
            target_feature_test_df = self.test_set[target_column_name]
            logging.info("Got train features and test feature")

            input_feature_train_arr = preprocessor.fit_transform(
                input_feature_train_df)
            input_feature_test_arr = preprocessor.transform(
                input_feature_test_df)
            logging.info(
                "Used the preprocessor object to transform the test features")

            train_arr = np.c_[
                input_feature_train_arr, np.array(target_feature_train_df)
            ]
            logging.info("Created train array.")

            os.makedirs(
                self.data_transformation_config.TRANSFORMED_TRAIN_DATA_DIR,
                exist_ok=True,
            )
            transformed_train_file = self.data_transformation_config.UTILS.save_numpy_array_data(
                self.data_transformation_config.TRANSFORMED_TRAIN_FILE_PATH, train_arr
            )
            logging.info(
                f"Saved train array to {os.path.basename(self.data_transformation_config.DATA_TRANSFORMATION_ARTIFACTS_DIR)}"
            )

            test_arr = np.c_[input_feature_test_arr,
                             np.array(target_feature_test_df)]
            logging.info("Created test array.")

            os.makedirs(
                self.data_transformation_config.TRANSFORMED_TEST_DATA_DIR, exist_ok=True
            )
            transformed_test_file = self.data_transformation_config.UTILS.save_numpy_array_data(
                self.data_transformation_config.TRANSFORMED_TEST_FILE_PATH, test_arr
            )
            logging.info(
                f"Saved test array to {os.path.basename(self.data_transformation_config.DATA_TRANSFORMATION_ARTIFACTS_DIR)}"
            )

            preprocessor_obj_file = self.data_transformation_config.UTILS.save_object(
                self.data_transformation_config.PREPROCESSOR_FILE_PATH, preprocessor
            )
            logging.info(
                "Saved the preprocessor object in DataTransformation artifacts directory."
            )
            logging.info(
                "Exited initiate_data_transformation method of Data_Transformation class"
            )

            data_transformation_artifacts = DataTransformationArtifacts(
                transformed_object_file_path=preprocessor_obj_file,
                transformed_train_file_path=transformed_train_file,
                transformed_test_file_path=transformed_test_file,
            )

            return data_transformation_artifacts

        except Exception as e:
            raise shippingException(e, sys) from e
