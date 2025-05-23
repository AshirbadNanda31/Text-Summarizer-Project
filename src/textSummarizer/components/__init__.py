import os
import urllib.request as request
import zipfile
from textSummarizer.logging import logger
from textSummarizer.utils.common import get_size
from pathlib import Path
from textSummarizer.entity import DataInjestionConfig



class DataInjestion:
    def __init__(self, config: DataInjestionConfig):
        self.config = config

    def download_file(self):
        if not os.path.exists(self.config.local_data_file):
           filename, headers = request.urlretrieve(
               url = self.config.source_URL,
               filename = self.config.local_data_file
           )
           logger.info(f"{filename} downloaded with following info: \n{headers}")
        else:
            logger.info(f"File already exists with size: {get_size(Path(self.config.local_data_file))}")
            
            
    def extract_zip_file(self):
        """
        zip_file_path: str
        Extracts the zip file into the directory
        Function returns None
        """
        unzip_path = self.config.unzip_dir
        os.makedirs(unzip_path, exist_ok=True)
        with zipfile.ZipFile(self.config.local_data_file, 'r') as zip_ref:
            zip_ref.extractall(unzip_path)