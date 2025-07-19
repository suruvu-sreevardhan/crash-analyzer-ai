from fastapi import FastAPI, UploadFile, File, Form
from fastapi.middleware.cors import CORSMiddleware
from log_parser import parse_logs_near_timestamp
from ai_explainer import explain_bug
import os

app = FastAPI()

# ✅ Only add CORS once
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # You can replace * with ["http://localhost:3000"] for more security
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"]
)

UPLOAD_DIR = "uploads"
os.makedirs(UPLOAD_DIR, exist_ok=True)

# ✅ Route 1: POST /analyze/
@app.post("/analyze/")
async def analyze_log(
    file: UploadFile = File(...),
    timestamp: str = Form(...)
):
    file_path = os.path.join(UPLOAD_DIR, file.filename)
    with open(file_path, "wb") as f:
        f.write(await file.read())

    relevant_logs = parse_logs_near_timestamp(file_path, timestamp)
    explanation = explain_bug(relevant_logs)
    return {"summary": explanation}

# ✅ Route 2: GET /
@app.get("/")
def read_root():
    return {"message": "Hello from FastAPI!"}
