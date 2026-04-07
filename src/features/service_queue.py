"""Priority-based service queue feature skeleton."""

from src.interfaces import ServiceQueueProtocol
from src.models.campus import ServiceRequest
from src.structures.priority_queue import ServicePriorityQueue


class ServiceQueueService(ServiceQueueProtocol):
    """Coordinates priority-based campus service requests."""

    def __init__(self, queue: ServicePriorityQueue) -> None:
        """Create the service queue feature with its priority queue dependency."""
        raise NotImplementedError

    def enqueue(self, request: ServiceRequest) -> None:
        """Add a service request to the priority queue."""
        raise NotImplementedError

    def dequeue(self) -> ServiceRequest | None:
        """Remove and return the highest-priority service request."""
        raise NotImplementedError

    def peek(self) -> ServiceRequest | None:
        """Return the next service request without removing it."""
        raise NotImplementedError
