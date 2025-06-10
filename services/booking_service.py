from typing import List
from fastapi import HTTPException
from models import BookingRequest, BookingResponse, ClassResponse
from seed_data import classes, bookings
from utils.timezone import convert_to_timezone
import logging

logger = logging.getLogger("main")



def get_classes_service(tz: str = "UTC") -> list[ClassResponse]:
    """
    Converts all class times to the given timezone and returns class data.

    Args:
        tz (str): Timezone string (e.g., 'Asia/Kolkata').

    Returns:
        List of ClassResponse objects with localized times.
    """
    from seed_data import classes

    converted_classes = []
    for cls in classes:
        converted = convert_to_timezone(cls, tz)
        class_time = converted["datetime"]

        converted_classes.append(
            ClassResponse(
                id=converted["id"],
                name=converted["name"],
                instructor=converted["instructor"],
                available_slots=converted["available_slots"],
                time=class_time.strftime("%Y-%m-%d %H:%M:%S"),
                timezone=tz,
            )
        )
    return converted_classes


def create_booking(booking: BookingRequest) -> BookingResponse:
    """
    Books a class for a user if slots are available.

    Args:
        booking (BookingRequest): The booking request data.

    Returns:
        BookingResponse: The booking confirmation.

    Raises:
        HTTPException: If class is not found or no slots are available.
    """
    for c in classes:
        if c["id"] == booking.class_id:
            # Check if slots are available
            if c.get("available_slots", 0) <= 0:
                raise HTTPException(status_code=400, detail="No slots available for this class")

            # Decrease available slots
            c["available_slots"] -= 1

            new_booking = {
                "class_id": booking.class_id,
                "client_name": booking.client_name,
                "client_email": booking.client_email
            }

            bookings.append(new_booking)
            logger.info(f"New booking by {booking.client_name} for class {c['name']}")
            return BookingResponse(**new_booking)

    raise HTTPException(status_code=404, detail="Class not found")


def get_bookings_by_email(client_email: str) -> List[BookingResponse]:
    """
    Retrieves all bookings made by a specific email.

    Args:
        client_email (str): The client's email.

    Returns:
        List[BookingResponse]: List of booking objects.

    Raises:
        HTTPException: If no bookings are found for the email.
    """
    filtered = [BookingResponse(**b) for b in bookings if b["client_email"] == client_email]
    if not filtered:
        raise HTTPException(status_code=404, detail="No bookings found for this email")
    return filtered
