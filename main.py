#Importing necessary modules and classes
from src.logging import logger
from src.pipelines.data_ingestion_pipeline import DataIngestionTrainingPipeline
from src.pipelines.data_validation_pipeline import DataValidationTrainingPipeline
from src.pipelines.data_transformation_pipeline import DataTransformationTrainingPipeline
from src.pipelines.model_trainer_pipeline import ModelTrainerTrainingPipeline

#Execution of Data Ingestion Pipeline
STAGE_NAME = "Data Ingestion"
try:
    logger.info(f">>>>>> Stage {STAGE_NAME} started <<<<<<")
    data_ingestion = DataIngestionTrainingPipeline()
    data_ingestion.main()
    logger.info(f">>>>>> Stage {STAGE_NAME} completed <<<<<<\n")
except Exception as e:
    logger.exception(e)
    raise e

#Execution of Data Validation Pipeline
STAGE_NAME = "Data Validation"
try:
    logger.info(f">>>>>> Stage {STAGE_NAME} started <<<<<<")
    data_validation = DataValidationTrainingPipeline()
    data_validation.main()
    logger.info(f">>>>>> Stage {STAGE_NAME} completed <<<<<<\n")
except Exception as e:
    logger.exception(e)
    raise e

#Execution of Data Transformation Pipeline
STAGE_NAME = "Data Transformation"
try:
    logger.info(f">>>>>> Stage {STAGE_NAME} started <<<<<<")
    data_transformation = DataTransformationTrainingPipeline()
    data_transformation.main()
    logger.info(f">>>>>> Stage {STAGE_NAME} completed <<<<<<\n")
except Exception as e:
    logger.exception(e)
    raise e

#Execution of Model Trainer Pipeline
STAGE_NAME = "Model Trainer"
try:
    logger.info(f">>>>>> Stage {STAGE_NAME} started <<<<<<")
    model_trainer = ModelTrainerTrainingPipeline()
    model_trainer.main()
    logger.info(f">>>>>> Stage {STAGE_NAME} completed <<<<<<\n")
except Exception as e:
    logger.exception(e)
    raise e