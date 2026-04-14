"""Adjacency-list graph implementation for campus navigation."""

from heapq import heappop, heappush


class Graph:
    """Campus graph using building IDs as nodes."""

    def __init__(self) -> None:
        """Initialize adjacency-list graph storage."""
        self._adjacency: dict[str, dict[str, int]] = {}

    def add_node(self, building_id: str) -> None:
        """Add a building node to the graph if it is not already present."""
        if building_id not in self._adjacency:
            self._adjacency[building_id] = {}

    def add_edge(self, src: str, dst: str, weight: int) -> None:
        """Add a weighted edge between two building IDs."""
        if weight < 0:
            raise ValueError("Dijkstra requires non-negative edge weights.")

        self.add_node(src)
        self.add_node(dst)

        # campus walkways are bidirectional
        self._adjacency[src][dst] = weight
        self._adjacency[dst][src] = weight

    def shortest_path(self, src: str, dst: str) -> tuple[list[str], int]:
        """Return the shortest path and total distance from src to dst."""
        if src not in self._adjacency:
            raise ValueError(f"Unknown source building: {src}")
        if dst not in self._adjacency:
            raise ValueError(f"Unknown destination building: {dst}")
        if src == dst:
            return [src], 0

        distances: dict[str, int] = {src: 0}
        previous: dict[str, str] = {}
        queue: list[tuple[int, str]] = [(0, src)]
        visited: set[str] = set()

        while queue:
            current_cost, current_node = heappop(queue)

            if current_node in visited:
                continue

            visited.add(current_node)

            if current_node == dst:
                break

            for neighbor, edge_weight in self._adjacency[current_node].items():
                next_cost = current_cost + edge_weight

                if next_cost < distances.get(neighbor, float("inf")):
                    distances[neighbor] = next_cost
                    previous[neighbor] = current_node
                    heappush(queue, (next_cost, neighbor))

        if dst not in distances:
            raise ValueError(f"No path exists between {src} and {dst}.")

        path = [dst]
        while path[-1] != src:
            path.append(previous[path[-1]])
        path.reverse()

        return path, distances[dst]
