"""Persistence and loading boundary skeletons.

Feature modules should not read files directly; integrate data loading here.
"""

from pathlib import Path
from typing import Any

from src.models.campus import Building, Room


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

    def load_resources(self) -> dict[str, Any]:
        """Load lookup resources from storage as key-value pairs."""
        raise NotImplementedError
