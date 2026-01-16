#Import necessary libraries and modules
import os
from box.exceptions import BoxValueError
import yaml
import json
import joblib
from src.logging import logger
from ensure import ensure_annotations  #type checking
from box import ConfigBox
from pathlib import Path
from typing import Any

#Function to read a YAML file and return its contents as a ConfigBox
@ensure_annotations
def read_yaml(path_to_yaml: Path) -> ConfigBox:
    try:
        with open(path_to_yaml, 'r') as yaml_file:
            content = yaml.safe_load(yaml_file)
            logger.info(f"YAML file: {path_to_yaml} loaded successfully")
            return ConfigBox(content)
    except BoxValueError as e:
        raise BoxValueError(f"Error while converting YAML to ConfigBox: {e}")
    except Exception as e:
        raise e
    
#Function to create directories if they do not exist
def create_directories(path_to_directories: list, verbose=True) -> None:
    for path in path_to_directories:
        os.makedirs(path, exist_ok=True)
        if verbose:
            logger.info(f"Directory created at: {path}")

#Function to create a JSON file from a dictionary
def create_json(path: Path, data: dict) -> None:
    with open(path, 'w') as json_file:
        json.dump(data, json_file, indent=4)
    logger.info(f"JSON file created at: {path}")

#Function to load a JSON file and return its contents as a ConfigBox
@ensure_annotations
def load_json(path: Path) -> ConfigBox:
    with open(path, 'r') as json_file:
        content = json.load(json_file)
    logger.info(f"JSON file: {path} loaded successfully")
    return ConfigBox(content)

#Function to save data in binary format using joblib
def save_bin(path: Path, data:Any) -> None:
    joblib.dump(value = data, filename = path)
    logger.info(f"Binary file saved at: {path}")

#Function to load data from a binary file using joblib
def load_bin(path: Path) -> Any:
    data = joblib.load(filename = path)
    logger.info(f"Binary file loaded from: {path}")
    return data

#Function to get the size of a file in KB
@ensure_annotations
def get_size(path: Path) -> str:
    size_in_kb = round(os.path.getsize(path) / 1024, 2)
    return f"{size_in_kb} KB"