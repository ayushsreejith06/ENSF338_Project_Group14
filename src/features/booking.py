"""Room and event booking system skeleton."""

from typing import Any

from src.models.campus import Booking


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
