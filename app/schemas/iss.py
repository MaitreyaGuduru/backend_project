from pydantic import BaseModel
from datetime import datetime

class TLERequest(BaseModel):
    tle_line1: str
    tle_line2: str
    timestamp: datetime  # Optional: can also accept current time

class PositionOut(BaseModel):
    x: float
    y: float
    z: float
