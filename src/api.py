from fastapi import FastAPI
from pydantic import BaseModel
from typing import List
from src.dream_predictor import predict_rem_probability

app = FastAPI(title="Dreamstate Cycle Predictor API")

class MovementData(BaseModel):
    movements: List[float]

@app.post("/predict")
def predict(data: MovementData):
    prob = predict_rem_probability(data.movements)
    return {"dreaming_probability": float(prob)}
