import os
import sys

import pandas as pd
import numpy as np
import pymongo
from typing import List
from dotenv import load_dotenv

from networksecurity.exception.exception import NetworkSecurityException
from networksecurity.logger.logger import logging

# cnfiguration of artifact and component genenration

from networksecurity.entity.config_entity import DatatIngestionArtifact
from networksecurity.entity.config_entity import DatatIngestionConfig


load_dotenv()
MONGO_DB_URL=os.getenv("MONGO_DB_URL")
print(MONGO_DB_URL)


class DataIngestion:
    def __init__(self):
        try:
            pass
        except Exception as e:
            raise NetworkSecurityException(e,sys)
        
    def export_collection_as_dataframe(self):
        try:
            pass
        except Exception as e:
            raise NetworkSecurityException(e,sys)
    

    def export_data_into_feature_store(self):
        try:
            pass
        except Exception as e:
            raise NetworkSecurityException(e,sys)
        

    def split_data_as_train_test(self):
        try:
            pass
        except Exception as e:
            raise NetworkSecurityException(e,sys)
        
    
        





