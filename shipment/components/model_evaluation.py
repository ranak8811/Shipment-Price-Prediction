import os
import sys
import pandas as pd
from sklearn.metrics import r2_score
from shipment.logger import logging
from shipment.exception import shippingException
from shipment.entity.config_entity import ModelEvaluationConfig
from shipment.entity.artifacts_entity import (
    DataTransformationArtifacts,
    ModelTrainerArtifacts,
    ModelEvaluationArtifacts,
)
from shipment.utils.main_utils import MainUtils


class ModelEvaluation:
    def __init__(
            self,
            model_eval_config: ModelEvaluationConfig,
            data_transformation_artifact: DataTransformationArtifacts,
            model_trainer_artifact: ModelTrainerArtifacts,
    ):
        try:
            logging.info("Initializing ModelEvaluation component")

            self.model_eval_config = model_eval_config
            self.data_transformation_artifact = data_transformation_artifact
            self.model_trainer_artifact = model_trainer_artifact
            self.utils = MainUtils()
        except Exception as e:
            raise shippingException(e, sys) from e

    def initiate_model_evaluation(self) -> ModelEvaluationArtifacts:
        logging.info(
            "Entered initiate_model_evaluation method of ModelEvaluation class")

        try:
            os.makedirs(
                self.model_eval_config.MODEL_EVALUATION_ARTIFACTS_DIR, exist_ok=True)
            logging.info("Created Model Evaluation artifacts directory")

            transformed_test_file_path = self.data_transformation_artifact.transformed_test_file_path
            test_array = self.utils.load_numpy_array_data(
                transformed_test_file_path)

            x_test = test_array[:, : -1]
            y_test = test_array[:, -1]

            logging.info(
                "Loaded and split test array into features and target")

            trained_model_path = self.model_trainer_artifact.trained_model_file_path
            trained_model = self.utils.load_object(trained_model_path)

            y_pred_new = trained_model.trained_model_object.predict(x_test)
            r2_new = r2_score(y_test, y_pred_new)
            logging.info(f"Newly trained model R2 score: {r2_new}")

            best_model_file_path = self.model_eval_config.BEST_MODEL_FILE_PATH
            is_model_accepted = False
            improved_score = 0.0
            best_model_path = ""

            if os.path.exists(best_model_file_path):
                logging.info(
                    "Previous best model found. Starting evaluation...")
                best_model = self.utils.load_object(best_model_file_path)

                y_pred_best = best_model.trained_model_object.predict(x_test)
                r2_best = r2_score(y_test, y_pred_best)
                logging.info(f"Previous best model R2 score: {r2_best}")

                improved_score = r2_new - r2_best
                best_model_path = best_model_file_path

                if r2_new > r2_best:
                    is_model_accepted = True
                    logging.info(
                        "New model outperforms the previous model. Model accepted!")
                else:
                    is_model_accepted = False
                    logging.info(
                        "New model does not outperform the previous model. Model rejected.")
            else:
                logging.info(
                    "No previous best model found. New model accepted automatically!")
                is_model_accepted = True
                improved_score = r2_new
                best_model_path = ""

            evaluation_report = {
                "is_model_accepted": is_model_accepted,
                "trained_model_score": float(r2_new),
                "best_model_score": float(r2_new - improved_score) if os.path.exists(best_model_file_path) else None,
                "improved_score": float(improved_score)
            }

            self.utils.write_json_to_yaml_file(
                json_content=evaluation_report,
                file_path=self.model_eval_config.REPORT_FILE_PATH
            )
            logging.info(
                f"Evaluation report saved to {self.model_eval_config.REPORT_FILE_PATH}")

            model_eval_artifact = ModelEvaluationArtifacts(
                is_model_accepted=is_model_accepted,
                improved_score=improved_score,
                best_model_path=best_model_path,
                trained_model_path=trained_model_path
            )
            logging.info(f"Model Evaluation Artifact: {model_eval_artifact}")
            return model_eval_artifact

        except Exception as e:
            raise shippingException(e, sys) from e
