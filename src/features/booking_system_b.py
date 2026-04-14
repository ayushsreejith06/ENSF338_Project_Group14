"""
Booking System (src/features/booking_system_b.py)
Author: Rolanted

Note: This is a continuation of booking_system.py file made by Leo.
      This includes:
      * next upcoming event
      * events for a specific day
"""

from datetime import datetime
from typing import Optional

from ..models.campus import Booking


def get_next_event(self) -> Optional[Booking]:
    """
    Return the next relevant event based on the current time.

    If an event is currently ongoing, it is returned.
    Otherwise, the next future event is returned.
    Returns None if there are no current or upcoming events.
    """
    now = datetime.now()

    for booking in self._sorted_bookings:
        if booking.end_time >= now:
            return booking

    return None

# More codes here...