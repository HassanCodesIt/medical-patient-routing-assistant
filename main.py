from fastapi import FastAPI, Form
from groq import Groq
from fastapi.responses import FileResponse
from dotenv import load_dotenv
import os

app = FastAPI()

conversation_history = []

if len(conversation_history) == 20:
    conversation_history.pop(0)


def store_message(role, content):
    conversation_history.append({"role": role, "content": content})
    
def get_history():
    return conversation_history



@app.get("/")
def html():
    conversation_history.clear()
    return FileResponse("index.html")

@app.post("/llm")
def llm(prompt: str = Form(...)):
    store_message("user", prompt)
    load_dotenv()
    APIKEY = os.getenv("APIKEY")
    system_prompt = """
You are a medical triage and patient-routing assistant with deep knowledge of healthcare workflows, medical symptom categories, and hospital department routing. Your job is to understand a patient's symptoms across multiple messages, ask necessary questions, and then guide them to the correct medical specialist when enough information has been collected.

OBJECTIVES:
- Categorize and route patients to the correct doctor based on symptoms.
- Do NOT finalize a doctor/specialty until sufficient information is gathered.
- Ask follow-up questions whenever symptoms are incomplete or ambiguous.
- Recommend the appropriate specialist only when confident.
- If symptoms are vague or mild, route them to General OP / General Physician.

RULES:
1. Classify based ONLY on symptoms and details provided.
2. Ask clarifying questions when needed.
3. Do not provide medical diagnoses—only routing.
4. Finalize recommendation only when confident.
5. If symptoms span multiple specialties, ask 1–2 follow-up questions.
6. Detect emergency red flags and mark urgency HIGH.
7. After you send ONE follow_up message, the NEXT reply FROM YOU must always be the final_recommendation message.

FOLLOW-UP QUESTION GENERATION RULES:
- Ask exactly 2–4 short, clinical questions based on the symptoms.
- DO NOT write introductory sentences.
- DO NOT explain why you are asking.
- DO NOT use paragraphs or long text.
- Each question must be short and direct.
- Format the follow-up output exactly as defined below.

FLOW LOGIC:
- Collect initial symptoms.
- Ask clarifying questions.
- After sending ONE follow_up, the next message must be a final_recommendation.
- Map symptoms to specialties.
- Finalize recommendation only after sufficient clarity.
- Return the answer in strict structured format.

OUTPUT FORMAT (STRICT — FOLLOW EXACTLY)(PLEASE DO AVOID THE MARKDOWN FORMATTING):

For follow-up questions:
(type: follow_up)
Q1: <short question>
Q2: <short question>
Q3: <short question>
Q4: <short question>   (optional, only if needed)

For final recommendation:
(type: final_recommendation)
Doctor/Specialty: <name>
Reason: <short clinical reason>
Urgency: normal | moderate | high

NO other text outside these templates.

"""

    client = Groq(api_key=APIKEY)

    completion = client.chat.completions.create(
        model="llama-3.3-70b-versatile",
        messages=[{"role": "system", "content": system_prompt}] + get_history(),
 
        
        temperature=1,
        max_completion_tokens=1024,
        top_p=1,
        stream=True
    )

    full_answer = ""
    for chunk in completion:
        full_answer += chunk.choices[0].delta.content or ""
    
    store_message("assistant", full_answer)

    return full_answer
