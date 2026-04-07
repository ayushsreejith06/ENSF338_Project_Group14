"""Adjacency-list graph skeleton for campus navigation."""


class Graph:
    """Campus graph using building IDs as nodes."""

    def __init__(self) -> None:
        """Initialize adjacency-list graph storage."""
        raise NotImplementedError

    def add_node(self, building_id: str) -> None:
        """Add a building node to the graph if it is not already present."""
        raise NotImplementedError

    def add_edge(self, src: str, dst: str, weight: int) -> None:
        """Add a weighted edge between two building IDs."""
        raise NotImplementedError

    def shortest_path(self, src: str, dst: str) -> tuple[list[str], int]:
        """Return the shortest path and total distance from src to dst."""
        raise NotImplementedError
