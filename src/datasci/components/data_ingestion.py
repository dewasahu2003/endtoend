import os
import urllib.request as req
from src.datasci import logger
import zipfile
from src.datasci.entity.config_entity import DataIngestionCofig


#component
class DataIngestion:
    def __init__(self,config:DataIngestionCofig) -> None:
        self.config = config
    
    #download the file
    def download_file(self):
        if not os.path.exists(self.config.local_data_file):
            filename,headers =  req.urlretrieve(
                url=self.config.source_URL,
                filename=self.config.local_data_file
            )
            logger.info(f"{filename} download! with following info: \n{headers}")
        else:
                logger.info(f"file already exists of size")
           
    def extract_zip_file(self):
        """
        
        Extracts the zip file into the data directory
        Function returns None
        """
        unzip_path = self.config.unzip_dir
        os.makedirs(unzip_path, exist_ok=True)
        with zipfile.ZipFile(self.config.local_data_file, 'r') as zip_ref:
            zip_ref.extractall(unzip_path)


