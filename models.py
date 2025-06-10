from pydantic import BaseModel, EmailStr
from typing import Optional

class ClassResponse(BaseModel):
    id: int
    name: str
    instructor: str
    time: str  # formatted datetime string
    timezone: str
    available_slots: int

class BookingRequest(BaseModel):
    class_id: int
    client_name: str
    client_email: EmailStr

class BookingResponse(BaseModel):
    class_id: int
    client_name: str
    client_email: EmailStr
