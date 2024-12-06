from src.datasci import logger
from src.datasci.components.data_validation import DataValidation
from src.datasci.config.configuration import ConfiguratonManager

STAGE_NAME = "Data Validation stage"

class DataValidationPipeline:
    def __init__(self):
        pass

    def initiate_data_valdiation(self):
        
        try:
            config = ConfiguratonManager()
            data_validation_config = config.get_data_validation_config()   
            data_validation = DataValidation(config=data_validation_config)
            data_validation.validate_all_columns()
          
        except Exception as e:
            raise e


if __name__ =="__main__":
    try:
        logger.info(f">>>>>> stage {STAGE_NAME} started <<<<<<")
        obj = DataValidationPipeline()
        obj.initiate_data_valdiation()
        logger.info(f">>>>>> stage {STAGE_NAME} completed <<<<<<\n\nx==========x")
    except Exception as e:
        logger.exception(e)
        raise e
