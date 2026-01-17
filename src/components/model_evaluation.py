#Import necessary modules and libraries
import numpy as np
import pandas as pd
import joblib
from pathlib import Path
from sklearn.metrics import mean_squared_error, mean_absolute_error, r2_score
from src.entities.config_entity import ModelEvaluationConfig
from src.utils.common import create_json

#Model evaluation class to evaluate the trained model (Model Evaluation component)
class ModelEvaluation   :
    def __init__(self, config: ModelEvaluationConfig):
        self.config = config
    
    #Method to evaluate the model
    def evaluate_metrics(self, actual, predicted):
        rmse = np.sqrt(mean_squared_error(actual, predicted))
        mae = mean_absolute_error(actual, predicted)
        r2 = r2_score(actual, predicted)

        return rmse, mae, r2 
    
    #Method to save evaluation results
    def save_results(self):
        test_data = pd.read_csv(self.config.test_data_path)
        model = joblib.load(self.config.model_path)

        X_test = test_data.drop([self.config.target_column], axis=1)
        y_test = test_data[self.config.target_column]

        # Predicting the values using the trained model
        predicted_qualities = model.predict(X_test)

        # Calculating evaluation metrics
        rmse, mae, r2 = self.evaluate_metrics(y_test, predicted_qualities)

        # Saving the evaluation metrics to a JSON file
        scores = {"RMSE": rmse, "MAE": mae, "R2_Score": r2}
        create_json(path = Path(self.config.metrics_file_path), data = scores)

