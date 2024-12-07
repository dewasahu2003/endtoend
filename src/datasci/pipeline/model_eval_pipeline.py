from src.datasci import logger
from src.datasci.components.model_eval import ModelEval
from src.datasci.config.configuration import ConfiguratonManager

STAGE_NAME = "Model Evaluation stage"   

class ModelEvaluationPipeline:
    def __init__(self):
        pass

    def initiate_evaluation(self):
        try:
            config = ConfiguratonManager()
            model_eval_config = config.get_model_eval_config()
            model_eval_config = ModelEval(config=model_eval_config)
            model_eval_config.log_into_mlflow()
        except Exception as e:
            raise e

if __name__=="__main__":
    try:
        logger.info(f">>>>>> stage {STAGE_NAME} started <<<<<<")
        obj = ModelEvaluationPipeline()
        obj.initiate_evaluation()
        logger.info(f">>>>>> stage {STAGE_NAME} completed <<<<<<\n\nx==========x")
    except Exception as e:
        logger.exception(e)
        raise e