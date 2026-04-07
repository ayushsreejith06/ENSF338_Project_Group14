"""FIFO incoming request processing feature skeleton."""

from src.interfaces import RequestPipelineProtocol
from src.models.campus import IncomingRequest
from src.structures.fifo_queue import IncomingRequestQueue


class RequestPipeline(RequestPipelineProtocol):
    """Coordinates FIFO processing for incoming requests."""

    def __init__(self, queue: IncomingRequestQueue) -> None:
        """Create the request pipeline with its FIFO queue dependency."""
        raise NotImplementedError

    def submit(self, request: IncomingRequest) -> None:
        """Add an incoming request to the FIFO queue."""
        raise NotImplementedError

    def process_next(self) -> IncomingRequest | None:
        """Remove and return the oldest pending incoming request."""
        raise NotImplementedError

    def pending_count(self) -> int:
        """Return the number of requests waiting to be processed."""
        raise NotImplementedError
