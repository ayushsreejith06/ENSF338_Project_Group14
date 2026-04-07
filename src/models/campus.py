"""Shared domain models for the campus system.

These dataclasses are intentionally logic-light so feature modules can depend
on them without pulling in UI, demo, or persistence code.
"""

from dataclasses import dataclass, field
from datetime import datetime


@dataclass(slots=True)
class Building:
    """A campus building represented as a graph node."""

    building_id: str
    name: str
    aliases: list[str] = field(default_factory=list)


@dataclass(slots=True)
class Room:
    """A room that can be booked for events."""

    room_id: str
    building_id: str
    name: str
    capacity: int
    resources: list[str] = field(default_factory=list)


@dataclass(slots=True)
class Resource:
    """A searchable campus resource such as equipment or room feature."""

    resource_id: str
    name: str
    location_id: str
    tags: list[str] = field(default_factory=list)


@dataclass(slots=True)
class Event:
    """An event that may be assigned to a room booking."""

    event_id: str
    title: str
    organizer: str
    expected_attendance: int


@dataclass(slots=True)
class Booking:
    """A room booking interval for an event."""

    booking_id: str
    room_id: str
    event: Event
    start_time: datetime
    end_time: datetime


@dataclass(slots=True)
class PathResult:
    """Result of a shortest-path navigation query."""

    building_ids: list[str]
    total_distance: float


@dataclass(slots=True)
class ServiceRequest:
    """A priority-based service request."""

    request_id: str
    title: str
    priority: int
    created_at: datetime
    location_id: str | None = None


@dataclass(slots=True)
class IncomingRequest:
    """A FIFO pipeline request before routing to a feature service."""

    request_id: str
    request_type: str
    payload: dict[str, str]
    received_at: datetime
