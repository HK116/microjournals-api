# 📝 MicroJournals API

A minimal yet extensible journaling API built with FastAPI.  
Capture tiny daily entries, moods, and moments — like digital sticky notes for your mind.

---

## 🚀 Features (MVP)
- Add short journal entries
- Attach optional mood or tag
- Retrieve all past entries
- Built with [FastAPI](https://fastapi.tiangolo.com/) — automatic docs included!

---

## 📦 Project Structure
```
microjournals-api/
├── app/
│ ├── main.py # FastAPI routes and server
│ └── models.py # Pydantic models for entries
├── requirements.txt # Project dependencies
└── README.md # This file
```
---

## 📚 Getting Started

### 1. Clone the project

```bash
git clone https://github.com/your-username/microjournals-api.git
cd microjournals-api
```

### 2. Creating a virtual environment

```bash
python -m venv .venv
source .venv/bin/activate  # On Windows use: .venv\Scripts\activate
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

### 4 Run the server

```bash
uvicorn app.main:app --reload
```

Then open your browser:

- API: http://127.0.0.1:8000/entries
- Docs: http://127.0.0.1:8000/docs

## 🔧 Example Entry (to be added manually for now)

```python
from app.models import JournalEntry
from datetime import datetime

entries.append(JournalEntry(
    id=1,
    content="This is my first micro-journal!",
    mood="grateful",
    timestamp=datetime.now()
))
```