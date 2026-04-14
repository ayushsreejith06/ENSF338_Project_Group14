"""Persistence and loading helpers for project seed data."""

import csv
import json
from pathlib import Path
from typing import Any

from src.models.campus import Building, Room
from src.structures.graph import Graph


class CampusDataRepository:
    """Loads and saves campus seed data for integration and demos."""

    def __init__(self, data_dir: Path) -> None:
        """Create a repository rooted at a data directory."""
        self._data_dir = Path(data_dir)

    def load_buildings(self) -> list[Building]:
        """Load campus buildings from storage."""
        rows = self._read_csv("buildings.csv", required=True)
        buildings: list[Building] = []

        for row in rows:
            buildings.append(
                Building(
                    building_id=row["building_id"].strip(),
                    name=row["name"].strip(),
                    location=(float(row["latitude"]), float(row["longitude"])),
                )
            )

        return buildings

    def load_rooms(self) -> list[Room]:
        """Load campus rooms from storage."""
        rows = self._read_csv("rooms.csv", required=False)
        rooms: list[Room] = []

        for row in rows:
            rooms.append(
                Room(
                    room_id=row["room_id"].strip(),
                    capacity=int(row["capacity"]),
                    room_type=row["room_type"].strip(),
                )
            )

        return rooms

    def load_resources(self) -> dict[str, Any]:
        """Load lookup resources from storage as key-value pairs."""
        resources_path = self._data_dir / "resources.json"
        if not resources_path.exists():
            return {}

        with resources_path.open("r", encoding="utf-8") as resource_file:
            data = json.load(resource_file)

        if not isinstance(data, dict):
            raise ValueError("resources.json must contain a JSON object.")

        return data

    def load_navigation_graph(self) -> Graph:
        """Load the campus pathway map into an adjacency-list graph."""
        graph = Graph()

        for building in self.load_buildings():
            graph.add_node(building.building_id)

        for row in self._read_csv("pathways.csv", required=True):
            graph.add_edge(
                row["src"].strip(),
                row["dst"].strip(),
                int(row["weight"]),
            )

        return graph

    def _read_csv(self, filename: str, required: bool) -> list[dict[str, str]]:
        """Return CSV rows from the data directory."""
        file_path = self._data_dir / filename
        if not file_path.exists():
            if required:
                raise FileNotFoundError(f"Missing required data file: {file_path}")
            return []

        with file_path.open("r", encoding="utf-8", newline="") as csv_file:
            return list(csv.DictReader(csv_file))
