from fastapi import FastAPI, Request, HTTPException
from fastapi.responses import HTMLResponse, FileResponse
from fastapi.staticfiles import StaticFiles
from fastapi.middleware.cors import CORSMiddleware
from models import Patient
from db import add_patient, get_patients, delete_next_patient, move_to_archive, get_archived_patients
import os

app = FastAPI()

# Allow frontend JS to call backend
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"]
)

# Serve HTML frontend
app.mount("/static", StaticFiles(directory="static"), name="static")

@app.get("/", response_class=HTMLResponse)
def serve_home():
    return FileResponse("static/index.html")

@app.post("/add")
def add(patient: Patient):
    add_patient(patient.dict())
    return {"message": "Patient added successfully."}

@app.get("/list")
def list_patients():
    return get_patients()

@app.delete("/next")
def next_patient():
    patient = delete_next_patient()
    if patient:
        move_to_archive(patient)
        return {"message": f"{patient['name']} treated and archived."}
    return {"message": "No patients in the list"}

@app.get("/archive")
def archive_patients():
    return get_archived_patients()

@app.post("/login")
def login(credentials: dict):
    email = credentials.get("email")
    password = credentials.get("password")
    if email == "admin@queue.com" and password == "1234":
        return {"message": "Login successful", "role": "admin"}
    raise HTTPException(status_code=401, detail="Invalid credentials")
