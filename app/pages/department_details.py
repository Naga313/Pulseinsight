import streamlit as st
import pandas as pd
import shap
import joblib
import matplotlib.pyplot as plt
from styles import global_styles

global_styles()


def show_details():
    st.title("ICU Department Details")

    df = pd.read_csv("Datasets/Final_Merged_Dataset/operational_risk_dataset.csv")
    pipeline = joblib.load("models/pipeline.pkl")
    expected_cols = joblib.load("models/columns.pkl")

    X = df.drop("target", axis=1)
    X = pd.get_dummies(X, drop_first=True)

    X = X.reindex(columns=expected_cols, fill_value=0)

    index = st.slider("Select Record", 0, len(df) - 1, 0)

    st.subheader("Selected Record (Processed Features)")
    st.write(X.iloc[index])

    # Extract XGBoost model from pipeline
    model = pipeline.named_steps["model"]

    explainer = shap.TreeExplainer(model)
    shap_values = explainer.shap_values(X)

    shap_val = shap_values[index]

    importance_df = pd.DataFrame(
        {"Feature": X.columns, "Impact": shap_val}
    ).sort_values(by="Impact", ascending=False)

    st.subheader("Top Risk Drivers")
    st.dataframe(importance_df.head(5))

    st.subheader("SHAP Breakdown")

    fig, ax = plt.subplots(figsize=(8, 5))
    shap.plots._waterfall.waterfall_legacy(
        explainer.expected_value, shap_val, feature_names=X.columns
    )

    st.pyplot(fig)

    st.info("These features contribute most to the predicted risk.")
