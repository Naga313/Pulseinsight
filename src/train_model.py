import pandas as pd
import joblib
from sklearn.model_selection import train_test_split
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import StandardScaler
from sklearn.metrics import roc_auc_score, classification_report
from sklearn.ensemble import IsolationForest
from xgboost import XGBClassifier

# Load dataset
df = pd.read_csv("Datasets/Final_Merged_Dataset/operational_risk_dataset.csv")

# Split features & target
X = df.drop("target", axis=1)
y = df["target"]

# One-hot encoding
X = pd.get_dummies(X, drop_first=True)

columns = X.columns.tolist()

# Train-test split
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42, stratify=y
)

iso = IsolationForest(contamination=0.05, random_state=42)
iso.fit(X)

# Create pipeline (scaling + model together)
pipeline = Pipeline(
    [("scaler", StandardScaler()), ("model", XGBClassifier(eval_metric="logloss"))]
)

# Train
pipeline.fit(X_train, y_train)

# Predictions
y_pred = pipeline.predict(X_test)
y_prob = pipeline.predict_proba(X_test)[:, 1]

# Evaluation
print("ROC-AUC:", roc_auc_score(y_test, y_prob))
print(classification_report(y_test, y_pred))

# Save model + scaler
joblib.dump(pipeline, "models/pipeline.pkl")
joblib.dump(columns, "models/columns.pkl")
joblib.dump(iso, "models/anomaly_model.pkl")

print("Model and scaler saved in /models folder")
