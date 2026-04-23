from fastapi import FastAPI
import joblib
import pandas as pd

app = FastAPI()

pipeline = joblib.load("models/pipeline.pkl")
columns = joblib.load("models/columns.pkl")


@app.post("/predict")
def predict(data: dict):
    df = pd.DataFrame([data])
    df = pd.get_dummies(df)
    df = df.reindex(columns=columns, fill_value=0)

    risk = pipeline.predict_proba(df)[0][1]

    return {
        "risk_score": float(risk),
        "risk_level": ("High" if risk > 0.7 else "Moderate" if risk > 0.5 else "Low"),
    }


@app.get("/")
def home():
    return {"status": "PulseInsight API running",
            "docs": "/docs"}
