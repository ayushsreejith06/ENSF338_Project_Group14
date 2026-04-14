"""
Booking System (src/features/booking_system_b.py)
Author: Rolanted

Note: This is a continuation of the booking_system.py file made by Leo.
This file includes:
* next upcoming event
* events for a specific day
"""

from datetime import datetime, date
from typing import Optional, List

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


def get_events_for_day(self, day: date) -> List[Booking]:
    """
    Return all bookings scheduled on the given day
    in chronological order.
    """
    events_for_day: List[Booking] = []

    for booking in self._sorted_bookings:
        if booking.start_time.date() == day:
            events_for_day.append(booking)

    return events_for_day