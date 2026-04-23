import streamlit as st
from styles import global_styles

global_styles()

st.set_page_config(
    page_title="PulseInsight", page_icon="assets/Logo.png", layout="wide"
)

st.markdown(
    """
    <style>
        [data-testid="stSidebarNav"] {display: none;}
    </style>
""",
    unsafe_allow_html=True,
)

USERNAME = "jim.hopper@pulseinsight.com"
PASSWORD = "PULSEINSIGHT."

# Session State Initialization
if "logged_in" not in st.session_state:
    st.session_state.logged_in = False


# Log in and Log out Functions
def login():

    st.markdown(
        """
        <style>
                
        @import url('https://fonts.googleapis.com/css2?family=Montserrat:wght@500;600;700&family=Poppins:wght@300;400;500&display=swap');
                
        html, body, [class*="css"] {
            font-family: 'Poppins', sans-serif;
        }
        </style>
    """,
        unsafe_allow_html=True,
    )

    # Header
    st.markdown('<div class="main-container">', unsafe_allow_html=True)
    left, center, right = st.columns([1, 2, 1])

    with center:
        col1, col2 = st.columns([1, 2], vertical_alignment="center")

    with col1:
        st.image("assets/Logo.png", width=120)

    with col2:
        st.markdown('<div class="title">PulseInsight</div>', unsafe_allow_html=True)
        st.markdown(
            '<div class="subtitle">Predict. Protect. Prevent.</div>',
            unsafe_allow_html=True,
        )

    st.markdown(
        '<div class="tagline">Access predictive safety intelligence in real time.</div>',
        unsafe_allow_html=True,
    )

    # Card
    login_container = st.container()
    with login_container:
        st.markdown('<div id="login-card"></div>', unsafe_allow_html=True)

        st.markdown("<h2>Welcome to PulseInsight</h2>", unsafe_allow_html=True)
        st.markdown("<p>Please login to continue</p>", unsafe_allow_html=True)

        st.markdown(
            "Work Email Address<span style='color:#8B5CF6;'>*</span>",
            unsafe_allow_html=True,
        )
        username = st.text_input("", key="username")
        st.markdown(
            "Password<span style='color:#8B5CF6;'>*</span>", unsafe_allow_html=True
        )
        password = st.text_input("", type="password", key="password")

        if st.button("Log in"):
            if username == USERNAME and password == PASSWORD:
                st.session_state.logged_in = True
                st.rerun()  # Re-run to load the dashboard after login
            else:
                st.error("Invalid credentials")

        st.markdown("<p>Forgot Password?</p>", unsafe_allow_html=True)


def logout():
    st.session_state.logged_in = False
    st.rerun()  # Re-run to go back to the login page


# Check login status
if not st.session_state.logged_in:
    login()
    st.stop()

# UI Styling
st.markdown(
    """
    <style>

    /* Background */
    @import url('https://fonts.googleapis.com/css2?family=Montserrat:wght@500;600;700&family=Poppins:wght@300;400;500&display=swap');
                
    html, body, [class*="css"] {
        font-family: 'Poppins', sans-serif;
    }
    .main {
        background-color: #F8FAFC;
    }

    /* Sidebar */
    section[data-testid="stSidebar"] {
        background-color: #F8FAFC;
    }
    section[data-testid="stSidebar"] * {
        color: #111827;
    }

    /* Titles */
    h1 {
        font-size: 28px;
        font-weight: 700;
        color: #111827;
    }
    h2 {
        font-size: 20px;
        font-weight: 600;
        color: #1E3A8A;
    }

    /* KPI Cards */
    .metric-card {
        background: #F8FAFC;
        padding: 25px;
        border-radius: 16px;
        box-shadow: 0px 4px 12px rgba(0,0,0,0.05);
        border: 1px solid #1E3A8A;
    }

    /* Buttons */
    .stButton button {
        background-color: #2563EB;
        color: white;
        border-radius: 12px;
        height: 45px;
        font-weight: 600;
    }
    .stButton button:hover {
        background-color: #1E40AF;
    }

    /* Alerts */
    .stAlert {
        border-radius: 12px;
    }

    /* Dataframe */
    .stDataFrame {
        border-radius: 12px;
    }

    </style>
""",
    unsafe_allow_html=True,
)

# Logout button in sidebar
top_col1, top_col2 = st.columns([6, 1])

with top_col2:
    if st.button("Log out"):
        logout()

# Sidebar
st.markdown(
    """
    <style>
    section[data-testid="stSidebar"] h1 {
        color: #111827;
        font-size: 20px;
        font-weight: bold;
        text-align: center;
    }
    
    section[data-testid="stSidebar"] [data-testid="stCaptionContainer"] {
        color: #111827;
        font-size: 14px;
        text-align: center;
    }
    </style>
""",
    unsafe_allow_html=True,
)

col1, col2, col3 = st.sidebar.columns([1, 2, 1])
with col2:
    st.image("assets/Logo.png", width=150)

st.sidebar.title("PulseInsight")
st.sidebar.caption("Predict. Protect. Prevent.")

with st.sidebar:
    col1, col2 = st.columns([1, 2])

    with col1:
        st.image("assets/Jim Hopper DP.png", width=150)

    with col2:
        st.title("Jim Hopper 🛡️")
        st.caption("Safety & Risk Manager")

# Navigation
page = st.sidebar.radio(
    "Navigation",
    ["Dashboard", "Department Details", "Analytics", "Alerts", "Feature Importance"],
)

# Page Routing
if page == "Dashboard":
    from pages.dashboard import show_dashboard

    show_dashboard()

elif page == "Department Details":
    from pages.department_details import show_details

    show_details()

elif page == "Analytics":
    from pages.analytics import show_simulation

    show_simulation()

elif page == "Alerts":
    from pages.alerts import show_alerts

    show_alerts()

elif page == "Feature Importance":
    from pages.feature_importance import show_feature_importance

    show_feature_importance()
