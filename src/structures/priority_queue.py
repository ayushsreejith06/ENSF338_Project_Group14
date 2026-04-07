"""Priority queue skeleton for service requests."""

from src.models.campus import ServiceRequest


class ServicePriorityQueue:
    """Priority queue for service requests."""

    def __init__(self) -> None:
        """Initialize priority queue storage."""
        raise NotImplementedError

    def enqueue(self, request: ServiceRequest) -> None:
        """Add a service request to the queue."""
        raise NotImplementedError

    def dequeue(self) -> ServiceRequest | None:
        """Remove and return the highest-priority request."""
        raise NotImplementedError

    def peek(self) -> ServiceRequest | None:
        """Return the highest-priority request without removing it."""
        raise NotImplementedError

    def is_empty(self) -> bool:
        """Return whether the queue has no requests."""
        raise NotImplementedError
