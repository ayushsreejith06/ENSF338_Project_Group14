"""Navigation-focused demo runner.

Keep demo wiring here instead of crowding a shared main.py during parallel work.
"""

from pathlib import Path

from src.features.navigation import NavigationManager
from src.io.repositories import CampusDataRepository
from src.models.campus import Building


def run_demo() -> None:
    """Run the current navigation demo from repository-backed map data."""
    data_dir = Path(__file__).resolve().parents[2] / "data"
    repository = CampusDataRepository(data_dir)
    buildings = {
        building.building_id: building for building in repository.load_buildings()
    }
    navigation_manager = NavigationManager(repository.load_navigation_graph())

    print("Campus Navigation Demo")
    print("======================")

    for src, dst in [("ENG", "ST"), ("EEEL", "ST")]:
        path, total_time = navigation_manager.navigate(src, dst)
        print(f"Route: {_building_label(src, buildings)} -> {_building_label(dst, buildings)}")
        print(f"Path: {_format_path(path, buildings)}")
        print(f"Total time: {total_time} minutes")
        print()

    print(navigation_manager.undo() or "No route available to undo.")


def _format_path(path: list[str], buildings: dict[str, Building]) -> str:
    """Format a route using both building names and IDs."""
    return " -> ".join(_building_label(building_id, buildings) for building_id in path)


def _building_label(building_id: str, buildings: dict[str, Building]) -> str:
    """Return a printable building label for a route segment."""
    building = buildings[building_id]
    return f"{building.name} ({building.building_id})"


if __name__ == "__main__":
    run_demo()
