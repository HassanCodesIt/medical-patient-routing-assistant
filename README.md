


```markdown
<h1 align="center">🩺 Medical Patient Routing Assistant</h1>
<h3 align="center">AI-powered clinical triage engine built with LLMs & FastAPI</h3>

<p align="center">
  <img src="https://img.shields.io/badge/Status-Active-success?style=for-the-badge" />
  <img src="https://img.shields.io/badge/Tech-FastAPI-blue?style=for-the-badge" />
  <img src="https://img.shields.io/badge/LLM-Groq%20LLaMA3-purple?style=for-the-badge" />
  <img src="https://img.shields.io/badge/Frontend-HTML%2FCSS%2FJS-yellow?style=for-the-badge" />
</p>

---

## 🧠 Overview

The **Medical Patient Routing Assistant** is an intelligent AI triage system that helps route patients to the correct medical department using structured conversation.  
It evaluates symptoms across multiple messages, asks follow-up questions, detects red flags, and finally recommends the right specialist with urgency classification.

Built using **FastAPI + Groq LLaMA + Intelligent Memory + Modern UI**.

---

## 🚀 Features

### ✔ Intelligent Clinical Triage  
Understands symptoms and asks context-aware follow-up questions.

### ✔ Specialist Recommendation  
Smart routing to:
- Cardiologist  
- Neurologist  
- ENT  
- Dermatologist  
- Orthopedics  
- Pulmonologist  
- Gastroenterologist  
- Psychologist  
- General Physician  
…based strictly on symptoms.

### ✔ Emergency Detection  
Flags critical cases with **Urgency: HIGH**.

### ✔ Multi-turn Conversation Memory  
Maintains conversation until user reloads the page.

### ✔ Clean & Professional UI  
- Chat bubbles  
- Structured follow-up question formatting  
- Doctor recommendation cards  
- Auto newline rendering  

---

## 🏗️ Tech Stack

<p align="center">
  <img src="https://skillicons.dev/icons?i=python,fastapi,html,css,javascript,github,vscode&perline=7" />
</p>

---

## 📂 Project Structure

```

📦 medical-patient-routing-assistant
┣ 📜 main.py                         # FastAPI backend + LLM logic
┣ 📜 index.html                      # Frontend interface
┣ 📜 .env                            # Groq API key
┣ 📜 README.md                       # Documentation
┗ 📂 (optional static assets)

```

---

## ⚙️ How It Works

### 1️⃣ User Sends Symptoms  
The assistant interprets the complaint.

### 2️⃣ System Applies Medical Logic  
- Maps symptoms → likely specialties  
- Asks differentiating questions  
- Considers emergency flags  

### 3️⃣ Structured Output is Returned:

**Follow-up Format**
```

(type: follow_up)
Q1: <question>
Q2: <question>
Q3: <question>

```

**Final Recommendation Format**
```

(type: final_recommendation)
Doctor/Specialty: <name>
Reason: <clinical reason>
Urgency: normal | moderate | high

````

---

## 🚀 Running Locally

### 1. Install dependencies
```bash
pip install fastapi uvicorn python-dotenv groq
````

### 2. Add your Groq API key

Create `.env`:

```
APIKEY=your_groq_api_key_here
```

### 3. Start the server

```bash
uvicorn main:app --reload
```

### 4. Open the UI

Visit:

```
http://127.0.0.1:8000
```

---

## 🛡️ Safety Notes

* This project **does not diagnose diseases**.
* It only performs **department routing** based on symptoms.
* Not a replacement for certified medical professionals.

---

## ✨ Future Improvements

* 🔊 Voice-based symptom input
* 🌙 Dark mode
* 🧠 Department-level confidence scoring
* 🏥 Integration with hospital systems

---

## 🤝 Contributing

Contributions, issues, and feature ideas are welcome!

---

## 👨‍💻 Author

<h3 align="center">Built with ❤️ by <a href="https://github.com/HassanCodesIt">Hassan Huda</a></h3>

<p align="center">
  <a href="https://www.linkedin.com/in/hassan-huda/">
    <img src="https://img.shields.io/badge/LinkedIn-0A66C2?logo=linkedin&logoColor=white&style=for-the-badge" />
  </a>
  <a href="mailto:hassanhudapalakkad@gmail.com">
    <img src="https://img.shields.io/badge/Gmail-Contact-red?logo=gmail&logoColor=white&style=for-the-badge" />
  </a>
  <a href="https://github.com/HassanCodesIt">
    <img src="https://img.shields.io/badge/GitHub-171515?logo=github&logoColor=white&style=for-the-badge" />
  </a>
</p>

---

<p align="center">
  <sub><b>✨ Empowering healthcare triage with AI-driven intelligence ✨</b></sub>
</p>
```

---


