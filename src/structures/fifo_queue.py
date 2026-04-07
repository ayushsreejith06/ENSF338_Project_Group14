"""Internal FIFO queue skeleton for incoming request processing."""

from typing import Any


class _IncomingRequestQueue:
    """Internal first-in, first-out queue for incoming requests."""

    def __init__(self) -> None:
        """Initialize FIFO queue storage."""
        raise NotImplementedError

    def _enqueue(self, request: Any) -> None:
        """Add a request to the back of the queue."""
        raise NotImplementedError

    def _dequeue(self) -> Any | None:
        """Remove and return the oldest request."""
        raise NotImplementedError

    def __len__(self) -> int:
        """Return the number of queued requests."""
        raise NotImplementedError
