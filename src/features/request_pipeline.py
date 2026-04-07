"""FIFO incoming request processing pipeline skeleton."""

from typing import Any


class RequestPipeline:
    """Coordinates FIFO processing for incoming requests."""

    def __init__(self) -> None:
        """Initialize request pipeline storage."""
        raise NotImplementedError

    def enqueue(self, request: Any) -> None:
        """Add a request to the back of the FIFO pipeline."""
        raise NotImplementedError

    def dequeue(self) -> Any | None:
        """Remove and return the oldest request in the FIFO pipeline."""
        raise NotImplementedError

    def process_next(self) -> Any | None:
        """Process and return the oldest pending request."""
        raise NotImplementedError
