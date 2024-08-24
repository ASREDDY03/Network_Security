import os
import sys
import numpy as np
import pandas as pd


"""
common variable for the training pipeline

"""

PIPELINE_NAME: str="NetworkSecurity"
TRAGET_COLUMN="Result"
ARIFACT_DIR: str="Artifacts"
FILE_NAME: str="NetworkData.csv"

TRAIN_FILE_NAME="train.csv"
TEST_FILE_NAME="test.csv"

PREPRCESSING_OBJECT_FILE_NAME="preprocessing.pkl"
MODEL_FILE_NAME="model.pkl"
SCHEMA_FILE_PATH=os.path.join("data_schedma","schema.yaml")
SCHEMA_DROP_COLS="drop_columns"


SAVED_MODEL_DIR=os.path.join("saved.models")



"""
Data Ingestion related constant start with DATA_INGESTION VAR NAME

"""
DATA_INGESTION_COLLLECTION_NAME: str="NetworkData"
DATA_INGESTION_DATABASE_NAME: str="SRAcademy"
DATA_INGESTION_DIR_NAME: str="data_ingestion"
DATA_INGESTION_FEATURE_STORE_DATA: str="feature_store"
DATA_INGESTION: str="ingested"
DATA_INGESTION_TRAIN_TEST_SPLIT_RATION: float=0.2

"""
Data Vaidation related cnstant start ith DATA_VALIDATION VAR NAME

"""

"""
Data Transformation related costant start with DATA_TRANSFORMATION VAR NAME
"""

"""
MOdel Trainer related constant with MODE TRAINER VAR NAME
"""

