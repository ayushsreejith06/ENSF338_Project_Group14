"""Shortest-path navigation manager skeleton."""

from src.structures.graph import Graph

# === EXPECTED OUTPUT / BEHAVIOR ===
# Must provide shortest-path navigation between two locations.
#
# navigate(src, dst):
# - Return shortest path as ordered list of node/building IDs
#   Example:
#       ["ICT", "ENG", "SCI"]
#
# - Return total path cost (distance or time)
#   Example:
#       12
#
# - Final output format should be close to:
#       Path: ICT -> ENG -> SCI
#       Cost: 12
#
#
# undo():
# - Reverts most recent navigation operation
# - Return message describing the action completed:
#   Example:
#       "Reverted to previous location: ICT"
#
# Internal expectations:
# - Graph-based implementation (adjacency list)
# - Dijkstra’s algorithm for shortest path
# - Stack used to track navigation history for undo
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
