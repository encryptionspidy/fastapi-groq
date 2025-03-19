from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
import requests
import os

app = FastAPI()

# Load API Key from environment variable
GROQ_API_KEY = os.getenv("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")
API_URL = "https://api.groq.com/v1/chat/completions"

# Request model
class QueryModel(BaseModel):
    question: str

@app.get("/")
def home():
    return {"message": "Groq API is running!"}

@app.post("/ask/")
def ask_groq(query: QueryModel):
    if not GROQ_API_KEY:
        raise HTTPException(status_code=500, detail="Groq API key is missing!")

    headers = {
        "Authorization": f"Bearer {GROQ_API_KEY}",
        "Content-Type": "application/json"
    }
    data = {
        "model": "mixtral-8x7b",
        "messages": [{"role": "user", "content": query.question}]
    }

    response = requests.post(API_URL, headers=headers, json=data)
    return response.json()

