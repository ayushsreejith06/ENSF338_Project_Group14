"""Shortest-path navigation manager implementation."""

from src.structures.graph import Graph
from src.structures.stack import _NavigationHistory


class NavigationManager:
    """Coordinates Dijkstra navigation and route undo history."""

    def __init__(self, graph: Graph) -> None:
        """Create a navigation manager with a campus graph dependency."""
        self._graph = graph
        self._history = _NavigationHistory()
        self._current_route: tuple[list[str], int] | None = None

    def navigate(self, src: str, dst: str) -> tuple[list[str], int]:
        """Return the shortest route and distance from src to dst."""
        route = self._graph.shortest_path(src, dst)
        self._history._push(route)
        self._current_route = route
        return route

    def undo(self) -> str | None:
        """Undo the most recent navigation action and return a status message."""
        removed_route = self._history._pop()
        if removed_route is None:
            return None

        self._current_route = self._history._peek()

        removed_path, removed_cost = removed_route
        removed_summary = f"{' -> '.join(removed_path)} ({removed_cost} minutes)"

        if self._current_route is None:
            return f"Undid route {removed_summary}. No active route remains."

        restored_path, restored_cost = self._current_route
        restored_summary = f"{' -> '.join(restored_path)} ({restored_cost} minutes)"
        return (
            f"Undid route {removed_summary}. "
            f"Restored previous route {restored_summary}."
        )
