"""Persistence and loading boundary skeletons.

Feature modules should not read files directly; integrate data loading here.
"""

from pathlib import Path

from src.models.campus import Building, Resource, Room


class CampusDataRepository:
    """Loads and saves campus seed data for integration and demos."""

    def __init__(self, data_dir: Path) -> None:
        """Create a repository rooted at a data directory."""
        raise NotImplementedError

    def load_buildings(self) -> list[Building]:
        """Load campus buildings from storage."""
        raise NotImplementedError

    def load_rooms(self) -> list[Room]:
        """Load campus rooms from storage."""
        raise NotImplementedError

    def load_resources(self) -> list[Resource]:
        """Load campus resources from storage."""
        raise NotImplementedError
