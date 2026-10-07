import numpy as np
import pandas as pd
from sklearn.ensemble import RandomForestClassifier
import pickle

# setup: run this in the terminal once
# pip install streamlit pandas numpy scikit-learn folium streamlit-folium twilio
# random data generation for the prototype
no_of_sample = 100
slope = np.random.uniform(15, 50, no_of_sample)

rainfall = np.random.uniform(0, 65, no_of_sample)
soil_moisture = np.random.uniform(30, 60, no_of_sample)

# risk calculation
risk_cal = (slope * 0.37) + (rainfall * 0.26) + (soil_moisture * 0.30)

# category: 0 = low, 1 = medium, 2 = high, 3 = critical
risk = []
for score in risk_cal:
    if score < 28:
        risk.append(0)   # Low
    elif score < 34:
        risk.append(1)   # Medium
    elif score < 40:
        risk.append(2)   # High
    else:
        risk.append(3)   # Critical

# create dataframe
df = pd.DataFrame({
    'slope': slope,
    'rainfall': rainfall,
    'soil_moisture': soil_moisture,
    'risk_level': risk
})
print(df['risk_level'].value_counts())   # check all 4 classes exist

# train model
a = df[['slope', 'rainfall', 'soil_moisture']]
b = df['risk_level']

model = RandomForestClassifier(n_estimators=100, random_state=42)
model.fit(a, b)

with open('model.pkl', 'wb') as f:
    pickle.dump(model, f)

print("Model trained successfully and saved as 'model.pkl'!")