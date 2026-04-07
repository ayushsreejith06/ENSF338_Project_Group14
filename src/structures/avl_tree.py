"""Optional AVL tree skeleton for the booking index bonus."""

from typing import Any

from src.models.campus import Booking


class AVLTree:
    """Optional balanced booking index keyed by booking time."""

    def __init__(self) -> None:
        """Initialize AVL tree storage."""
        raise NotImplementedError

    def insert(self, booking: Booking) -> None:
        """Insert a booking into the AVL tree."""
        raise NotImplementedError

    def search_in_range(self, start_time: Any, end_time: Any) -> list[Booking]:
        """Return bookings with times inside the requested interval."""
        raise NotImplementedError
