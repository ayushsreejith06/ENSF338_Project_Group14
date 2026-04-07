"""Frozen public interfaces for feature modules.

Teammates should implement these contracts without renaming public methods.
"""

from abc import ABC, abstractmethod
from datetime import datetime

from src.models.campus import (
    Booking,
    Building,
    Event,
    IncomingRequest,
    PathResult,
    Resource,
    Room,
    ServiceRequest,
)


class CampusMapProtocol(ABC):
    """Public API for campus graph storage and traversal support."""

    @abstractmethod
    def add_building(self, building: Building) -> None:
        """Add or replace a building node in the campus graph."""
        raise NotImplementedError

    @abstractmethod
    def add_path(self, source_id: str, destination_id: str, distance: float) -> None:
        """Add a weighted path between two buildings."""
        raise NotImplementedError

    @abstractmethod
    def neighbors(self, building_id: str) -> list[tuple[str, float]]:
        """Return neighboring building IDs and edge weights."""
        raise NotImplementedError

    @abstractmethod
    def get_building(self, building_id: str) -> Building | None:
        """Return a building by ID, or None when missing."""
        raise NotImplementedError


class NavigationServiceProtocol(ABC):
    """Public API for shortest-path navigation and undo history."""

    @abstractmethod
    def shortest_path(self, start_id: str, end_id: str) -> PathResult:
        """Return the shortest path between two buildings."""
        raise NotImplementedError

    @abstractmethod
    def record_route(self, route: PathResult) -> None:
        """Push a completed route onto the navigation history stack."""
        raise NotImplementedError

    @abstractmethod
    def undo_last_route(self) -> PathResult | None:
        """Pop and return the most recent route, if any."""
        raise NotImplementedError


class BookingServiceProtocol(ABC):
    """Public API for room and event booking."""

    @abstractmethod
    def create_booking(
        self,
        room_id: str,
        event: Event,
        start_time: datetime,
        end_time: datetime,
    ) -> Booking:
        """Create a booking request for an event in a room."""
        raise NotImplementedError

    @abstractmethod
    def cancel_booking(self, booking_id: str) -> bool:
        """Cancel an existing booking and return whether it was found."""
        raise NotImplementedError

    @abstractmethod
    def bookings_for_room(self, room_id: str) -> list[Booking]:
        """Return bookings associated with one room."""
        raise NotImplementedError

    @abstractmethod
    def is_room_available(
        self,
        room_id: str,
        start_time: datetime,
        end_time: datetime,
    ) -> bool:
        """Return whether a room is available during a time interval."""
        raise NotImplementedError


class ServiceQueueProtocol(ABC):
    """Public API for priority-based campus service requests."""

    @abstractmethod
    def enqueue(self, request: ServiceRequest) -> None:
        """Add a service request to the priority queue."""
        raise NotImplementedError

    @abstractmethod
    def dequeue(self) -> ServiceRequest | None:
        """Remove and return the highest-priority service request."""
        raise NotImplementedError

    @abstractmethod
    def peek(self) -> ServiceRequest | None:
        """Return the next service request without removing it."""
        raise NotImplementedError


class LookupServiceProtocol(ABC):
    """Public API for hash-table-style building and resource lookup."""

    @abstractmethod
    def add_building(self, building: Building) -> None:
        """Register a building for fast lookup."""
        raise NotImplementedError

    @abstractmethod
    def add_room(self, room: Room) -> None:
        """Register a room for fast lookup."""
        raise NotImplementedError

    @abstractmethod
    def add_resource(self, resource: Resource) -> None:
        """Register a resource for fast lookup."""
        raise NotImplementedError

    @abstractmethod
    def find_building(self, building_id: str) -> Building | None:
        """Find a building by ID."""
        raise NotImplementedError

    @abstractmethod
    def find_room(self, room_id: str) -> Room | None:
        """Find a room by ID."""
        raise NotImplementedError

    @abstractmethod
    def find_resources(self, query: str) -> list[Resource]:
        """Find resources matching a search query."""
        raise NotImplementedError


class RequestPipelineProtocol(ABC):
    """Public API for FIFO incoming request processing."""

    @abstractmethod
    def submit(self, request: IncomingRequest) -> None:
        """Add an incoming request to the FIFO queue."""
        raise NotImplementedError

    @abstractmethod
    def process_next(self) -> IncomingRequest | None:
        """Remove and return the oldest pending incoming request."""
        raise NotImplementedError

    @abstractmethod
    def pending_count(self) -> int:
        """Return the number of requests waiting to be processed."""
        raise NotImplementedError
