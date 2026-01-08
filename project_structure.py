import os
from pathlib import Path
import logging

#Display the timestamp and the messages in the logs
logging.basicConfig(level=logging.INFO, format='[%(asctime)s]: %(message)s:')

#Files and Floders to be created in the project structure
list_of_files = [
    "src/__init__.py",
    "src/components/__init__.py",
    "src/utils/__init__.py",
    "src/utils/common.py",
    "src/config/__init__.py",
    "src/config/configuration.py",
    "src/pipelines/__init__.py",
    "src/entities/__init__.py",
    "src/entities/config_entity.py",
    "src/constants/__init__.py",
    "config/config.yaml",
    "params.yaml",
    "schema.yaml",
    "main.py",
    "app.py",
    "requirements.txt",
    "setup.py",
    "research/trials.ipynb",
    "templates/index.html"
]

#Logic to create the files and folders

for filepath in list_of_files:
    filepath = Path(filepath) #Convert the filepath string to a Path object

    #Split the filepath into directory and filename
    filedir, filename = os.path.split(filepath)

    #Create the directory if it does not exist
    if filedir != "":
        os.makedirs(filedir, exist_ok=True)
        logging.info(f"Created directory: {filedir} for file: {filename}")  #Display log message for directory creation

    #Create the file if it does not exist or is empty
    if (not os.path.exists(filepath)) or (os.path.getsize(filepath) == 0): #Check if file does not exist or is empty
        with open(filepath, "w") as f:  #Create an empty file
            pass
        logging.info(f"Created file: {filepath}")   #Display log message for file creation
    else:
        logging.info(f"File already exists: {filepath}")  #Display log message if file already exists
