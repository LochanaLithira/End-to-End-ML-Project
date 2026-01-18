#Import necessary modules and libraries
import os 
import numpy as np
import pandas as pd
from flask import Flask, request, render_template
from src.pipelines.prediction_pipeline import PredictionPipeline

app = Flask(__name__)  #Initialize Flask application

#Define route for home page
@app.route('/')
def home():
    return render_template('index.html')  #Render the home page

#Define route for training the model
@app.route('/train', methods = ['GET'])
def train():
    os.system("python main.py")  #Execute the main.py script to start training
    return "Training Successful"

#Define route for making predictions
@app.route('/predict', methods = ['POST'])
def index():
    if request.method == 'POST':
        try:
            #Extract input features from the form
            fixed_acidity = float(request.form['fixed_acidity'])
            volatile_acidity = float(request.form['volatile_acidity'])
            citric_acid = float(request.form['citric_acid'])
            residual_sugar = float(request.form['residual_sugar'])
            chlorides = float(request.form['chlorides'])
            free_sulfur_dioxide = float(request.form['free_sulfur_dioxide'])
            total_sulfur_dioxide = float(request.form['total_sulfur_dioxide'])
            density = float(request.form['density'])
            pH = float(request.form['pH'])
            sulphates = float(request.form['sulphates'])
            alcohol = float(request.form['alcohol'])

            #Create a DataFrame with input features and column names
            data = pd.DataFrame([[fixed_acidity, volatile_acidity, citric_acid,
                    residual_sugar, chlorides, free_sulfur_dioxide,
                    total_sulfur_dioxide, density, pH, sulphates, alcohol]],
                    columns=['fixed acidity', 'volatile acidity', 'citric acid',
                             'residual sugar', 'chlorides', 'free sulfur dioxide',
                             'total sulfur dioxide', 'density', 'pH', 'sulphates', 'alcohol'])

            #Make prediction using the prediction pipeline
            pipeline = PredictionPipeline()
            predict = pipeline.predict(data)

            return render_template('results.html', prediction = str(predict))  #Render results page with prediction
        
        except Exception as e:
            return f"An error occurred: {e}"
    else:
        return render_template('index.html')  #Render the home page for GET requests


if __name__ == "__main__":
    app.run(host = '0.0.0.0', port=5000)  #Run the Flask application
