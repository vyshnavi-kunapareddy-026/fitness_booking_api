# utils/timezone.py

from typing import Dict
import pytz
from datetime import datetime
from fastapi import HTTPException

def convert_to_timezone(class_info: Dict, tz: str) -> Dict:
    """
    Converts the 'time' field in the class object to the specified timezone.

    Args:
        class_obj (dict): Class dictionary with UTC datetime.
        tz (str): Target timezone string.

    Returns:
        dict: Updated class object with timezone-aware datetime.

    Raises:
        Exception: If timezone conversion fails.
    """
    try:
        user_tz = pytz.timezone(tz)
    except pytz.UnknownTimeZoneError:
        raise HTTPException(status_code=400, detail="Invalid timezone")

    try:
        # Copy class info to avoid mutating the original data
        class_copy = class_info.copy()

        class_datetime = class_copy.get("datetime")
        if not isinstance(class_datetime, datetime):
            raise ValueError("'datetime' field must be a datetime object")

        # Ensure datetime is timezone-aware before conversion
        if class_datetime.tzinfo is None:
            raise ValueError("Datetime must be timezone-aware")

        # Convert to requested timezone
        class_copy["datetime"] = class_datetime.astimezone(user_tz)
        return class_copy
    except Exception as e:
        print("Timezone conversion error:", str(e))
        raise HTTPException(status_code=400, detail="Failed to convert class time to requested timezone")
