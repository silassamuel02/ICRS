from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI(title="ICRS AI Service")


class AnalyzeRequest(BaseModel):
    text: str


@app.get("/health")
def health():
    return {"status": "ok"}


@app.post("/analyze")
def analyze(payload: AnalyzeRequest):
    text = payload.text.lower()
    score = 0.0

    if any(word in text for word in ["fire", "explosion", "smoke"]):
        score = 0.95
    elif any(word in text for word in ["fraud", "theft", "abuse"]):
        score = 0.72
    else:
        score = 0.35

    return {
        "label": "risk_detected" if score >= 0.6 else "low_risk",
        "score": round(score, 2),
        "summary": "AI analysis completed"
    }
