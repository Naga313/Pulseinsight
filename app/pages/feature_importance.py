import streamlit as st
import pandas as pd
import joblib
import shap
from styles import global_styles

global_styles()


def show_feature_importance():
    st.title("Feature Importance Dashboard")

    df = pd.read_csv("Datasets/Final_Merged_Dataset/operational_risk_dataset.csv")

    pipeline = joblib.load("models/pipeline.pkl")
    columns = joblib.load("models/columns.pkl")

    X = df.drop("target", axis=1)
    X = pd.get_dummies(X, drop_first=True)
    X = X.reindex(columns=columns, fill_value=0)

    model = pipeline.named_steps["model"]

    explainer = shap.TreeExplainer(model)
    shap_values = explainer.shap_values(X)

    importance = pd.DataFrame(
        {"Feature": X.columns, "Importance": abs(shap_values).mean(axis=0)}
    ).sort_values("Importance")

    st.bar_chart(importance.set_index("Feature").head(15))
