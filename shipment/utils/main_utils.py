import sys
import yaml
from shipment.constants import *
from shipment.exception import shippingException
from shipment.logger import logging


class MainUtils:
    def read_yaml_file(self, filename: str) -> dict:
        logging.info("Entered the read_yaml_file method of MainUtils class")
        try:
            with open(filename, "rb") as yaml_file:
                return yaml.safe_load(yaml_file)

        except Exception as e:
            raise shippingException(e, sys) from e
