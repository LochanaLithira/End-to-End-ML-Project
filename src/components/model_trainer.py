#Import necessary modules and libraries
import os
import pandas as pd
import joblib
from sklearn.linear_model import ElasticNet
from src.entities.config_entity import ModelTrainerConfig

#Model Trainer class to handle model training (Model Trainer component)
class ModelTrainer:
    def __init__(self, config:ModelTrainerConfig):
        self.config = config
    
    #Method to train the model
    def model_train(self):
        train_data = pd.read_csv(self.config.train_data_path)
        test_data = pd.read_csv(self.config.test_data_path)
        
        #Splitting train data into features and target variable
        X_train = train_data.drop([self.config.target_column], axis=1)
        y_train = train_data[self.config.target_column]
        
        #Splitting test data into features and target variable
        X_test = test_data.drop([self.config.target_column], axis=1)
        y_test = test_data[self.config.target_column]

        #Initializing and training the ElasticNet model
        model = ElasticNet(alpha = self.config.alpha, l1_ratio = self.config.l1_ratio, random_state = self.config.random_state)
        model.fit(X_train, y_train)

        #Saving the trained model to the specified path
        joblib.dump(model, os.path.join(self.config.root_dir, self.config.model_name))