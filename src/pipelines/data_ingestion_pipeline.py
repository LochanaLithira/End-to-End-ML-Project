#Import necessary modules and libraries
from src.config.configuration import ConfigurationManager
from src.components.data_ingestion import DataIngestion
from src.logging import logger

#Define stage name for logging purposes
STAGE_NAME = "Data Ingestion"

#Data Ingestion Training Pipeline class
class DataIngestionTrainingPipeline:
    def __init__(self):
        pass

    def main(self):
        config = ConfigurationManager()  #Initialize configuration manager
        data_ingestion_config = config.get_data_ingestion_config()  #Get data ingestion configuration
        data_ingestion = DataIngestion(config= data_ingestion_config)  #Initialize data ingestion
        data_ingestion.download_file()  #Download the data file
        data_ingestion.extract_zip_file()

if __name__ == "__main__":  #Entry point for script execution
    try:
        logger.info(f">>>>>> Stage {STAGE_NAME} started <<<<<<")
        obj = DataIngestionTrainingPipeline()
        obj.main()
        logger.info(f">>>>>> Stage {STAGE_NAME} completed <<<<<<\n")
    except Exception as e:
        logger.exception(e)
        raise e