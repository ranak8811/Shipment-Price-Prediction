import os
import sys
import shutil
from shipment.logger import logging
from shipment.exception import shippingException
from shipment.entity.config_entity import ModelPusherConfig
from shipment.entity.artifacts_entity import (
    ModelEvaluationArtifacts,
    ModelPusherArtifacts,
)
from shipment.utils.main_utils import MainUtils


class ModelPusher:
    def __init__(
        self,
        model_pusher_config: ModelPusherConfig,
        model_evaluation_artifact: ModelEvaluationArtifacts,
    ):
        try:
            logging.info("Initializing ModelPusher component")
            self.model_pusher_config = model_pusher_config
            self.model_evaluation_artifact = model_evaluation_artifact
            self.utils = MainUtils()
        except Exception as e:
            raise shippingException(e, sys) from e

    def initiate_model_pusher(self) -> ModelPusherArtifacts:
        logging.info(
            "Entered initiate_model_pusher method of ModelPusher class")
        try:
            if self.model_evaluation_artifact.is_model_accepted:
                logging.info(
                    "Model accepted by evaluation. Proceeding to push...")

                os.makedirs(
                    self.model_pusher_config.BEST_MODEL_DIR_PATH, exist_ok=True)

                source_model_path = self.model_evaluation_artifact.trained_model_path

                target_model_path = self.model_pusher_config.BEST_MODEL_FILE_PATH

                shutil.copy(src=source_model_path, dst=target_model_path)
                logging.info(
                    f"Model copied from {source_model_path} to {target_model_path}")

                os.makedirs(
                    self.model_pusher_config.MODEL_PUSHER_ARTIFACTS_DIR, exist_ok=True)
                artifact_model_path = os.path.join(
                    self.model_pusher_config.MODEL_PUSHER_ARTIFACTS_DIR,
                    os.path.basename(target_model_path)
                )
                shutil.copy(src=source_model_path, dst=artifact_model_path)
                logging.info(
                    f"Model backup artifact saved to {artifact_model_path}")

                model_pusher_artifact = ModelPusherArtifacts(
                    is_model_pushed=True,
                    saved_model_path=target_model_path
                )
            else:
                logging.info("Model rejected by evaluation. Model not pushed.")
                model_pusher_artifact = ModelPusherArtifacts(
                    is_model_pushed=False,
                    saved_model_path=""
                )

            logging.info(f"Model Pusher Artifact: {model_pusher_artifact}")
            return model_pusher_artifact

        except Exception as e:
            raise shippingException(e, sys) from e
