from pydantic import BaseModel
from typing import Optional, Dict

class ErrorLog(BaseModel):
    project_id: str
    source: str
    message: str
    stack: Optional[str]
    metadata: Optional[Dict]