from pydantic import BaseModel, Field
from datetime import datetime
from typing import Optional

class JournalEntry(BaseModel):
    id: int
    content: str = Field(..., min_length=1, max_length=500)
    mood: Optional[str] = Field(None, description="Optional mood like happy, sad, etc.")
    timestamp: datetime