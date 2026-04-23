import streamlit as st
import pandas as pd
import joblib
import plotly.express as px
from styles import global_styles

global_styles()


def show_dashboard():
    st.title("PulseInsight Safety Command Center")
    st.caption("Real-time predictive monitoring across operational units.")

    df = pd.read_csv("Datasets/Final_Merged_Dataset/operational_risk_dataset.csv")
    pipeline = joblib.load("models/pipeline.pkl")
    expected_cols = joblib.load("models/columns.pkl")
    anomaly_model = joblib.load("models/anomaly_model.pkl")

    X = df.drop("target", axis=1)
    X = pd.get_dummies(X, drop_first=True)

    X = X.reindex(columns=expected_cols, fill_value=0)

    df["predicted_risk"] = pipeline.predict_proba(X)[:, 1]
    df["anomaly"] = anomaly_model.predict(X)

    # KPIs
    col1, col2, col3 = st.columns(3)

    col1.metric(
        "Overall Risk Index",
        f"{df['predicted_risk'].mean() * 100:.2f}%",
        "Above recommended safety threshold.",
    )

    col2.metric(
        "High Risk Units",
        int((df["predicted_risk"] > 0.7).sum()),
        "Requires review within 24 hours.",
    )

    col3.metric(
        "Active Predictive Alerts",
        int(((df["predicted_risk"] > 0.5) & (df["predicted_risk"] <= 0.7)).sum()),
        "Immediate action recommended.",
    )

    st.markdown("---")

    st.subheader("Risk Trend")
    fig = px.line(
        df.head(50),
        y="predicted_risk",
        labels={"index": "Index", "predicted_risk": "Predicted Risk"},
    )

    st.plotly_chart(fig)

    st.markdown("---")

    st.subheader("Sample Data")
    st.dataframe(df.head(10))

    st.subheader("Anomalies Detected")
    st.dataframe(df[df["anomaly"] == -1])
