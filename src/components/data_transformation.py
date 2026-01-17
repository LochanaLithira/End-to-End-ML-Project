#Import necessary modules and libraries
import os
import pandas as pd
from sklearn.model_selection import train_test_split
from src.config.configuration import DataTransformationConfig
from src.logging import logger

#Data Transformation class to handle data splitting (Data Transformation component)
class DataTransformation:
    def __init__(self, config: DataTransformationConfig):
        self.config = config

    def train_test_splitting(self):
        data = pd.read_csv(self.config.data_path)
        data = data.drop(columns=['Id'])  #Dropping unnecessary column
        
        #Splitting the dataset into training and testing sets
        train,test = train_test_split(data, test_size = 0.2, random_state = 42)

        #Saving the training and testing sets to CSV files
        train.to_csv(os.path.join(self.config.root_dir, "train.csv"), index = False)
        test.to_csv(os.path.join(self.config.root_dir, "test.csv"), index = False)

        logger.info("Splitted dataset into training and test sets")
        logger.info(train.shape)
        logger.info(test.shape)