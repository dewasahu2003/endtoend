import os
from pathlib import Path

import joblib
import numpy as np
import pandas as pd

from src.datasci.constants import CONFIG_FILE_PATH
from src.datasci.utils.common import read_yaml


class PredictionPipeline:
    def __init__(self):
        self.config = read_yaml(CONFIG_FILE_PATH).model_trainer
        self.model_path = os.path.join(self.config.root_dir, self.config.model_name)
        self.model = joblib.load(self.model_path)

    def predict(self, data):
        prediction = self.model.predict(data)
        return prediction