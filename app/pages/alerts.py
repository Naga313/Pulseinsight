import streamlit as st
import pandas as pd
import joblib
from styles import global_styles

global_styles()


def show_alerts():
    st.title("Alert Component Variants")

    df = pd.read_csv("Datasets/Final_Merged_Dataset/operational_risk_dataset.csv")
    pipeline = joblib.load("models/pipeline.pkl")
    columns = joblib.load("models/columns.pkl")

    X = df.drop("target", axis=1)
    X = pd.get_dummies(X, drop_first=True)

    X = X.reindex(columns=columns, fill_value=0)

    df["risk"] = pipeline.predict_proba(X)[:, 1]

    st.subheader("Critical Alerts")

    for i, row in df[df["risk"] > 0.7].head(5).iterrows():
        st.error(f"Record {i} | Risk: {row['risk']:.2f}")

    st.subheader("Warnings")

    for i, row in df[(df["risk"] > 0.5) & (df["risk"] <= 0.7)].head(5).iterrows():
        st.warning(f"Record {i} | Risk: {row['risk']:.2f}")
