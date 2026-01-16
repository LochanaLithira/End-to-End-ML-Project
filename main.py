#Importing necessary modules and classes
from src.logging import logger
from src.pipelines.data_ingestion_pipeline import DataIngestionTrainingPipeline
from src.pipelines.data_validation_pipeline import DataValidationTrainingPipeline

#Execution of Data Ingestion Pipeline
STAGE_NAME = "Data Ingestion"
try:
    logger.info(f">>>>>> Stage {STAGE_NAME} started <<<<<<")
    obj = DataIngestionTrainingPipeline()
    obj.main()
    logger.info(f">>>>>> Stage {STAGE_NAME} completed <<<<<<\n")
except Exception as e:
    logger.exception(e)
    raise e

#Execution of Data Validation Pipeline
STAGE_NAME = "Data Validation"
try:
    logger.info(f">>>>>> Stage {STAGE_NAME} started <<<<<<")
    obj = DataValidationTrainingPipeline()
    obj.main()
    logger.info(f">>>>>> Stage {STAGE_NAME} completed <<<<<<\n")
except Exception as e:
    logger.exception(e)
    raise e