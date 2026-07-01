import os
import sys
import pandas as pd
from shipment.logger import logging
from shipment.exception import shippingException
from shipment.utils.main_utils import MainUtils
from shipment.constants import BEST_MODEL_DIR, BEST_MODEL_FILE_NAME


class PredictionPipeline:
    def __init__(self):
        try:
            self.utils = MainUtils()
            self.model_path = os.path.join(
                os.getcwd(), BEST_MODEL_DIR, BEST_MODEL_FILE_NAME
            )
        except Exception as e:
            raise shippingException(e, sys) from e

    def predict(self, dataframe: pd.DataFrame) -> pd.Series:
        logging.info("Entered predict method of PredictionPipeline class")
        try:
            logging.info(f"Loading best model from: {self.model_path}")
            model = self.utils.load_object(self.model_path)
            logging.info("Model loaded successfully. Making predictions...")

            predictions = model.predict(dataframe)
            return predictions
        except Exception as e:
            raise shippingException(e, sys) from e


class ShipmentData:
    def __init__(
        self,
        artist_reputation: float,
        height: float,
        width: float,
        weight: float,
        material: str,
        price_of_sculpture: float,
        base_shipping_price: float,
        international: str,
        express_shipment: str,
        installation_included: str,
        transport: str,
        fragile: str,
        customer_information: str,
        remote_location: str,
    ):
        self.artist_reputation = artist_reputation
        self.height = height
        self.width = width
        self.weight = weight
        self.material = material
        self.price_of_sculpture = price_of_sculpture
        self.base_shipping_price = base_shipping_price
        self.international = international
        self.express_shipment = express_shipment
        self.installation_included = installation_included
        self.transport = transport
        self.fragile = fragile
        self.customer_information = customer_information
        self.remote_location = remote_location

    def get_data_as_dataframe(self) -> pd.DataFrame:
        try:
            custom_data_input_dict = {
                "Artist Reputation": [self.artist_reputation],
                "Height": [self.height],
                "Width": [self.width],
                "Weight": [self.weight],
                "Material": [self.material],
                "Price Of Sculpture": [self.price_of_sculpture],
                "Base Shipping Price": [self.base_shipping_price],
                "International": [self.international],
                "Express Shipment": [self.express_shipment],
                "Installation Included": [self.installation_included],
                "Transport": [self.transport],
                "Fragile": [self.fragile],
                "Customer Information": [self.customer_information],
                "Remote Location": [self.remote_location],
            }
            df = pd.DataFrame(custom_data_input_dict)
            return df
        except Exception as e:
            raise shippingException(e, sys) from e
