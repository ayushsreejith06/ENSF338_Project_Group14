"""Shared data models for the campus navigation and event system.

These models are intentionally logic-light. Feature modules may import them,
but model classes must not import feature, structure, demo, or I/O modules.
"""

from dataclasses import dataclass, field
from typing import Any


@dataclass(slots=True)
class Room:
    """A room that can be searched and booked for events."""

    room_id: str
    capacity: int
    room_type: str


@dataclass(slots=True)
class Building:
    """A campus building represented as a graph node."""

    building_id: str
    name: str
    location: tuple[float, float]
    rooms: list[Room] = field(default_factory=list)


@dataclass(slots=True)
class Booking:
    """A room booking interval for an event."""

    booking_id: str
    room_id: str
    title: str
    start_time: Any
    end_time: Any
    organizer: str


@dataclass(slots=True)
class Campus:
    """Container for shared campus data used by feature services."""

    buildings: dict[str, Building] = field(default_factory=dict)
    rooms: dict[str, Room] = field(default_factory=dict)
    bookings: dict[str, Booking] = field(default_factory=dict)
