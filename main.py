# main.py
from fastapi import FastAPI, HTTPException, Query
from typing import List, Optional
from database import fitness_classes, bookings
from schemas import FitnessClass, BookingRequest, Booking
import logging
import pytz
from seed_data import classes

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

app = FastAPI(title="Fitness Studio Booking API")

@app.get("/classes", response_model=List[FitnessClass])
def get_classes(tz: Optional[str] = Query(default="Asia/Kolkata")):
    try:
        user_tz = pytz.timezone(tz)
    except pytz.UnknownTimeZoneError:
        raise HTTPException(status_code=400, detail="Invalid timezone")

    converted_classes = []
    for cls in classes:
        # Clone the class object to avoid mutating seed data
        cls_copy = cls.copy()
        original_dt = cls_copy["datetime"]
        # Convert IST to requested timezone
        cls_copy["datetime"] = original_dt.astimezone(user_tz)
        converted_classes.append(cls_copy)

    return converted_classes

@app.post("/book")
def book_class(booking: BookingRequest):
    class_item = next((c for c in fitness_classes if c["id"] == booking.class_id), None)

    # Edge Case 1: Invalid class ID
    if not class_item:
        raise HTTPException(status_code=404, detail="Class not found")

    # Edge Case 2: No slots available
    if class_item["available_slots"] <= 0:
        raise HTTPException(status_code=400, detail="No slots available for this class")

    # If everything is okay, proceed with booking
    class_item["available_slots"] -= 1

    new_booking = {
        "class_id": booking.class_id,
        "client_name": booking.client_name,
        "client_email": booking.client_email,
    }

    bookings.append(new_booking)
    logger.info(f"New booking by {booking.client_name} for class {class_item['name']}")
    return {"message": "Booking successful", "booking": new_booking}

@app.get("/bookings")
def get_bookings(client_email: str):
    print("All bookings:", bookings)  # debug line
    filtered = [booking for booking in bookings if booking['client_email'] == client_email]
    if not filtered:
        raise HTTPException(status_code=404, detail="No bookings found for this email")
    print("Filtered bookings:", filtered)  # debug line
    return filtered

