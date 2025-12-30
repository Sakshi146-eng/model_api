from fastapi import FastAPI
from sklearn.preprocessing import StandardScaler
import joblib
import pandas as pd
import numpy as np
from models import ModelInput

app = FastAPI()

scaler=joblib.load('../models/scaler.pkl','rb')
model=joblib.load('../models/ridge.pkl','rb')



@app.get("/")
async def root():
    return {"message":"Welcome to Forest Fire Prediction API"}

@app.post("/predict")
async def predict_data(data: ModelInput):
    input_data=np.array([[data.Temperature, data.RH, data.Ws, data.Rain, data.FFMC, data.DMC, data.ISI, data.Classes, data.Region]])
    scaled_input=scaler.transform(input_data)
    prediction=model.predict(scaled_input)

    return{"Prediction": float(prediction[0])}
