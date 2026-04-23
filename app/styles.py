import streamlit as st


def global_styles():
    st.markdown(
        """
    <style>

    # Fonts
    @import url('https://fonts.googleapis.com/css2?family=Montserrat:wght@500;600;700&family=Poppins:wght@300;400;500&display=swap');

    /* Global */
    html, body, [class*="css"]  {
        font-family: 'Poppins', sans-serif;
    }
                
    .title, h2 {
        font-family: 'Montserrat', sans-serif;
        font-size: 32px;
        font-weight: 700;
        color: #111827;
        margin-bottom: 5px;
        text-align: center;
    }
                
    p {
        font-family: 'Poppins', sans-serif;
        font-size: 16px;
    }

    .stApp {
        background-color: #F8FAFC;
    }

    /* Font styles */
    div[data-testid="stHeading"] h1 {
        font-family: 'Montserrat', sans-serif;
        font-size: 32px;
        font-weight: 700;
        color: #111827;
    }
    
    div[data-testid="stMarkdownContainer"] p {
        font-family: 'Poppins', sans-serif;
    }
                
    [data-testid="stMetricValue"] {
        font-family: 'Montserrat', sans-serif;
    }

    /* Sidebar */
    section[data-testid="stSidebar"] {
        background-color: #F8FAFC;
    }
    
    section[data-testid="stSidebar"] {
        font-family: 'Poppins', sans-serif;
    }
    
    section[data-testid="stSidebar"] [data-testid="stMarkdownContainer"] {
        font-family: 'Poppins', sans-serif;
    }
    
    input, textarea {
        font-family: 'Poppins', sans-serif;
    }
                
    section[data-testid="stSidebar"] * {
        color: #F8FAFC;
    }

    /* Sidebar title */
    section[data-testid="stSidebar"] h1 {
        color: #F8FAFC;
        font-size: 20px;
    }

    /* Buttons */
    .stButton button {
        background-color: #2563EB;
        color: white;
        border-radius: 10px;
        padding: 10px 20px;
        font-weight: 600;
        border: none;
        transition: 0.2s ease;
    }

    .stButton button:hover {
        background-color: #1E40AF;
        transform: translateY(-1px);
    }

    /* Logout button (top right) */
    .logout-btn button {
        background-color: #EF4444 !important;
        color: white !important;
        border-radius: 10px;
        padding: 8px 16px;
        font-weight: 600;
    }

    .logout-btn button:hover {
        background-color: #DC2626 !important;
    }

    /* Inputs */
    .stTextInput input {
        border-radius: 10px;
        padding: 10px;
        border: 1px solid #D1D5DB;
    }

    /* KPI's */
    .metric-card {
        background: #FFFFFF;
        padding: 20px;
        border-radius: 16px;
        border: 1px solid #E5E7EB;
        box-shadow: 0px 4px 12px rgba(0,0,0,0.05);
    }

    /* Alerts */
    .stAlert {
        border-radius: 12px;
    }

    /* DataFrames */
    .stDataFrame {
        border-radius: 12px;
        overflow: hidden;
    }

    .block-container {
        padding-top: 2rem;
        padding-left: 2rem;
        padding-right: 2rem;
    }
                
    h2, p {
        font-family: 'Poppins', sans-serif;
    }
                
    /* Page background */
    .stApp {
        background-color: #F8FAFC;
    }
                
    /* Center everything */
    .main-container {
        display: flex;
        flex-direction: column;
        align-items: center;
        justify-content: center;
    }

    .subtitle {
        font-family: 'Montserrat', sans-serif;
        font-size: 24px;
        font-weight: 200;
        color: #111827;
        margin-bottom: 10px;
        text-align: center;
    }

    .tagline {
        font-family: 'Montserrat', sans-serif;
        font-size: 20px;
        font-weight: lighter;
        color: #111827;
        margin-bottom: 50px;
        text-align: center;
    }

    /* Card */
    div[data-testid="stVerticalBlock"]:has(#login-card):not(:has(div[data-testid="stVerticalBlock"] #login-card)) {
            max-width: 800px;
            margin: 0 auto;
            border: 2px solid #2c3e91;
            border-radius: 20px;
            padding: 45px;
            background: #F8FAFC;
            gap: 0.5rem;
            box-shadow: 0px 4px 12px rgba(0,0,0,0.1);
    }

    /* Inputs */
    .stTextInput > div > div > input {
        font-family: 'Poppins', sans-serif;
        border-radius: 10px;
        padding: 14px;
        border: 1px solid #d1d5db;
        font-size: 14px;
    }

    /* Button */
    .stButton > button {
        font-family: 'Poppins', sans-serif;
        background-color: #2c3e91;
        color: #F8FAFC;
        border-radius: 10px;
        padding: 10px 35px;
        font-weight: 800;
        border: none;
        margin: 25px 0px;
    }

    /* Row alignment */
    .row {
        display: flex;
        justify-content: space-between;
        align-items: center;
        margin-top: 15px;
    }

    .forgot-inline {
        color: #374151;
        font-size: 14px;
    }

    .forgot-bottom {
        margin-top: 25px;
        color: #374151;
        font-size: 14px;
        }
    </style>
    """,
        unsafe_allow_html=True,
    )
