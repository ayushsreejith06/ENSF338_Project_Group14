import json
from pathlib import Path
from typing import Any


def load_buildings_seed() -> list[dict[str, Any]]:
    """Load shared building seed data from JSON."""
    data_path = Path("data/buildings_seed.json")

    with data_path.open("r", encoding="utf-8") as file:
        return json.load(file)