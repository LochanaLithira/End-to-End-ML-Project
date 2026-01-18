# 🍷 Wine Quality Prediction - End-to-End ML Project

![Python](https://img.shields.io/badge/Python-3.10-blue.svg)
![Flask](https://img.shields.io/badge/Flask-Web%20App-green.svg)
![scikit-learn](https://img.shields.io/badge/scikit--learn-ML-orange.svg)
![Docker](https://img.shields.io/badge/Docker-Containerized-blue.svg)
![License](https://img.shields.io/badge/License-MIT-yellow.svg)

A production-ready, modular machine learning project that predicts wine quality based on physicochemical properties. This project demonstrates best practices in ML engineering with a complete pipeline from data ingestion to model deployment.

## 📋 Table of Contents

- [Overview](#overview)
- [Features](#features)
- [Project Structure](#project-structure)
- [Installation](#installation)
- [Usage](#usage)
- [ML Pipeline Stages](#ml-pipeline-stages)
- [Model Details](#model-details)
- [API Endpoints](#api-endpoints)
- [Docker Deployment](#docker-deployment)
- [Configuration](#configuration)
- [License](#license)

## 🎯 Overview

This project implements a complete end-to-end machine learning workflow for predicting wine quality scores. It uses the Wine Quality dataset and employs an ElasticNet regression model to predict quality ratings based on 11 physicochemical features.

### Input Features

| Feature | Description |
|---------|-------------|
| Fixed Acidity | Tartaric acid content (g/dm³) |
| Volatile Acidity | Acetic acid content (g/dm³) |
| Citric Acid | Citric acid content (g/dm³) |
| Residual Sugar | Remaining sugar after fermentation (g/dm³) |
| Chlorides | Sodium chloride content (g/dm³) |
| Free Sulfur Dioxide | Free SO₂ content (mg/dm³) |
| Total Sulfur Dioxide | Total SO₂ content (mg/dm³) |
| Density | Density of wine (g/cm³) |
| pH | pH level |
| Sulphates | Potassium sulphate content (g/dm³) |
| Alcohol | Alcohol percentage (% vol) |

## ✨ Features

- **Modular Architecture**: Clean separation of components, entities, pipelines, and utilities
- **Configuration-Driven**: YAML-based configuration for easy customization
- **Automated Pipelines**: End-to-end training and prediction pipelines
- **Data Validation**: Schema-based validation to ensure data quality
- **Flask Web App**: User-friendly web interface for predictions
- **Docker Support**: Containerized deployment for consistency
- **Logging**: Comprehensive logging for debugging and monitoring
- **Research Notebooks**: Jupyter notebooks for experimentation

## 📁 Project Structure

```
End-to-End-ML-Project/
│
├── app.py                     # Flask web application
├── main.py                    # Training pipeline orchestrator
├── Dockerfile                 # Docker configuration
├── requirements.txt           # Python dependencies
├── setup.py                   # Package setup
├── params.yaml                # Model hyperparameters
├── schema.yaml                # Data schema definition
│
├── config/
│   └── config.yaml            # Pipeline configurations
│
├── src/
│   ├── components/            # Core ML components
│   │   ├── data_ingestion.py
│   │   ├── data_validation.py
│   │   ├── data_transformation.py
│   │   ├── model_trainer.py
│   │   └── model_evaluation.py
│   │
│   ├── pipelines/             # Training & prediction pipelines
│   │   ├── data_ingestion_pipeline.py
│   │   ├── data_validation_pipeline.py
│   │   ├── data_transformation_pipeline.py
│   │   ├── model_trainer_pipeline.py
│   │   ├── model_evaluation_pipeline.py
│   │   └── prediction_pipeline.py
│   │
│   ├── config/                # Configuration management
│   │   └── configuration.py
│   │
│   ├── entities/              # Data classes & entities
│   │   └── config_entity.py
│   │
│   ├── utils/                 # Utility functions
│   │   └── common.py
│   │
│   ├── logging/               # Logging configuration
│   │   └── __init__.py
│   │
│   └── constants/             # Project constants
│       └── __init__.py
│
├── artifacts/                 # Generated artifacts
│   ├── data_ingestion/        # Downloaded & extracted data
│   ├── data_validation/       # Validation status
│   ├── data_transformation/   # Train/test splits
│   ├── model_trainer/         # Trained model
│   └── model_evaluation/      # Evaluation metrics
│
├── research/                  # Jupyter notebooks for experimentation
│   ├── 01_data_ingestion.ipynb
│   ├── 02_data_validation.ipynb
│   ├── 03_data_transformation.ipynb
│   ├── 04_model_trainer.ipynb
│   └── 05_model_evaluation.ipynb
│
├── templates/                 # HTML templates for Flask
│   ├── index.html
│   └── results.html
│
└── logs/                      # Application logs
```

## 🚀 Installation

### Prerequisites

- Python 3.10 or higher
- pip (Python package manager)
- Git

### Step 1: Clone the Repository

```bash
git clone https://github.com/LochanaLithira/End-to-End-ML-Project.git
cd End-to-End-ML-Project
```

### Step 2: Create Virtual Environment

```bash
# Create virtual environment
python -m venv venv

# Activate virtual environment
# On Windows:
.\venv\Scripts\activate

# On macOS/Linux:
source venv/bin/activate
```

### Step 3: Install Dependencies

```bash
pip install -r requirements.txt
```

## 💻 Usage

### Training the Model

Run the complete training pipeline:

```bash
python main.py
```

This executes all pipeline stages:
1. Data Ingestion
2. Data Validation
3. Data Transformation
4. Model Training
5. Model Evaluation

### Starting the Web Application

```bash
python app.py
```

The application will be available at `http://localhost:5000`

### Making Predictions via Web Interface

1. Navigate to `http://localhost:5000`
2. Enter the wine's physicochemical properties
3. Click "Predict" to get the quality prediction

## 🔄 ML Pipeline Stages

### 1. Data Ingestion
- Downloads the Wine Quality dataset from the source URL
- Extracts the ZIP file to the artifacts directory
- Saves raw data for subsequent processing

### 2. Data Validation
- Validates the dataset schema against predefined columns
- Checks data types and column presence
- Generates validation status report

### 3. Data Transformation
- Removes unnecessary columns (Id)
- Splits data into training (80%) and testing (20%) sets
- Saves processed datasets as CSV files

### 4. Model Training
- Trains an ElasticNet regression model
- Uses hyperparameters from `params.yaml`
- Saves the trained model using joblib

### 5. Model Evaluation
- Evaluates model performance on test data
- Calculates metrics: RMSE, MAE, R² Score
- Saves metrics to JSON file

## 🤖 Model Details

### Algorithm: ElasticNet Regression

ElasticNet combines L1 (Lasso) and L2 (Ridge) regularization, providing a balance between feature selection and coefficient shrinkage.

### Hyperparameters

| Parameter | Value | Description |
|-----------|-------|-------------|
| alpha | 0.2 | Regularization strength |
| l1_ratio | 0.1 | Mix ratio between L1 and L2 |
| random_state | 42 | Random seed for reproducibility |

### Model Performance

| Metric | Value |
|--------|-------|
| RMSE | 0.622 |
| MAE | 0.494 |
| R² Score | 0.305 |

## 🌐 API Endpoints

| Endpoint | Method | Description |
|----------|--------|-------------|
| `/` | GET | Home page with prediction form |
| `/train` | GET | Trigger model training |
| `/predict` | POST | Submit features for prediction |

## 🐳 Docker Deployment

### Build the Docker Image

```bash
docker build -t wine-quality-prediction .
```

### Run the Container

```bash
docker run -p 5000:5000 wine-quality-prediction
```

Access the application at `http://localhost:5000`

## ⚙️ Configuration

### config/config.yaml
Contains paths and configurations for all pipeline stages:
- Data ingestion URLs and directories
- Data validation paths
- Model training and evaluation paths

### params.yaml
Contains model hyperparameters:
```yaml
ElasticNet:
  alpha: 0.2
  l1_ratio: 0.1
  random_state: 42
```

### schema.yaml
Defines the expected data schema:
- Column names and data types
- Target column specification

## 📊 Research Notebooks

The `research/` directory contains Jupyter notebooks for each pipeline stage:

| Notebook | Description |
|----------|-------------|
| `01_data_ingestion.ipynb` | Data downloading and extraction |
| `02_data_validation.ipynb` | Schema validation experiments |
| `03_data_transformation.ipynb` | Data preprocessing and splitting |
| `04_model_trainer.ipynb` | Model training experiments |
| `05_model_evaluation.ipynb` | Model evaluation and metrics |
| `experiments.ipynb` | General experimentation |

## 🤝 Contributing

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 👤 Author

**LochanaLithira**

---

<p align="center">
  Made with ❤️ for Machine Learning Engineering
</p>
