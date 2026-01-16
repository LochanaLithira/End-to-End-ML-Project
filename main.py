#Importing necessary modules and classes
from src.logging import logger
from src.pipelines.data_ingestion_pipeline import STAGE_NAME, DataIngestionTrainingPipeline

#Execution of Data Ingestion Pipeline
try:
    logger.info(f">>>>>> Stage {STAGE_NAME} started <<<<<<")
    obj = DataIngestionTrainingPipeline()
    obj.main()
    logger.info(f">>>>>> Stage {STAGE_NAME} completed <<<<<<\n")
except Exception as e:
    logger.exception(e)
    raise e