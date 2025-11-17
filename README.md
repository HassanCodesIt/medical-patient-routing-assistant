# 🩺 Medical Patient Routing Assistant

AI-powered clinical triage engine built with LLMs & FastAPI.

## 🚑 Banner

<h1 align="center" style="font-weight:700;">🚑 Medical Patient Routing Assistant</h1>
<h3 align="center">AI-powered triage engine that analyzes symptoms, asks clinical follow-up questions, and routes patients to the correct medical department.</h3>
<p align="center">
  <img src="https://img.shields.io/badge/AI%20Triage-FastAPI-blue?style=for-the-badge" />
  <img src="https://img.shields.io/badge/Groq-LLaMA3-purple?style=for-the-badge" />
  <img src="https://img.shields.io/badge/Clinical-Routing-green?style=for-the-badge" />
  <img src="https://img.shields.io/badge/Frontend-HTML%2C%20CSS%2C%20JS-yellow?style=for-the-badge" />
</p>

---

## 🧠 Overview

The **Medical Patient Routing Assistant** is an intelligent AI triage system that helps route patients to the correct medical department using structured conversation. It evaluates symptoms across multiple messages, asks follow-up questions, detects red flags, and finally recommends the right specialist with urgency classification.

Built using **FastAPI + Groq LLaMA + Intelligent Memory + Modern UI**.

---

## 🚀 Features

* ✔ Intelligent clinical triage asking contextual follow-up questions
* ✔ Specialist recommendation (Cardiology, Neuro, ENT, etc.)
* ✔ Emergency red-flag detection
* ✔ Multi-turn conversation memory
* ✔ Clean UI with structured cards

---

## 🏗️ Tech Stack

* Python
* FastAPI
* Groq LLaMA 3.3
* HTML / CSS / JavaScript
* Git & GitHub

---

## 📂 Project Structure

```
📦 medical-patient-routing-assistant
 ┣ 📜 main.py
 ┣ 📜 index.html
 ┣ 📜 .env
 ┣ 📜 README.md
```

---

## ⚙️ How It Works

### 1️⃣ User Sends Symptoms

Assistant listens and interprets.

### 2️⃣ System Applies Medical Logic

* Maps symptoms → specialties
* Asks differentiating questions
* Detects red flags

### 3️⃣ Outputs in Required Format

**Follow-up Example:**

```
(type: follow_up)
Q1: <question>
Q2: <question>
Q3: <question>
```

**Final Recommendation:**

```
(type: final_recommendation)
Doctor/Specialty: <name>
Reason: <clinical reason>
Urgency: normal | moderate | high
```

---

## 💻 Run Locally

### Install dependencies

```
pip install fastapi uvicorn python-dotenv groq
```

### Add API key

In `.env`:

```
APIKEY=your_groq_api_key
```

### Start server

```
uvicorn main:app --reload
```

### Open in browser

```
http://127.0.0.1:8000
```

---

## 📥 Clone This Project

```
git clone https://github.com/HassanCodesIt/medical-patient-routing-assistant.git
cd medical-patient-routing-assistant
```

---

## 🛡 Safety Notes

* Does NOT diagnose diseases
* Only routes based on symptoms
* Not a replacement for medical professionals

---

## ✨ Future Enhancements

* Voice-based symptom input
* Dark mode UI
* Symptom analytics dashboard
* Hospital system integration

---

## 👨‍💻 Author

Built with ❤️ by **Hassan Huda**

* GitHub: [https://github.com/HassanCodesIt](https://github.com/HassanCodesIt)
* LinkedIn: [https://www.linkedin.com/in/hassan-huda/](https://www.linkedin.com/in/hassan-huda/)
* Email: [hassanhudapalakkad@gmail.com](mailto:hassanhudapalakkad@gmail.com)

---

**✨ Empowering healthcare triage with AI-driven intelligence ✨**
