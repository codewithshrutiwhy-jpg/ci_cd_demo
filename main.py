from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

class EmailRequest(BaseModel):
    text: str

@app.get("/")
def home():
    return {"message": "Hello Shrutika"}

@app.get("/health")
def health():
    return {"status": "OK"}

@app.post("/summarize")
def summarize_email(request: EmailRequest):
    text = request.text

    # Simple logic (we’ll upgrade later)
    summary = text[:100]  # first 100 characters

    return {
        "original_length": len(text),
        "summary": summary
    }