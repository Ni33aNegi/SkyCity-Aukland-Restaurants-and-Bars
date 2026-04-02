import streamlit as st
import webbrowser

# Page Config
st.set_page_config(
    page_title="Skycity Analytics Dashboard",
    page_icon="📊",
    layout="centered"
)

# Custom CSS for professional UI
st.markdown("""
    <style>
        .main {
            text-align: center;
        }
        .title {
            font-size: 42px;
            font-weight: bold;
            color: #2E86C1;
        }
        .subtitle {
            font-size: 18px;
            color: #555;
            margin-bottom: 30px;
        }
        .stButton>button {
            background-color: #2E86C1;
            color: white;
            font-size: 18px;
            padding: 10px 30px;
            border-radius: 10px;
            border: none;
        }
        .stButton>button:hover {
            background-color: #1B4F72;
            color: white;
        }
    </style>
""", unsafe_allow_html=True)

# UI Content
st.markdown('<div class="title">📊 Skycity Restaurants and Bars Analysis</div>', unsafe_allow_html=True)
st.markdown('<div class="subtitle">Interactive Dashboard for Business Insights & Performance Tracking</div>', unsafe_allow_html=True)

# st.image("https://images.unsplash.com/photo-1556741533-974f8e62a92d", use_container_width=True)

st.write("")

st.markdown("""
### 🚀 Features
- Real-time Data Visualization  
- Channel Performance Analysis  
- Customer Insights  
- Sales Trends & KPIs  
""")

st.write("")

# Button to open main dashboard
if st.button("🔍 Open Dashboard"):
    webbrowser.open_new_tab("http://localhost:8501")  # Change port if needed