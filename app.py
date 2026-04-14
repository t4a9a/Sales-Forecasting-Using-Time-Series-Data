import streamlit as st
import pickle
import numpy as np
import time

# Config
st.set_page_config(page_title="Sales Forecasting", page_icon="📊", layout="centered")

# Load model
model = pickle.load(open('sales_model.pkl', 'rb'))

# CSS (Black + Red + Glow)
st.markdown("""
<style>
.stApp {
    background-color: #000;
}
.stApp::before {
    content: "";
    position: fixed;
    width: 100%;
    height: 100%;
    background: radial-gradient(circle at top right, rgba(255,0,0,0.1), transparent 60%);
    z-index: -1;
}
.card {
    background: rgba(20,20,20,0.95);
    padding: 25px;
    border-radius: 15px;
    border: 1px solid rgba(255,0,0,0.3);
    box-shadow: 0 0 15px rgba(255,0,0,0.15);
    animation: fadeIn 1s ease-in-out;
}
.stButton>button {
    background: linear-gradient(90deg, #ff0000, #800000);
    color: white;
    border-radius: 10px;
    height: 3em;
    width: 100%;
}
.stButton>button:hover {
    transform: scale(1.05);
    box-shadow: 0 0 10px red;
}
h1 {
    color: red;
    text-align: center;
}
@keyframes fadeIn {
    from {opacity: 0; transform: translateY(15px);}
    to {opacity: 1; transform: translateY(0);}
}
</style>
""", unsafe_allow_html=True)

# Title
st.markdown("<h1>📊 Sales Forecasting AI</h1>", unsafe_allow_html=True)
st.markdown("<p style='text-align:center;'>Smart Prediction Dashboard</p>", unsafe_allow_html=True)

st.markdown("<div class='card'>", unsafe_allow_html=True)

# Layout
col1, col2 = st.columns(2)

# Dropdown values
stores = list(range(1, 46))
months = list(range(1, 13))
weeks = list(range(1, 53))
days = list(range(1, 32))
years = [2010, 2011, 2012, 2013]

with col1:
    store = st.selectbox("🏬 Store ID", stores)
    holiday = st.selectbox("🎉 Holiday", [0, 1])
    temp = st.slider("🌡 Temperature", -10, 50, 25)
    fuel = st.slider("⛽ Fuel Price", 1.0, 5.0, 2.5)

with col2:
    cpi = st.slider("📊 CPI", 100.0, 300.0, 200.0)
    unemp = st.slider("👨‍💼 Unemployment", 0.0, 15.0, 8.0)
    year = st.selectbox("📅 Year", years)
    month = st.selectbox("🗓 Month", months)

week = st.selectbox("📆 Week", weeks)
day = st.selectbox("📌 Day", days)

st.markdown("</div>", unsafe_allow_html=True)

# Hidden lag values
lag1 = 1000000
lag2 = 1000000
rolling = 1000000

st.divider()

# Prediction
if st.button("🚀 Predict Sales"):

    with st.spinner("🤖 AI thinking..."):
        time.sleep(1.5)

    data = np.array([[store, holiday, temp, fuel, cpi, unemp,
                      year, month, week, day, lag1, lag2, rolling]])

    prediction = model.predict(data)

    # Animated result
    placeholder = st.empty()
    for i in range(0, int(prediction[0]), int(prediction[0]/20)):
        placeholder.markdown(f"<h1 style='text-align:center;color:red;'>₹ {i:,}</h1>", unsafe_allow_html=True)
        time.sleep(0.03)

    placeholder.markdown(f"<h1 style='text-align:center;color:white;'>₹ {prediction[0]:,.2f}</h1>", unsafe_allow_html=True)