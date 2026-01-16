#Import necessary libraries and modules
import os
import urllib.request as request
from pathlib import Path
import zipfile
from src.utils.common import get_size
from src.entities.config_entity import DataIngestionConfig
from src.logging import logger

#Data Ingestion class to handle data downloading and extraction (Date Ingestion component)
class DataIngestion:

    #Initialization method to set up configuration
    def __init__(self, config: DataIngestionConfig):
        self.config = config

    #Method to download file from source URL
    def download_file(self):
        if not os.path.exists(self.config.local_data_file):
            filename, headers = request.urlretrieve(
                url = self.config.source_URL,
                filename = self.config.local_data_file
            )
            logger.info(f"File: {filename} downloaded with following info: \n{headers}")
        else:
            logger.info(f"File already exists of size: {get_size(Path(self.config.local_data_file))}")
    
    #Method to extract the downloaded zip file
    def extract_zip_file(self):
        unzip_path = self.config.unzip_dir
        os.makedirs(unzip_path, exist_ok= True)  #Create directory if it doesn't exist
        
        #Extract the zip file
        with zipfile.ZipFile(self.config.local_data_file, 'r') as zip_ref:
            zip_ref.extractall(unzip_path)  #Extract all contents to the specified directory
        logger.info(f"File extracted to: {unzip_path}")


