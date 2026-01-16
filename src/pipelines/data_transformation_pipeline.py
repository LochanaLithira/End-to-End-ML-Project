from pathlib import Path
from src.config.configuration import ConfigurationManager
from src.components.data_transformation import DataTransformation
from src.logging import logger


#Define stage name for logging purposes
STAGE_NAME = "Data Transformation"

#Data Transformation Training Pipeline class
class DataTransformationTrainingPipeline:
    def __init__(self):
        pass

    def main(self):
        try:
            #Check data validation status
            with open(Path("artifacts/data_validation/status.txt"), "r") as f:  #Read validation status file
                status = f.read().split(" ")[-1].strip()  #Get the last word indicating status
            
            if status == "True":
                config = ConfigurationManager()  #Initialize configuration manager
                data_transformation_config = config.get_data_transformation_config()  #Get data transformation configuration
                data_transformation = DataTransformation(config= data_transformation_config)  #Initialize data transformation
                data_transformation.train_test_splitting()  #Perform train-test splitting
            else:
                raise Exception("Data Validation Failed. Cannot proceed to Data Transformation.")
        except Exception as e:
            logger.exception(e)
            raise e
        