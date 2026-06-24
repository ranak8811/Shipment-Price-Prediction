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

    def write_json_to_yaml_file(self, json_file: dict, yaml_file_path: str) -> yaml:
        logging.info(
            "Entered the write_json_to_yaml_file method of MainUtils class")
        try:
            data = json_file
            stream = open(yaml_file_path, "w")
            yaml.dump(data, stream)

        except Exception as e:
            raise shippingException(e, sys) from e
