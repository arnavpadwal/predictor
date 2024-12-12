import streamlit as st
import joblib
import numpy as np
import os

# Define the mapping of predictors and intervals to model file names
predictor_mapping = {
    "PF using SF": {
        "SF": {
            "Admission SF": "best_sf_pf_SF_PF.pkl",
            "0-6 hrs SF": "best_sf_pf_0-6_SF_0-6_PF.pkl",
            "6-12 hrs SF": "best_sf_pf_6-12_SF_6-12_PF.pkl",
            "12-24 hrs SF": "best_sf_pf_12-24_SF_12-24_PF.pkl",
            "24-48 hrs SF": "best_sf_pf_24-48_SF_24-48_PF.pkl",
            "48-72 hrs SF": "best_sf_pf_48-72_SF_48-72_PF.pkl",
            "After 72 hrs SF": "best_sf_pf_After_72_SF_After_72_PF.pkl"
        }
    },
    "OI using OSI": {
        "OSI": {
            "Admission OSI": "best_osi_oi_OSI_OI.pkl",
            "0-6 hrs OSI": "best_osi_oi_0-6_OSI_0-6_OI.pkl",
            "6-12 hrs OSI": "best_osi_oi_6-12_OSI_6-12_OI.pkl",
            "12-24 hrs OSI": "best_osi_oi_12-24_OSI_12-24_OI.pkl",
            "24-48 hrs OSI": "best_osi_oi_24-48_OSI_24-48_OI.pkl",
            "48-72 hrs OSI": "best_osi_oi_48-72_OSI_48-72_OI.pkl",
            "After 72 hrs OSI": "best_osi_oi_After_72_OSI_After_72_OI.pkl"
        }
    }
}

# Function to load the model and predict
def load_model_and_predict(file_path, input_value):
    # Load the model from the file
    model = joblib.load(file_path)
    # Make a prediction
    prediction = model.predict(np.array(input_value).reshape(-1, 1))
    return prediction[0]

# Streamlit App Configuration
st.set_page_config(page_title="Prediction App", layout="centered")

# App Title
st.markdown('<h1 class="title">🔮 Prediction App</h1>', unsafe_allow_html=True)
st.markdown("Select a predictor, choose an interval, and input a value for prediction.")

# Sidebar options
st.sidebar.title("Options")

# Select Predictor (SF/PF or OSI/OI)
predictor = st.sidebar.selectbox("Select Predictor", list(predictor_mapping.keys()))

# Select Hour Interval
intervals = list(predictor_mapping[predictor][list(predictor_mapping[predictor].keys())[0]].keys())
hour_interval = st.sidebar.selectbox("Select Hour Interval", intervals)

# Input Value for Prediction
input_value = st.sidebar.number_input("Enter Input Value", min_value=0.0, step=0.1)

# Display Disclaimer for specific intervals
if (predictor == "PF using SF" and hour_interval in ["Admission SF", "0-6 hrs SF"]) or \
   (predictor == "OI using OSI" and hour_interval == "Admission OSI"):
    st.sidebar.markdown("<p style='color:red;'>Note: Predictions for these intervals may be less accurate due to limited data.</p>", unsafe_allow_html=True)

# Predict Button
if st.sidebar.button("Predict"):
    # Get model file path
    model_file = predictor_mapping[predictor][list(predictor_mapping[predictor].keys())[0]][hour_interval]
    model_path = os.path.join("models", model_file)
    
    # Check if model file exists
    if os.path.exists(model_path):
        prediction = load_model_and_predict(model_path, input_value)
        st.markdown(f'<div class="prediction-result">Prediction for <b>{predictor}</b> ({hour_interval}): <span>{prediction:.4f}</span></div>', unsafe_allow_html=True)
    else:
        st.error("Model file not found! Please make sure the model is saved correctly.")

# Custom CSS for Centering the Heading
st.markdown("""
    <style>
        /* General App Styling */
        /* Ensure page title color contrasts with background */
        .title {
            text-align: center;
            font-size: 2.5em;
            color: #333; /* Change this to a darker color for better contrast */
            margin-top: 50px;
        }
        .block-container {
            background-color: #f8f8f8; /* Light background color */
            padding: 2rem;
            border-radius: 20px;
            box-shadow: 0px 4px 15px rgba(0, 0, 0, 0.1);
        }
        /* Sidebar Styling */
        .sidebar .sidebar-content {
            background-color: #000;
            color: white;
            border-radius: 20px;
            padding: 1.5rem;
        }
        .sidebar .sidebar-content h1 {
            color: white;
        }
        .sidebar .sidebar-content input, .sidebar .sidebar-content select {
            background-color: white;
            color: black;
            border-radius: 10px;
        }
        /* Button */
        .stButton > button {
            background-color: black;
            color: white;
            padding: 10px 20px;
            font-size: 1.2em;
            border-radius: 10px;
            border: none;
        }
        .stButton > button:hover {
            background-color: white;
            color: black;
            border: 2px solid black;
        }
        /* Prediction Result Styling */
        .prediction-result {
            text-align: center;
            font-size: 1.8em;
            color: black;
            margin-top: 20px;
            padding: 10px 20px;
            border-radius: 10px;
            background-color: white;
            box-shadow: 0px 4px 15px rgba(0, 0, 0, 0.1);
        }
        .prediction-result span {
            font-weight: bold;
            color: black;
        }
        /* Input Fields Styling */
        .stNumberInput input {
            border-radius: 10px;
            padding: 10px;
            font-size: 1.1em;
            border: 1px solid #000;
        }
    </style>
""", unsafe_allow_html=True)
