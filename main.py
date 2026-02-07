from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
import json

app = FastAPI(title="Executive Intelligence Agent")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],   # allow frontend
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
) 
from fastapi.responses import FileResponse

@app.get("/")
def home():
    return FileResponse("./index.html")


def generate_executive_brief(data):
    y = data["yesterday"]
    t = data["today"]
    ctx = data["context"]

    insights = [
        f"LTV declined from {y['LTV']} to {t['LTV']}, signaling reduced customer quality.",
        f"CAC increased by {t['CAC'] - y['CAC']}, lowering acquisition efficiency.",
        "Partner retention dropped significantly, indicating growing partner dissatisfaction."
    ]

    risks = [
        "Sustained partner churn could impact revenue stability.",
        "Margin pressure may increase if acquisition costs continue rising."
    ]

    opportunity = (
        "Revising partner commission structures can attract higher-quality partners "
        "and stabilize long-term value."
    )

    actions = [
        "Adjust partner payouts to remain competitive in the market.",
        "Prioritize high-retention acquisition channels.",
        "Introduce weekly partner performance monitoring."
    ]

    return {
        "key_insights": insights,
        "risks": risks,
        "opportunity": opportunity,
        "recommended_actions": actions,
        "context": ctx
    }

@app.get("/executive-brief")
def executive_brief():
    with open("./data.json") as f:
        data = json.load(f)

    return {
        "title": "Overnight Executive Brief",
        "summary": generate_executive_brief(data)
    }



