# Pulseinsight
AI-Based Early Warning System for Preventing Serious Safety Events

## Problem Statement
Current safety monitoring systems are mostly reactive incidents are analyzed only after they occur. There is a lack of predictive and explainable systems that can identify high-risk situations early and support timely interventions.

## Proposed Solution
PulseInsight is an early warning analytics system that predicts the risk of serious safety events in advance and explains the key factors driving that risk.  It provides a web-based analytical platform that:
1. Displays real-time risk scores for operational units.
2. Highlights key contributing risk factors.
3. Enables what-if scenario simulation.
4. Supports data-driven safety decision-making.

## System Architecture
1. Design & Prototyping: Figma.
2. Frontend: Streamlit (Interactive Dashboard).
3. Backend: Python (ML Models + FastAPI).
4. Machine Learning: XGBoost Classifier.
5. Explainability: SHAP (Feature Importance).
6. Data Sources: CSV / Structured datasets.
  Datasets:
    1. HCAI - California Department of Health Care Access and Information - Hospital Staffing, 2009-2013 - https://data.chhs.ca.gov/dataset/hospital-staffing-2009-2013
    2. Kaggle - mimic-iv-clinical-database-demo-2.2 - https://www.kaggle.com/datasets/montassarba/mimic-iv-clinical-database-demo-2-2

7. Deployment: Localhost (extendable to cloud).

## Features
1. Dashboard
   Overall risk index monitoring.
   Department-level risk tracking.
   Trend visualization.
2. Alerts System
   Low / Medium / High risk classification.
   Automated alert generation.
3. Explainability Module
   SHAP-based feature importance.
    Top risk-driving factors visualization.
4. Scenario Simulation
   What-if analysis for operational decisions.
    Risk comparison between current vs modified conditions.
5. API Layer
   FastAPI endpoint for external predictions.
    JSON-based risk scoring system.

## Output
The system provides:
1. Risk classification (Low / Medium / High) 
2. Explanation of contributing factors 
3. Preventive insights for risk reduction 
4. Trend visualization over time

## User Journey
Login → Dashboard → Department View → Simulation → Alerts → Profile → Logout
Flow includes:
1. Authentication
2. Real-time monitoring
3.  Drill-down analysis
4. What-if simulation
5.  Alert handling

## API Example
1. FastAPI Request (Input)
{
  "department": "ICU",
  "staffing_ratio": 0.8,
  "workload_index": 70,
  "overtime_hours": 10,
  "equipment_availability": 0.85,
  "incident_last_7_days": 3,
  "shift_type": "Day",
  "patient_acuity": 3,
  "avg_response_time": 10,
  "bed_occupancy_rate": 0.85
}
2. Response (Output)
{
  "risk_score": 0.82,
  "risk_level": "High"
}

## Installation
1. Clone repository
   git https://github.com/Naga313/Pulseinsight
   cd Pulseinsight
2. Install dependencies
   pip install -r requirements.txt
3. Run the Project
   python src/train_model.py
4. Start Streamlit App
   streamlit run app/app.py
5. Start FastAPI Backend
   uvicorn api.main:app --reload

## Key Insights
1. Early prediction of operational risks improves intervention timing.
2.  Explainable AI builds trust in healthcare decision systems.
3. Scenario simulation supports proactive decision-making.

## Tech Stack
1. Figma.
2. Python.
3. Streamlit.
4. FastAPI.
5. XGBoost.
6. SHAP.
7. Pandas.
8. NumPy.
9. Matplotlib.
10. Plotly.

## Future Improvements
1. Cloud deployment (AWS / Azure).
2.  Role-based authentication.
3. Real-time database integration Live hospital data streaming.
4. Mobile dashboard support.

## Author: NAGA SAI SRAVAB REDROWTHU
PulseInsight - Predict. Protect. Prevent.
University of Massachusetts of Dartmouth
Under the guidance of Prof.Long Jiao
Master’s Project Spring 2026 - Healthcare AI Risk Prediction System
