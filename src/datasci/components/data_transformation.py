import os

import pandas as pd
from sklearn.model_selection import train_test_split

from src.datasci import logger
from src.datasci.entity.config_entity import DataTransformationConfig


class DataTransformation:
    def __init__(self,config:DataTransformationConfig):
        self.config=config  
    
    def train_test_spliting(self):
        df=pd.read_csv(self.config.data_path)
        
        train_set,test_set=train_test_split(df,test_size=0.2,random_state=42)
        
        
        train_set.to_csv(os.path.join(self.config.root_dir,"train.csv"),index=False)
        test_set.to_csv(os.path.join(self.config.root_dir,"test.csv"),index=False)
        
        logger.info("Splitted data into training and test sets")
        logger.info(train_set.shape)
        logger.info(test_set.shape)
        
        
        