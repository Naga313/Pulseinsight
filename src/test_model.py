import joblib
import pandas as pd

model = joblib.load("models/model.pkl")
scaler = joblib.load("models/scaler.pkl")
columns = joblib.load("models/columns.pkl")

df = pd.read_csv("Datasets/Final_Merged_Dataset/operational_risk_dataset.csv")

X = df.drop("target", axis=1)

sample = X.iloc[0:1]

sample_scaled = scaler.transform(sample)

prediction = model.predict_proba(sample_scaled)[0][1]

print("Sample Risk Prediction:", prediction)