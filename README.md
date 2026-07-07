# 🩸 Non-Invasive AI Glucose Tracker
**Build with AI: Code for Communities Hackathon | Real-time PPG Signal Analysis**

![Python](https://img.shields.io/badge/Python-3.9+-blue.svg)
![FastAPI](https://img.shields.io/badge/FastAPI-0.100+-009688.svg)
![Streamlit](https://img.shields.io/badge/Streamlit-1.25+-FF4B4B.svg)
![Docker](https://img.shields.io/badge/Docker-Ready-2496ED.svg)
![Hackathon](https://img.shields.io/badge/Hack2Skill-Code_for_Communities-orange.svg)

An end-to-end, Dockerized, real-time healthcare application that predicts Blood Glucose levels non-invasively using Photoplethysmography (PPG) signals. Built for the **"Build with AI: Code for Communities"** Hackathon.

## 🎥 Watch Live Demo Video: https://drive.google.com/file/d/12x02vdEnKTFEyT0lhI5m3j4QDz8W-c9P/view?usp=sharing

## 🚀 The Problem
Currently, millions of diabetic patients rely on traditional glucometers that require painful, daily finger-pricking. This method is uncomfortable and expensive, limiting continuous monitoring for communities with fewer healthcare resources.

## 💡 Our Solution
We developed a **Zero-Blood, Non-Invasive Glucose Tracker**. 
By capturing raw PPG signals, our AI pipeline filters the noise, extracts critical waveform features (like Systolic/Diastolic peaks, Area, Pulse Intervals), and applies a highly optimized regression model mapped to patient demographics to predict blood glucose levels in real-time.

## 🛠️ System Architecture
1. **Frontend (Streamlit):** A clinical dashboard for real-time visualization of the PPG waveform and AI predictions.
2. **Backend (FastAPI):** A high-performance REST API that receives raw signal payloads and runs feature extraction.
3. **AI/Signal Processing (SciPy/NumPy):** Performs advanced filtering (Butterworth) and intelligent peak detection.
4. **Containerization (Docker Compose):** Fully isolated microservices architecture for the UI and API, ensuring zero-configuration deployment.

## 💻 Tech Stack
* **Backend:** FastAPI, Uvicorn, Python
* **Frontend:** Streamlit
* **AI & Data Processing:** SciPy, NumPy, Pandas, Scikit-Learn
* **DevOps / Deployment:** Docker, Docker Compose, Cloudflare Tunnels

## ⚙️ How to Run Locally (Using Docker)

The easiest way to run this project is using Docker. You don't need to manually configure Python environments.

**1. Clone the repository:**
```
git clone [https://github.com/surjeetlko/Non-Invasive-AI-Glucose-Tracker.git](https://github.com/surjeetlko/Non-Invasive-AI-Glucose-Tracker.git)
cd Non-Invasive-AI-Glucose-Tracker
```

2. Fire up the Containers:

```
docker-compose up -d --build
```

3. Access the Application:

* Live Dashboard: http://localhost:8501
* API Swagger Docs: http://localhost:8014/docs

(To stop the application, simply run docker-compose down)

## 📸 Dashboard Preview
<img width="1920" height="1185" alt="screencapture-sensitivity-stylus-expensive-committees-trycloudflare-2026-07-07-13_52_05" src="https://github.com/user-attachments/assets/8ac32a00-2ec8-4af7-afd4-27873261feb2" />

## 🤝 Built For Communities
This project aims to democratize health monitoring, making it affordable, painless, and accessible to everyone.
