"""Room and event booking system skeleton."""

from typing import Any

from src.models.campus import Booking

# === EXPECTED OUTPUT / BEHAVIOR ===
# Must manage room and event bookings with ordered access.
#
# add_booking(booking) should:
# - Insert booking into system in correct position/order
# - Preserve information to support later queries
#
# remove_booking(booking_id) should:
# - Remove booking by ID
# - Return True if removed, False if not found
#
# get_bookings_in_range(start_time, end_time) should:
# - Return all bookings within requested interval(chronological order)
#
# get_next_event() should:
# - Return next upcoming booking
# - Return None if no upcoming bookings
#
# get_events_for_day(day) should:
# - Return all bookings scheduled for requested day(chronological order)
#
# Booking output shown in main should include:
# - booking_id
# - room_id
# - title
# - start_time
# - end_time
#
# Example printed format:
#   Booking ID: B101
#   Room: ICT-121
#   Title: Study Group
#   Time: 10:00 - 11:00
#
# Internal expectations:
# - Uses ordered booking structure
# - Supports efficient time-based retrieval
# - Scalable for minimum 100 bookings for project testing
class BookingSystem:
    """Coordinates room booking operations against a sorted booking structure."""

    def __init__(self) -> None:
        """Initialize booking system storage dependencies."""
        raise NotImplementedError

    def add_booking(self, booking: Booking) -> None:
        """Add a booking to the system."""
        raise NotImplementedError

    def remove_booking(self, booking_id: str) -> bool:
        """Remove a booking by ID and return whether it was found."""
        raise NotImplementedError

    def get_bookings_in_range(self, start_time: Any, end_time: Any) -> list[Booking]:
        """Return bookings with times inside the requested interval."""
        raise NotImplementedError

    def get_next_event(self) -> Booking | None:
        """Return the next upcoming booking, or None when there are no bookings."""
        raise NotImplementedError

    def get_events_for_day(self, day: Any) -> list[Booking]:
        """Return all bookings scheduled for the given day."""
        raise NotImplementedError
