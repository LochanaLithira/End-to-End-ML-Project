#Import necessary libraries and modules
import os
import pandas as pd
from src.entities.config_entity import DataValidationConfig

#Data validation class to handle data validation tasks (Data Validation component)
class DataValidation:

    #Initialization method to set up configuration
    def __init__(self, config: DataValidationConfig):
        self.config = config

    #Method to validate all columns in the dataset
    def validate_all_columns(self) -> bool:
        try:
            validatation_status = None
            
            data = pd.read_csv(self.config.unzip_data_dir)
            all_columns = list(data.columns)

            all_schema = self.config.all_schema.keys()

            for column in all_columns:
                if column not in all_schema:
                    validatation_status = False
                    with open(self.config.status_file, 'w') as f:
                        f.write(f"Validation Status: {validatation_status}\n")
                else:
                    validatation_status = True
                    with open(self.config.status_file, 'w') as f:
                        f.write(f"Validation Status: {validatation_status}\n")

            return validatation_status
        
        except Exception as e:
            raise e