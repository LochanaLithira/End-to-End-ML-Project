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