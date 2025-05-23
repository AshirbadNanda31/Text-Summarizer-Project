from textSummarizer.config.configuration import ConfigurationManager
from textSummarizer.components.data_ingestion import DataInjestion
from textSummarizer.logging import logger


class DataIngestionTrainingPipeline:
    def __init__(self):
        pass
    
    def main(self):
        config = ConfigurationManager()
        data_ingestion_config = config.get_data_ingestion_config()
        data_ingestion = DataInjestion(config=data_ingestion_config)
        data_ingestion.download_file()
        data_ingestion.extract_zip_file()