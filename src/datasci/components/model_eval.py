import os
from pathlib import Path
from urllib.parse import urlparse

import joblib
import mlflow as mf
import mlflow.sklearn as mfsk
import numpy as np
import pandas as pd
from sklearn.metrics import mean_absolute_error, mean_squared_error, r2_score

from src.datasci.entity.config_entity import ModelEvalConfig
from src.datasci.utils.common import save_json

os.environ["MLFLOW_TRACKING_URI"] = "https://dagshub.com/dewasahu2003/endtoend.mlflow"
os.environ["MLFLOW_TRACKING_USERNAME"] = "dewasahu2003"
os.environ["MLFLOW_TRACKING_PASSWORD"] = "6976e6dedfc675e1145823597f708aa2b40572a2"


class ModelEval:
    def __init__(self,config:ModelEvalConfig):
        self.config =  config
        
    
    def eval_metrics(self,actual,pred):
        rmse =  np.sqrt(mean_squared_error(actual,pred))
        mae = mean_absolute_error(actual,pred)
        r2 = r2_score(actual,pred)
        return rmse,mae,r2
    
    def log_into_mlflow(self):
        test_data = pd.read_csv(self.config.test_data_path)
        model = joblib.load(self.config.model_path)
        
        test_x = test_data.drop([self.config.target_column],axis=1)
        test_y = test_data[[self.config.target_column]]
        
        mf.set_registry_uri(self.config.mlflow_uri)
        tracking_url_type_store = urlparse(mf.get_tracking_uri()).scheme
        
        with mf.start_run():
            predicted_qualities = model.predict(test_x)
            (rmse,mae,r2) = self.eval_metrics(test_y,predicted_qualities)
            # Log parameter, metrics, and model to MLflow
            scores = {"rmse": rmse, "mae": mae, "r2": r2}
            save_json(path=Path(self.config.metric_file),data=scores)
            
            mf.log_params(self.config.all_params)
            mf.log_metrics(scores)
            
            if tracking_url_type_store != "file":
                #register the model
                mfsk.log_model(model, "model", registered_model_name="ElasticnetModel")
            else:
                mfsk.log_model(model, "model")
    