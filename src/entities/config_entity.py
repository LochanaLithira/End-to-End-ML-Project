#Import necessary libraries
from dataclasses import dataclass
from pathlib import Path

#Configuration class for data ingestion
@dataclass(frozen=True)  #frozen makes the instance immutable
class DataIngestionConfig:
    root_dir: Path
    source_URL: str
    local_data_file: Path
    unzip_dir: Path

#Configuration class for Data Validation component
@dataclass(frozen=True)
class DataValidationConfig:
    root_dir: Path
    unzip_data_dir: Path
    status_file: str
    all_schema: dict  #Schema for data validation (schema.yaml) -> Need to read the schema file

#Configuration class for Data Transformation component
@dataclass(frozen = True)
class DataTransformationConfig:
    root_dir: Path
    data_path: Path   

#Configuration class for model trainer component
@dataclass(frozen=True)
class ModelTrainerConfig:
    root_dir: Path
    train_data_path: Path
    test_data_path: Path
    model_name: str
    alpha: float
    l1_ratio: float
    random_state: int
    target_column: str