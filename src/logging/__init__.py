#import necessary modules
import os
import sys
import logging

#Define the logging format string
logging_str = "[%(asctime)s: %(levelname)s: %(module)s]: %(message)s"

#Create log directory and file path
log_dir ="logs"
log_filepath=os.path.join(log_dir, "logs.log")
os.makedirs(log_dir, exist_ok=True)

#Configure logging settings
logging.basicConfig(
    level=logging.INFO,  #Set the logging level to INFO
    format=logging_str,  #Use the defined logging format
    handlers=[
        logging.FileHandler(log_filepath),  #Log messages to the specified file
        logging.StreamHandler(sys.stdout)  #Log messages to standard output
    ]
)

#Create a logger instance
logger = logging.getLogger("app_logger")


