# Dreamstate Cycle Predictor

An ML framework to predict REM sleep and dreaming events using passive IoT motion streams.

## Usage
```bash
python examples/predict_dreams.py
```


## FastAPI API Service
The project includes a FastAPI server wrapper. 

### Running the API
```bash
uvicorn src.api:app --host 0.0.0.0 --port 8000
```
- **Interactive docs**: Navigate to `/docs` for swagger documentation.
- **POST `/predict`**: Input movements to classify sleep stage metrics.
