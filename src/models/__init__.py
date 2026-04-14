"""Shared data models used across feature modules."""

from .campus import Booking, Building, Campus, Room
from ..features.booking_system import BookingSystem

__all__ = [
    "Booking",
    "Building",
    "Campus",
    "Room",
    "BookingSystem",
]
