"""Shortest-path navigation feature skeleton."""

from src.interfaces import CampusMapProtocol, NavigationServiceProtocol
from src.models.campus import PathResult
from src.structures.stack import NavigationHistory


class NavigationService(NavigationServiceProtocol):
    """Coordinates Dijkstra shortest paths and route undo history."""

    def __init__(self, campus_map: CampusMapProtocol, history: NavigationHistory) -> None:
        """Create the navigation service with graph and history dependencies."""
        raise NotImplementedError

    def shortest_path(self, start_id: str, end_id: str) -> PathResult:
        """Return the shortest path between two buildings."""
        raise NotImplementedError

    def record_route(self, route: PathResult) -> None:
        """Push a completed route onto the navigation history stack."""
        raise NotImplementedError

    def undo_last_route(self) -> PathResult | None:
        """Pop and return the most recent route, if any."""
        raise NotImplementedError
