import joblib
import pandas as pd

pipeline = joblib.load("models/pipeline.pkl")
expected_cols = joblib.load("models/columns.pkl")


def predict_risk(input_data):
    df = pd.DataFrame([input_data])

    # Apply same preprocessing as training
    df["department"] = pd.Categorical(
        df["department"], categories=["General Ward", "ICU", "Emergency", "Surgery"]
    )
    df["shift_type"] = pd.Categorical(df["shift_type"], categories=["Day", "Night"])

    df = pd.get_dummies(df, columns=["department", "shift_type"], drop_first=True)

    # # Add missing columns
    # for col in expected_cols:
    #     if col not in df.columns:
    #         df[col] = 0

    # # Ensure correct order
    # df = df[expected_cols]

    # # Scale
    # scaled = scaler.transform(df)

    # Align columns with training
    df = df.reindex(columns=expected_cols, fill_value=0)

    return pipeline.predict_proba(df)[0][1]
