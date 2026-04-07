"""Sorted booking index skeleton."""

from datetime import datetime

from src.models.campus import Booking


class BookingIndex:
    """Sorted booking structure for room availability queries."""

    def __init__(self) -> None:
        """Initialize booking index storage."""
        raise NotImplementedError

    def add(self, booking: Booking) -> None:
        """Add a booking to the index."""
        raise NotImplementedError

    def remove(self, booking_id: str) -> bool:
        """Remove a booking by ID and return whether it was found."""
        raise NotImplementedError

    def for_room(self, room_id: str) -> list[Booking]:
        """Return all bookings for a room."""
        raise NotImplementedError

    def conflicts(
        self,
        room_id: str,
        start_time: datetime,
        end_time: datetime,
    ) -> list[Booking]:
        """Return bookings that conflict with a time interval."""
        raise NotImplementedError
