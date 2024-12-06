from src.datasci.constants import (CONFIG_FILE_PATH, PARAMS_FILE_PATH,
                                   SCHEMA_FILE_PATH)
from src.datasci.entity.config_entity import DataIngestionCofig
from src.datasci.utils.common import create_directories, read_yaml


class ConfiguratonManager:
    def __init__(self,
                 config_file_path=CONFIG_FILE_PATH,
                 params_file_path=PARAMS_FILE_PATH,
                 schema_file_path=SCHEMA_FILE_PATH
                 ):
        self.config = read_yaml(config_file_path)
        self.params = read_yaml(params_file_path)
        self.schema = read_yaml(schema_file_path)
        create_directories([self.config.artifacts_root])
    
    def get_data_ingestion_config(self)-> DataIngestionCofig:
        config = self.config.data_ingestion #from yaml
        create_directories([config.root_dir])
        data_ingestion_config = DataIngestionCofig(
            root_dir=config.root_dir,
            source_URL=config.source_URL,
            local_data_file=config.local_data_file,
            unzip_dir=config.unzip_dir
        )
        return data_ingestion_config