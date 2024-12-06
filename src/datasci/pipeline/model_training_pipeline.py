from src.datasci import logger
from src.datasci.components.model_trainer import ModelTraining
from src.datasci.config.configuration import ConfiguratonManager

STAGE_NAME = "Model Training stage"

class ModelTrainingPipeline:
    def __init__(self):
        pass

    def initiate_model_training(self):
        try:
            config = ConfiguratonManager()
            model_trainer_config = config.get_trainer_config()
            model_trainer_config = ModelTraining(config=model_trainer_config)
            model_trainer_config.train()
        except Exception as e:
            raise e

if __name__=="__main__":
    try:
        logger.info(f">>>>>> stage {STAGE_NAME} started <<<<<<")
        obj = ModelTrainingPipeline()
        obj.initiate_model_training()
        logger.info(f">>>>>> stage {STAGE_NAME} completed <<<<<<\n\nx==========x")
    except Exception as e:
        logger.exception(e)
        raise e
