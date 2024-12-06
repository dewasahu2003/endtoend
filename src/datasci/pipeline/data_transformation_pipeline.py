from src.datasci import logger
from src.datasci.components.data_transformation import DataTransformation
from src.datasci.config.configuration import ConfiguratonManager

STAGE_NAME = "Data Transformation stage"


class DataTransformationPipeline:
    def __init__(self):
        pass

    def initiate_data_transformation(self):
        try:
            config = ConfiguratonManager()
            data_transformation_config = config.get_data_transformation_config()
            data_transformation = DataTransformation(config=data_transformation_config)
            data_transformation.train_test_spliting()
        except Exception as e:
            raise e
        
if __name__ == "__main__":
    try:
        logger.info(f">>>>>> stage {STAGE_NAME} started <<<<<<")
        obj = DataTransformationPipeline()
        obj.initiate_data_transformation()
        logger.info(f">>>>>> stage {STAGE_NAME} completed <<<<<<\n\nx==========x")
    except Exception as e:
        logger.exception(e)
        raise e

