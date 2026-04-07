"""Fast building, room, and resource lookup feature skeleton."""

from src.interfaces import LookupServiceProtocol
from src.models.campus import Building, Resource, Room


class LookupService(LookupServiceProtocol):
    """Hash-table-style lookup service for campus entities."""

    def __init__(self) -> None:
        """Initialize lookup indexes."""
        raise NotImplementedError

    def add_building(self, building: Building) -> None:
        """Register a building for fast lookup."""
        raise NotImplementedError

    def add_room(self, room: Room) -> None:
        """Register a room for fast lookup."""
        raise NotImplementedError

    def add_resource(self, resource: Resource) -> None:
        """Register a resource for fast lookup."""
        raise NotImplementedError

    def find_building(self, building_id: str) -> Building | None:
        """Find a building by ID."""
        raise NotImplementedError

    def find_room(self, room_id: str) -> Room | None:
        """Find a room by ID."""
        raise NotImplementedError

    def find_resources(self, query: str) -> list[Resource]:
        """Find resources matching a search query."""
        raise NotImplementedError
