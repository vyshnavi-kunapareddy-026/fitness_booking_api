from pydantic import BaseModel, Field
from typing import Optional

class BookingRequest(BaseModel):
    class_id: int = Field(..., example=1)
    client_name: str = Field(..., example="John Doe")
    client_email: str = Field(..., example="john@example.com")

    model_config = {
        "json_schema_extra": {
            "examples": [
                {
                    "class_id": 1,
                    "client_name": "John Doe",
                    "client_email": "john@example.com"
                }
            ]
        }
    }

class BookingResponse(BaseModel):
    class_id: int
    client_name: str
    client_email: str

    model_config = {
        "json_schema_extra": {
            "examples": [
                {
                    "class_id": 1,
                    "client_name": "John Doe",
                    "client_email": "john@example.com"
                }
            ]
        }
    }

class ClassResponse(BaseModel):
    id: int
    name: str
    instructor: str
    available_slots: int
    time: str
    timezone: str

    model_config = {
        "json_schema_extra": {
            "examples": [
                {
                    "id": 1,
                    "name": "Yoga",
                    "instructor": "Alice",
                    "available_slots": 5,
                    "time": "2025-06-09 10:00:00",
                    "timezone": "Asia/Kolkata"
                }
            ]
        }
    }
