# patient-queue-system
Cloud-deployed patient queue manager built with FastAPI, Firebase, and Bootstrap frontend

# 🏥 Cloud-Based Patient Queue Management System

This is a **full-stack, cloud-ready Patient Queue Management System** built using FastAPI (Python), Firebase, and Bootstrap. It simulates a live hospital triage system where patients are added based on emergency level and prioritized accordingly.


live link to see the project
🌐 **Live Project**: [http://3.138.120.238:8000](http://3.138.120.238:8000)

---

## 🚀 Features

- ✅ Add/View/Remove patients
- 🔺 Emergency-based priority queue logic
- 🧠 Firebase Firestore for real-time cloud database
- 🌐 FastAPI-powered REST backend
- 💻 Bootstrap-based responsive frontend
- ☁️ Deployed on AWS EC2 (Ubuntu server)

---

## 📦 Tech Stack

| Layer      | Technology              |
|------------|--------------------------|
| Backend    | FastAPI, Uvicorn         |
| Frontend   | HTML, Bootstrap 5        |
| Database   | Firebase Firestore       |
| Auth       | Simple local demo auth   |
| Deployment | AWS EC2 + systemd        |

---

## 👨‍💻 Author

**Shukan Miteshkumar Shah**  
- 👨‍💻 GitHub: [Shukan1712](https://github.com/Shukan1712)
- 🌱 Website: [Visit My Portfolio](https://sites.google.com/view/shukan-shah/about-me) 
📍 Based in British Columbia, Canada  
🎓 The University of British Columbia (UBC)| Computer Science 


---
## 🧠 Logic Summary

- Patients are added with an emergency level (1–5).
- Highest emergency patients appear first (5 > 1).
- Admin can "Treat Next" to remove and archive the top patient.



## 📦 Deployment Summary

- Hosted on AWS EC2 (Ubuntu)
- Uses `systemd` to keep the app alive:
```bash
sudo nano /etc/systemd/system/patient-queue.service
```

---

## ⚙️ How to Run Locally

1. **Clone the repo**
```bash
git clone https://github.com/yourusername/patient-queue.git
cd patient-queue
```

2. **Set up virtual environment**
```bash
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

3. **Set environment variable for Firebase**
```
export FIREBASE_CREDENTIALS_PATH=./serviceAccountKey.json
```

4. **Run the app**
```bash
uvicorn main:app --reload
```

5. **Open in browser**: `http://127.0.0.1:8000`

---

## 📁 Project Structure

```
.
├── main.py                 # FastAPI app with routes
├── db.py                   # Firebase Firestore interaction
├── models.py               # Patient schema
├── static/                 # HTML frontend
├── serviceAccountKey.json  # Firebase credentials (not committed)
└── README.md
```

---

## 👨‍⚕️ Admin Login (Demo)

```
Email: admin@queue.com
Pass : 1234
```
---

## 🙌 Author
Made with ❤️ by Shukan Shah
