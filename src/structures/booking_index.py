"""Internal sorted booking index skeleton."""

from typing import Any

from src.models.campus import Booking


class _BookingIndex:
    """Internal sorted booking structure for room availability queries."""

    def __init__(self) -> None:
        """Initialize booking index storage."""
        raise NotImplementedError

    def _add(self, booking: Booking) -> None:
        """Add a booking to the index."""
        raise NotImplementedError

    def _remove(self, booking_id: str) -> bool:
        """Remove a booking by ID and return whether it was found."""
        raise NotImplementedError

    def _get_bookings_in_range(self, start_time: Any, end_time: Any) -> list[Booking]:
        """Return bookings with times inside the requested interval."""
        raise NotImplementedError
