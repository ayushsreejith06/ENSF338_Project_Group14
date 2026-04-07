"""Room and event booking feature skeleton."""

from datetime import datetime

from src.interfaces import BookingServiceProtocol
from src.models.campus import Booking, Event
from src.structures.booking_index import BookingIndex


class BookingService(BookingServiceProtocol):
    """Coordinates room booking operations against a booking index."""

    def __init__(self, booking_index: BookingIndex) -> None:
        """Create the booking service with its index dependency."""
        raise NotImplementedError

    def create_booking(
        self,
        room_id: str,
        event: Event,
        start_time: datetime,
        end_time: datetime,
    ) -> Booking:
        """Create a booking request for an event in a room."""
        raise NotImplementedError

    def cancel_booking(self, booking_id: str) -> bool:
        """Cancel an existing booking and return whether it was found."""
        raise NotImplementedError

    def bookings_for_room(self, room_id: str) -> list[Booking]:
        """Return bookings associated with one room."""
        raise NotImplementedError

    def is_room_available(
        self,
        room_id: str,
        start_time: datetime,
        end_time: datetime,
    ) -> bool:
        """Return whether a room is available during a time interval."""
        raise NotImplementedError
