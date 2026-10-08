# Landslide-Risk-Prediction-Early-Warning-System
A machine learning-powered system for predicting landslide risks and generating real-time early warnings using spatial, geological, and meteorological data.
⛰️ Landslide Risk Prediction & Early Warning System
A real-time terrain and IoT sensor simulation dashboard designed for the Dehradun & Uttarakhand region to predict landslide risks using Machine Learning.

👨‍💻 About The Project
As a first-year engineering student, I built this project to explore how Machine Learning and GIS mapping can be applied to real-world disaster management.

To bridge the gap between complex ML concepts and practical coding, I leveraged AI tools (Gemini & AI assistants) to help draft, structure, and assemble the codebase while actively learning how each component functions under the hood:

How feature vectors feed into trained machine learning models (.pkl files).

How interactive UI libraries like Streamlit communicate with geospatial frameworks like Folium.

How gauge charts and alert logic present critical data during high-risk scenarios.

✨ Key Features
🎛️ Live IoT Sensor Simulation
Interactive Sliders: Simulates live sensor data feeds including:

Terrain Slope (°): Angle of the land inclination.

Rainfall Intensity (mm/hr): Real-time precipitation rate.

Soil Moisture Level (%): Water saturation percentage in the soil.

Quick Demo Presets: One-click scenario loading for rapid testing (e.g., Normal Weather vs. Heavy Monsoon Critical Risk).

🤖 ML-Powered Hazard Classification
Real-time Inference: Passes sensor inputs into a pre-trained Machine Learning model (model.pkl) to instantly output a risk level from 0 to 3.

Dynamic Warning Banners: Color-coded alert boxes (Low, Medium, High, Critical) triggering situational status messages and automated warning notices.

🗺️ GIS Mapping & Geospatial Dashboard
Regional Monitoring Map: Built with Folium and centered around high-susceptibility zones in Dehradun (Mussoorie Road, Rajpur Sector, Sahastradhara, Clement Town).

Live Station Markers: Sensor nodes dynamically change color on the map according to the predicted risk level.

📊 Plotly Hazard Severity Gauge
Visual Indicator Gauge: Interactive Plotly gauge measuring the threat level on a 0–3 scale (Low, Med, High, Crit) matched with current hazard color schemes.

🏗️ System Architecture & Workflow
Data Layer: Interactive UI simulates IoT sensor telemetry (soil moisture, rainfall, slope).

ML Engine: A Machine Learning classifier (e.g., Random Forest) evaluates feature vectors ([Moisture, Rainfall, Slope]).

Geospatial & Visualization Layer:

Folium dynamically renders geo-located station markers.

Plotly generates responsive gauge charts.

Alert Pipeline: Evaluates risk thresholds and renders emergency warnings when conditions become critical.
FIRST RUN THIS CODE IN TERMINAL TO DOWNLOAD REQUIRED ELEMENT
pip install streamlit pandas numpy scikit-learn folium streamlit-folium plotly twilio
