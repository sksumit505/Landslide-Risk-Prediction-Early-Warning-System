import streamlit as st
import pandas as pd
import folium
from streamlit_folium import st_folium
import pickle
import numpy as np
import plotly.graph_objects as go


st.set_page_config(page_title="AI Landslide Early Warning System", layout="wide")

# Load trained ML model
@st.cache_resource
def load_model():
    with open('model.pkl', 'rb') as f:
        return pickle.load(f)

try:
    model = load_model()
except FileNotFoundError:
    st.error("⚠️ `model.pkl` not found! Please run `python Train_model.py` first to generate the model.")
    st.stop()

model = load_model()

st.title("⛰️ AI-Based Early Warning & Landslide Risk Monitoring System")
st.caption("Real-Time Terrain & Sensor Simulation | Dehradun & Uttarakhand Region")

# Sidebar - Live Sensor Inputs
st.sidebar.header("📊 Sensor Input Controls")
slope_input = st.sidebar.slider("Terrain Slope (°)", min_value=10, max_value=60, value=35)
rainfall_input = st.sidebar.slider("Rainfall Rate (mm/hr)", min_value=0, max_value=150, value=40)
moisture_input = st.sidebar.slider("Soil Moisture (%)", min_value=10, max_value=90, value=50)

# Quick Presets for Demo
st.sidebar.markdown("---")
st.sidebar.subheader("Quick Demo Presets")
if st.sidebar.button("Normal Weather"):
    slope_val, rainfall_val, moisture_val = 20.0, 10.0, 35.0
if st.sidebar.button("Heavy Monsoon (Critical Risk)"):
    slope_val, rainfall_val, moisture_val = 45.0, 85.0, 82.0

# ML Prediction
features = np.array([[slope_input, rainfall_input, moisture_input]])
prediction = model.predict(features)[0]

risk_levels = {
    0: ("LOW RISK", "green"),
    1: ("MEDIUM RISK", "yellow"),
    2: ("HIGH RISK", "orange"),
    3: ("CRITICAL / EVACUATE", "red")
}
risk_info={0: {"label": "LOW RISK", "color":"#28a74c", "alert": "Normal conditions. No immediate threat detected."},
    1: {"label": "MEDIUM RISK", "color": "#ffc107", "alert": "Elevated soil moisture. Monitoring active."},
    2: {"label": "HIGH RISK", "color": "#fd7e14", "alert": "High slope saturation! Disaster response teams on standby."},
    3: {"label": "CRITICAL RISK", "color": "#b81021", "alert": "🚨 EMERGENCY WARNING: High probability of slope failure! Automated SMS alert triggered."}
}

current_status=risk_info[prediction]
col1,col2,col3,col4=st.columns(4)
col1.metric("Predicted Status", current_status["label"])
col2.metric("rainfall Rate",f"{rainfall_input}mm/hr")
col3.metric("soil saturation",f"{moisture_input}")
col4.metric("Terrain Slope", f"{slope_input}°")
# banner alter 
if prediction==1:
    st.error(f"***Stutas{current_status['label']}***-- {current_status['label']}")
elif prediction==2:
    st.error(f"***Stutas{current_status['label']}***-- {current_status['label']}")
elif prediction==3:
    st.error(f"***Stutas{current_status['label']}***-- {current_status['label']}")

st.markdown("---")
# 6. Interactive GIS Map & Risk GaugeA
left_col, right_col = st.columns([2, 1])
with left_col:
    st.subheader("🗺️ Regional Monitoring Map (Dehradun Sector)")
 # Map centered around Dehradun
    m = folium.Map(location=[30.3165, 78.0322], zoom_start=11, tiles="OpenStreetMap")
#sensor loctation
    sensors = [
        {"name": "Station A - Mussoorie Road", "lat": 30.3800, "lon": 78.0800},
        {"name": "Station B - Rajpur Sector", "lat": 30.3600, "lon": 78.0900},
        {"name": "Station C - Sahastradhara", "lat": 30.3850, "lon": 78.1300},
        {"name": "Station D - Clement Town", "lat": 30.2680, "lon": 78.0070}
    ]
    for sensor in sensors:
        folium.CircleMarker(
            location=[sensor["lat"], sensor["lon"]],
            radius=12,
            popup=f"<b>{sensor['name']}</b><br>Status: {current_status['label']}",
            color=current_status["color"],
            fill=True,
            fill_color=current_status["color"],
            fill_opacity=0.7
        ).add_to(m)
st_folium(m, width=700, height=400)

with right_col:
    st.subheader("📊 Hazard Severity Gauge")
    
    fig = go.Figure(go.Indicator(
        mode="gauge+number",
        value=prediction,
        domain={'x': [0, 1], 'y': [0, 1]},
        title={'text': "Risk Scale (0-3)"},
        gauge={
            'axis': {'range': [0, 3], 'tickvals': [0, 1, 2, 3], 'ticktext': ['Low', 'Med', 'High', 'Crit']},
            'bar': {'color': current_status["color"]},
            'steps': [
                {'range': [0, 1], 'color': "lightgreen"},
                {'range': [1, 2], 'color': "khaki"},
                {'range': [2, 3], 'color': "orange"},
                {'range': [3, 4], 'color': "salmon"}
            ]
        }
    ))
    fig.update_layout(height=350, margin=dict(l=20, r=20, t=50, b=20))
    st.plotly_chart(fig, use_container_width=True)

# 7. System Architecture Footer
with st.expander("ℹ️ System Architecture & Data Pipeline"):
    st.write("""
    - **Data Layer:** Simulated IoT sensors measuring soil saturation, slope angle, and rainfall intensity.
    - **ML Engine:** Random Forest Classifier trained on terrain and weather triggers[cite: 3].
    - **GIS Mapping:** Folium geospatial engine displaying active station hazard status in real-time.
    - **Alert Pipeline:** Trigger thresholds sending automated warnings when risk reaches Critical level[cite: 2, 3].
    """)