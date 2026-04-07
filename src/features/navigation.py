"""Shortest-path navigation manager skeleton."""

from src.structures.graph import Graph


class NavigationManager:
    """Coordinates Dijkstra navigation and route undo history."""

    def __init__(self, graph: Graph) -> None:
        """Create a navigation manager with a campus graph dependency."""
        raise NotImplementedError

    def navigate(self, src: str, dst: str) -> tuple[list[str], int]:
        """Return the shortest route and distance from src to dst."""
        raise NotImplementedError

    def undo(self) -> str | None:
        """Undo the most recent navigation action and return a status message."""
        raise NotImplementedError
