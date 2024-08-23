import os
import sys

from networksecurity.exception.exception import NetworkSecurityException
from networksecurity.logger.logger import logging

from networksecurity.components.data_ingestion import DataIngestion
from networksecurity.components.data_vaidation import DataVaidation
from networksecurity.components.data_transformation import DataTransformation
from networksecurity.components.model_trainer import ModelTrainer
from networksecurity.components.model_evaluation import ModelEvaluation
from networksecurity.components.model_pusher import ModePusher



from networksecurity.entity.config_entity import (
    TrainingPiplelineconfig,
    DatatIngestionConfig,
    DatatValiidationConfig,
    DataTransformationConfig,
    ModelTrainerConfig,
    ModelEvalutaionConfig,
    ModelPusherCOnfig
)

from networksecurity.entity.config_entity import (
    
    DatatIngestionArtifact,
    DatatValiidationArtifact,
    DataTransformationArtifact,
    ModelTrainerArtifact,
    ModelEvalutaionArtifact,
    ModelPusherArtifact
)



class Training_Pipeline:
    def __init__(self):
        pass

    def start_data_validation(self):
        try:
            pass
        except Exception as e:
            raise NetworkSecurityException(e,sys)
        
    def start_data_transformation(self):
        try:
            pass
        except Exception as e:
            raise NetworkSecurityException(e,sys)
    def start_model_model_trainer(self):
        try:
            pass
        except Exception as e:
            raise NetworkSecurityException(e,sys)
    def start_model_pusher(self):
        try:
            pass
        except Exception as e:
            raise NetworkSecurityException(e,sys)
    def run_pipeine(self):
        try:
            pass
        except Exception as e:
            raise NetworkSecurityException(e,sys)
    


