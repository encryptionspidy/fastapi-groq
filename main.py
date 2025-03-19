from fastapi import FastAPI, Query
import requests
import os

app = FastAPI()

# Groq API Key (from Render environment variable)
GROQ_API_KEY = os.getenv("GROQ_API_KEY")
API_URL = "https://api.groq.com/v1/chat/completions"

@app.get("/")
def home():
    return {"message": "Groq API is running!"}

@app.post("/ask/")
def ask_groq(question: str = Query(..., description="Enter your question")):
    if not GROQ_API_KEY:
        return {"error": "Groq API key is missing!"}

    headers = {"Authorization": f"Bearer {GROQ_API_KEY}", "Content-Type": "application/json"}
    data = {
        "model": "mixtral-8x7b",
        "messages": [{"role": "user", "content": question}],
    }

    response = requests.post(API_URL, headers=headers, json=data)
    return response.json()


