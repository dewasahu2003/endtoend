import os

import numpy as np
import pandas as pd
from flask import Flask, render_template, request

from src.datasci import logger
from src.datasci.pipeline.prediction_pipeline import PredictionPipeline

app = Flask(__name__)

@app.route('/',methods=['GET']) #for homepage
def homePage():
    return render_template('index.html')


@app.route('/train',methods=['GET']) #for training the model
def training():
    os.system("python main.py")
    logger.info("Training Successful! From FrontEnd")
    return "Training Successful!"

@app.route('/predict',methods=['GET','POST'])
def predict():
    if request.method == 'GET':
        return render_template('index.html')
    else:
        try:
            fixed_acidity = float(request.form['fixed_acidity'])
            volatile_acidity = float(request.form['volatile_acidity'])
            citric_acid = float(request.form['citric_acid'])
            residual_sugar = float(request.form['residual_sugar'])
            chlorides = float(request.form['chlorides'])
            free_sulfur_dioxide = float(request.form['free_sulfur_dioxide'])
            total_sulfur_dioxide = float(request.form['total_sulfur_dioxide'])
            density = float(request.form['density'])
            pH = float(request.form['pH'])
            sulphates = float(request.form['sulphates'])
            alcohol = float(request.form['alcohol'])
            
            data = [fixed_acidity,volatile_acidity,citric_acid,residual_sugar,chlorides,free_sulfur_dioxide,total_sulfur_dioxide,density,pH,sulphates,alcohol]
            data = np.array(data).reshape(1,11)
            
            obj = PredictionPipeline()
            predict = obj.predict(data)
            
            return render_template("result.html",prediction=str(predict))
        except Exception as e:
            logger.info(str(e))
            raise e
        


if __name__=="__main__":
    app.run(host='0.0.0.0',port=8080,debug=True)
    