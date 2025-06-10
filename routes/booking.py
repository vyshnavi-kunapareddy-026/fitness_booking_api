from fastapi import APIRouter, HTTPException, Query
from typing import List
from models import BookingRequest, BookingResponse, ClassResponse
from services.booking_service import (
    get_all_classes_with_timezone,
    create_booking,
    get_bookings_by_email,
    get_classes_service
)

router = APIRouter()

@router.get("/classes", response_model=List[ClassResponse])
def get_classes(tz: str = Query(default="UTC", description="Timezone like Asia/Kolkata")):
    return get_classes_service(tz)

@router.post("/book", response_model=BookingResponse)
def book_class(booking: BookingRequest):
    return create_booking(booking)

@router.get("/bookings", response_model=List[BookingResponse])
def get_bookings(client_email: str):
    return get_bookings_by_email(client_email)
