from fastapi import APIRouter
import joblib
import pandas as pd
from src.rating_engine.model.input_schema import PremiumPredict
from src.config import CATEGORICAL_COLUMNS

router = APIRouter()

# load model once
model = joblib.load("model/model.joblib")

@router.post("/predict")
def premium_prediction(input_data: PremiumPredict):
    # convert input to DataFrame
    df = pd.DataFrame([dict(input_data)])
    
    # convert categorical columns to category dtype (must match training data)
    for col in CATEGORICAL_COLUMNS:
        if col in df.columns:
            df[col] = df[col].astype("category")

    # predict
    prediction = model.predict(df)

    return {"predicted_premium": float(prediction[0])}
