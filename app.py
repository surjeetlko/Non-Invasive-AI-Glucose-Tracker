import os
import streamlit as st
import requests
import matplotlib.pyplot as plt
import numpy as np

# Page Configuration
st.set_page_config(page_title="AI Glucose Tracker", page_icon="🩸", layout="wide")

st.title("🩸 Non-Invasive AI Glucose Tracker")
st.markdown("**Build with AI: Code for Communities Hackathon** | Real-time PPG Signal Analysis")
st.markdown("---")

# Layout: Two columns
col1, col2 = st.columns([1, 2])

with col1:
    st.subheader("Patient Details")
    # Simple form for demo purposes
    pid = st.text_input("Patient ID", value="5555555")
    pname = st.text_input("Patient Name", value="Mukesh")
    age = st.number_input("Age", value=53, min_value=1, max_value=100)
    gender = st.selectbox("Gender", ["Male", "Female"])
    
    st.markdown("---")
    analyze_btn = st.button("🚀 Start Virtual Sensor & Analyze", use_container_width=True)

with col2:
    st.subheader("Live PPG Analysis Dashboard")
    
    # Placeholder for results
    result_placeholder = st.empty()
    graph_placeholder = st.empty()

    if analyze_btn:
        with st.spinner("Analyzing PPG Signal with AI..."):
            
            # 1. Prepare the exact payload your API expects (using your test data)
            # api_url = "http://172.16.75.31:8014/api/v3/glucose"
            api_url = os.getenv("API_URL", "http://localhost:8014/api/v3/glucose")
            headers = {
                "authKey": "N4N56F50UF4UGSN",
                "Content-Type": "application/json"
            }
            
            # Using your exact sample RD string for the demo
            sample_rd = "53240.0,53234.0,53250.0,53264.0,53323.0,53294.0,53308.0,53341.0,53354.0,53355.0,53391.0,53365.0,53425.0,53402.0,53425.0,53444.0,53462.0,53398.0,53365.0,53213.0,52994.0,52730.0,52562.0,52455.0,52403.0,52333.0,52343.0,52318.0,52331.0,52360.0,52377.0,52407.0,52455.0,52507.0,52572.0,52653.0,52730.0,52789.0,52838.0,52848.0,52898.0,52969.0,52969.0,52987.0,53011.0,52992.0,53039.0,53044.0,53053.0,53071.0,53097.0,53102.0,53132.0,53159.0,53196.0,53212.0,53219.0,53266.0,53256.0,53265.0,53293.0,53316.0,53313.0,53342.0,53363.0,53393.0,53374.0,53408.0,53435.0,53433.0,53450.0,53448.0,53480.0,53466.0,53488.0,53506.0,53507.0,53516.0,53526.0,53516.0,53539.0,53544.0,53533.0,53547.0,53570.0,53530.0,53520.0,53475.0,53368.0,53135.0,52860.0,52643.0,52449.0,52352.0,52281.0,52231.0,52186.0,52182.0,52137.0,52139.0,52133.0,52161.0,52201.0,52241.0,52310.0,52369.0,52447.0,52501.0,52556.0,52618.0,52625.0,52665.0,52690.0,52719.0,52744.0,52751.0,52764.0,52780.0,52807.0,52819.0,52820.0,52849.0,52888.0,52892.0,52922.0,52941.0,52973.0,52980.0,53007.0,53022.0,53033.0,53040.0"
            
            payload = {
                "time": "2026-07-06 13:06:02",
                "deviceName": "CT_Glucose",
                "parameters": {
                    "pid": pid,
                    "pname": pname,
                    "gender": gender,
                    "age": str(age),
                },
                "graph": {
                    "RD": sample_rd
                }
            }

            try:
                # 2. Hit your FastAPI backend
                response = requests.post(api_url, json=payload, headers=headers)
                
                if response.status_code == 200:
                    data = response.json()
                    predicted_glucose = data.get("predicted_glucose", "Error")
                    
                    # 3. Display Beautiful Results
                    result_placeholder.success("✅ Analysis Complete!")
                    st.metric(label="Predicted Blood Glucose", value=f"{predicted_glucose} mg/dL", delta="Non-Invasive AI Model")
                    
                    # 4. Plot the Signal for the Judges
                    st.markdown("### Raw PPG Signal Waveform")
                    rd_values = [float(x.strip()) for x in sample_rd.split(',') if x.strip()]
                    
                    fig, ax = plt.subplots(figsize=(10, 3))
                    ax.plot(rd_values, color='red', linewidth=1.5)
                    ax.set_title("Photoplethysmography (PPG) Signal")
                    ax.set_xlabel("Time (Samples)")
                    ax.set_ylabel("Amplitude")
                    ax.grid(True, linestyle='--', alpha=0.6)
                    
                    graph_placeholder.pyplot(fig)
                    
                else:
                    result_placeholder.error(f"Error {response.status_code}: {response.text}")
                    
            except Exception as e:
                result_placeholder.error(f"Connection Failed! Is your FastAPI running on port 8014? Error: {e}")