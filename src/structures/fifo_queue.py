"""FIFO queue skeleton for incoming request processing."""

from src.models.campus import IncomingRequest


class IncomingRequestQueue:
    """First-in, first-out queue for incoming requests."""

    def __init__(self) -> None:
        """Initialize FIFO queue storage."""
        raise NotImplementedError

    def enqueue(self, request: IncomingRequest) -> None:
        """Add a request to the back of the queue."""
        raise NotImplementedError

    def dequeue(self) -> IncomingRequest | None:
        """Remove and return the oldest request."""
        raise NotImplementedError

    def peek(self) -> IncomingRequest | None:
        """Return the oldest request without removing it."""
        raise NotImplementedError

    def __len__(self) -> int:
        """Return the number of queued requests."""
        raise NotImplementedError
