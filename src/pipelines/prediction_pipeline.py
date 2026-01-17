#import necessary modules and libraries
import joblib
from pathlib import Path

# Prediction pipeline to load the trained model and make predictions
class PredictionPipeline:
    def __init__(self):
        self.model = joblib.load(Path("artifacts/model_trainer/model.joblib"))
    
    #method to make predictions
    def predict(self, data):
        predictions = self.model.predict(data)
        return predictions