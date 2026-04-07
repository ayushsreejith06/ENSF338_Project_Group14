"""Adjacency-list campus graph skeleton."""

from src.interfaces import CampusMapProtocol
from src.models.campus import Building


class CampusGraph(CampusMapProtocol):
    """Campus map backed by an adjacency list."""

    def __init__(self) -> None:
        """Initialize graph storage."""
        raise NotImplementedError

    def add_building(self, building: Building) -> None:
        """Add or replace a building node in the campus graph."""
        raise NotImplementedError

    def add_path(self, source_id: str, destination_id: str, distance: float) -> None:
        """Add a weighted path between two buildings."""
        raise NotImplementedError

    def neighbors(self, building_id: str) -> list[tuple[str, float]]:
        """Return neighboring building IDs and edge weights."""
        raise NotImplementedError

    def get_building(self, building_id: str) -> Building | None:
        """Return a building by ID, or None when missing."""
        raise NotImplementedError
