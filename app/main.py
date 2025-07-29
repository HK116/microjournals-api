from fastapi import FastAPI
from typing import List
from app.models import JournalEntry
from datetime import datetime

app = FastAPI(title="MicroJournals API")

# In-memory stores for now
entries: List[JournalEntry] = []

entries.append(JournalEntry(id=1, content="This is my first journal. to test the functionality", mood="Meh", timestamp=datetime.now()))

@app.get("/entries", response_model=List[JournalEntry])
def get_entries():
    return entries