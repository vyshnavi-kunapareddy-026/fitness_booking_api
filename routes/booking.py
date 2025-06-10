from fastapi import APIRouter, HTTPException, Query
from typing import List
from models import BookingRequest, BookingResponse, ClassResponse
from services.booking_service import (
    create_booking,
    get_bookings_by_email,
    get_classes_service
)

router = APIRouter()

@router.get("/classes", response_model=List[ClassResponse],tags=["Classes"])
def get_classes(tz: str = Query(default="UTC", description="Timezone like Asia/Kolkata")):
    """
    Retrieve all available fitness classes in the specified timezone.

    - **tz**: Optional. A timezone string (e.g., 'Asia/Kolkata', 'UTC').
    - Returns a list of classes with their time converted to the requested timezone.
    """
    return get_classes_service(tz)

@router.post("/book", response_model=BookingResponse,tags=["Bookings"])
def book_class(booking: BookingRequest):
    """
    Book a spot in a fitness class.

    - **booking**: Request body including class ID, client name, and email.
    - Decreases available slots for the class if successful.
    - Returns booking confirmation.
    """
    return create_booking(booking)

@router.get("/bookings", response_model=List[BookingResponse],tags=["Bookings"])
def get_bookings(client_email: str):
    """
    Retrieve all bookings for a given email.

    - **client_email**: Email address of the client.
    - Returns a list of all classes the client has booked.
    """
    return get_bookings_by_email(client_email)
