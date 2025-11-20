
from fastapi import FastAPI, Form, UploadFile, File
from groq import Groq
from fastapi.responses import FileResponse
from dotenv import load_dotenv
import os
from groq import Groq
from gtts import gTTS



app = FastAPI()

conversation_history = []



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
    global last_llm_output
    last_llm_output = ""
    store_message("user", prompt)
    load_dotenv()
    APIKEY = os.getenv("APIKEY")
    system_prompt = """
You are a medical triage and patient-routing assistant with deep knowledge of healthcare workflows, medical symptom categories, and hospital department routing. Your job is to understand a patient's symptoms across multiple messages, ask necessary questions, and then guide them to the correct medical specialist when enough information has been collected.

OBJECTIVES:
- Categorize and route patients to the correct doctor based on symptoms.
- NEVER finalize a doctor/specialty until sufficient information is gathered.
- Ask ONLY ONE follow-up question at a time.
- Recommend the appropriate specialist only when confident.
- If symptoms are vague or mild, route them to General OP / General Physician.

FOLLOW-UP QUESTION RULES:
- You MUST output exactly ONE short, direct clinical question.
- No introductions, no explanations, no paragraphs.
- Your follow_up message MUST contain only:
  Q1: <short question>
- Ask one question, stop, and wait for patient reply.

FLOW LOGIC:
- Collect initial symptom message.
- Send ONE follow_up message containing exactly ONE question.
- After receiving the user's answer, your NEXT response MUST be a final_recommendation.

OUTPUT FORMAT (STRICT — FOLLOW EXACTLY):

For follow-up:
(type: follow_up)
 <short question>

For final recommendation:
(final recommendation)
Doctor/Specialty: <name>
Reason: <short clinical reason>
Urgency: normal | moderate | high

NO OTHER TEXT outside these templates.


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
    
    last_llm_output = full_answer
    
    return full_answer


@app.post("/speech-to-text")
async def speechtotext(audio: UploadFile = File(...)):
    
    load_dotenv()
    APIKEY = os.getenv("APIKEY")
    client = Groq(api_key=APIKEY)
    
    audio_bytes = await audio.read() #read the uploaded file as bytes
    
    
    
    transcription = client.audio.transcriptions.create(
        file=(audio.filename, audio_bytes),
        model="whisper-large-v3-turbo",
        temperature=0,
        response_format="verbose_json",
        )
    transcription_text=transcription.text
        
    llmresponse =llm(prompt=transcription_text)
    
    return {"transcription": transcription_text, "llm_response": llmresponse}



audio_id=[]



@app.post("/text-to-speech")
def tts():
    
    
    next_id=len(audio_id)+1
    
    tts=gTTS(last_llm_output)
    filename=f'audio{next_id}.mp3'
    tts.save(filename)
    
    audio_id.append(filename)
    return FileResponse(filename)
    