# seed_data.py

from datetime import datetime, timedelta
import pytz

IST = pytz.timezone("Asia/Kolkata")
now = datetime.now()

classes = [
    {
        "id": 1,
        "name": "Yoga",
        "instructor": "Anjali Sharma",
        "datetime": IST.localize(now + timedelta(days=1, hours=8)),
        "available_slots": 5,
    },
    {
        "id": 2,
        "name": "Zumba",
        "instructor": "Rahul Mehra",
        "datetime": IST.localize(now + timedelta(days=2, hours=10)),
        "available_slots": 8,
    },
    {
        "id": 3,
        "name": "HIIT",
        "instructor": "Sneha Roy",
        "datetime": IST.localize(now + timedelta(days=3, hours=7)),
        "available_slots": 4,
    },
]

bookings = []
