import streamlit as st
import numpy as np
import pandas as pd
import sys
import os
import plotly.express as px
from styles import global_styles

global_styles()

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "../../")))

from src.predict import predict_risk

df = pd.read_csv("Datasets/Final_Merged_Dataset/operational_risk_dataset.csv")


def show_simulation():
    col1, col2 = st.columns([3, 1])

    with col1:
        st.title("Scenario Simulation")

    with col2:
        if st.button("Reset"):
            st.rerun()

    default_input = {
        "department": "General Ward",
        "staffing_ratio": 0.8,
        "workload_index": 70,
        "overtime_hours": 10,
        "equipment_availability": 0.85,
        "incident_last_7_days": 3,
        "shift_type": 1,
        "patient_acuity": 3,
        "avg_response_time": 10,
        "bed_occupancy_rate": 0.85,
    }

    department = st.selectbox(
        "Department", ["General Ward", "ICU", "Emergency", "Surgery"]
    )
    shift_type = st.selectbox("Shift Type", ["Day", "Night"])
    patient_acuity = st.slider("Patient Acuity", 1, 5, 3)
    staffing = st.slider("Staffing Ratio", 0.5, 1.2, 0.8)
    workload = st.slider("Workload Index", 0, 100, 70)
    overtime = st.slider("Overtime Hours", 0, 30, 10)
    equipment = st.slider("Equipment Availability", 0.5, 1.0, 0.85)
    incidents = st.slider("Incidents (Last 7 Days)", 0, 20, 3)
    response_time = st.slider("Avg Response Time (mins)", 1, 60, 10)
    bed_occupancy = st.slider("Bed Occupancy Rate", 0.5, 1.0, 0.85)

    if st.button("Run Simulation"):

        user_input = {
            "department": department,
            "staffing_ratio": staffing,
            "workload_index": workload,
            "overtime_hours": overtime,
            "equipment_availability": equipment,
            "incident_last_7_days": incidents,
            "shift_type": shift_type,
            "patient_acuity": patient_acuity,
            "avg_response_time": response_time,
            "bed_occupancy_rate": bed_occupancy,
        }

        base_row = df.drop("target", axis=1).iloc[0].to_dict()
        default_input = base_row.copy()
        base = predict_risk(default_input)
        new = predict_risk(user_input)

        # simulate small risk trajectory
        steps = 20
        noise = np.random.normal(0, 0.02, steps)

        trend = [base]
        for i in range(1, steps):
            trend.append(min(1, max(0, trend[-1] + (new - base) / steps + noise[i])))

        chart_df = pd.DataFrame({"Step": list(range(steps)), "Risk": trend})

        st.subheader("Risk Evolution (Simulated)")

        fig = px.line(
            chart_df,
            x="Step",
            y="Risk",
            labels={"Step": "Simulation Step", "Risk": "Predicted Risk"},
        )

        fig.update_traces(line=dict(width=3))
        fig.update_layout(
            xaxis=dict(showgrid=True), yaxis=dict(showgrid=True, range=[0, 1])
        )

        st.plotly_chart(fig, use_container_width=True)

        st.metric("Current Risk", f"{base*100:.2f}%")
        st.metric("New Risk", f"{new*100:.2f}%")
        delta = (new - base) * 100
        st.metric("Risk Change", f"{new*100:.2f}%", f"{delta:.2f}%")

        if new > 0.8:
            st.error("High Risk")
        elif new > 0.5:
            st.warning("Moderate Risk")
        else:
            st.success("Low Risk")
