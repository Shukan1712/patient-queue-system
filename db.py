import os
import firebase_admin
from firebase_admin import credentials, firestore
from dotenv import load_dotenv

load_dotenv()

cred = credentials.Certificate(os.getenv("FIREBASE_CREDENTIALS_PATH"))
firebase_admin.initialize_app(cred)
db = firestore.client()

def add_patient(patient):
    db.collection("patients").add(patient)

def get_patients():
    patients_ref = db.collection("patients")
    docs = patients_ref.stream()
    return [doc.to_dict() for doc in docs]

def delete_next_patient():
    patients = get_patients()
    if not patients:
        return None
    sorted_patients = sorted(patients, key=lambda x: (-x["emergency"], x["id"]))
    patient_to_remove = sorted_patients[0]

    patients_ref = db.collection("patients")
    for doc in patients_ref.stream():
        if doc.to_dict() == patient_to_remove:
            doc.reference.delete()
            break
    return patient_to_remove

def move_to_archive(patient):
    db.collection("archive").add(patient)

def get_archived_patients():
    archived_ref = db.collection("archive")
    docs = archived_ref.stream()
    return [doc.to_dict() for doc in docs]
