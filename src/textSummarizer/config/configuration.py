from textSummarizer.constants import *
from textSummarizer.utils.common import read_yaml, create_directories
from textSummarizer.entity import (DataInjestionConfig)



from pathlib import Path  # Make sure this is imported if you're using Path objects

class ConfigurationManager:
    def __init__(self,
                 config_filepath=CONFIG_FILE_PATH,
                 params_filepath=PARAMS_FILE_PATH):
        # Convert to string before passing to read_yaml
        self.config = read_yaml(str(config_filepath))
        self.params = read_yaml(str(params_filepath))
        
        create_directories([self.config.artifacts_root])
                
    def get_data_ingestion_config(self) -> DataInjestionConfig:
        config = self.config.data_ingestion
        create_directories([config.root_dir])
        
        data_ingestion_config = DataInjestionConfig(
            root_dir = config.root_dir,
            source_URL = config.source_URL,
            local_data_file = Path(config.local_data_file),
            unzip_dir = Path(config.unzip_dir)
        )
        return data_ingestion_config