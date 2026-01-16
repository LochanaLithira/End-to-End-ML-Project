#Import the necessary modules and libraries
from src.config.configuration import ConfigurationManager
from src.components.data_validation import DataValidation
from src.logging import logger

#Define stage name for logging purposes
STAGE_NAME = "Data Validation"

#Data Validation Training Pipeline class
class DataValidationTrainingPipeline:
    def __init__(self):
        pass

    def main(self):
        config = ConfigurationManager()  #Initialize configuration manager
        data_validation_config = config.get_data_validation_config()  #Get data validation configuration
        data_validation = DataValidation(config= data_validation_config)  #Initialize data validation
        data_validation.validate_all_columns()  #Validate all columns in the dataset

if __name__ == "__main__":
    try:
        logger.info(f">>>>>> Stage {STAGE_NAME} started <<<<<<")
        obj = DataValidationTrainingPipeline()
        obj.main()
        logger.info(f">>>>>> Stage {STAGE_NAME} completed <<<<<<\n")
    except Exception as e:
        logger.exception(e)
        raise e