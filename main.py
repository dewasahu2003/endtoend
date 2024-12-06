from src.datasci import logger
from src.datasci.pipeline.data_ingestion_pipeline import DataIngestionPipeline

STAGE_NAME = "Data Ingestion stage"
if __name__ =="__main__":
    try:
        logger.info(f">>>>>> stage {STAGE_NAME} started <<<<<<")
        obj = DataIngestionPipeline()
        obj.initiate_data_ingestion()
        logger.info(f">>>>>> stage {STAGE_NAME} completed <<<<<<\n\nx==========x")
    except Exception as e:
        logger.exception(e)
        raise e
