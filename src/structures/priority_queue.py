"""Priority queue skeleton for service requests."""

from typing import Any


class ServicePriorityQueue:
    """Priority queue for campus service requests."""

    def __init__(self) -> None:
        """Initialize priority queue storage."""
        raise NotImplementedError

    def enqueue(self, request: Any) -> None:
        """Add a request to the priority queue."""
        raise NotImplementedError

    def dequeue(self) -> Any | None:
        """Remove and return the highest-priority request."""
        raise NotImplementedError

    def is_empty(self) -> bool:
        """Return whether the priority queue has no requests."""
        raise NotImplementedError
