from __future__ import annotations

from collections import deque
from typing import Deque, Optional

from src.models.service_request import ServiceRequest


class RequestPipeline:
    """
    FIFO queue for incoming requests.
    Requests are processed strictly in arrival order.
    """

    def __init__(self) -> None:
        self._queue: Deque[ServiceRequest] = deque()

    def enqueue(self, req: ServiceRequest) -> None:
        self._queue.append(req)

    def dequeue(self) -> Optional[ServiceRequest]:
        if self.is_empty():
            return None
        return self._queue.popleft()

    def process_next(self) -> Optional[ServiceRequest]:
        return self.dequeue()

    def is_empty(self) -> bool:
        return len(self._queue) == 0

    def __len__(self) -> int:
        return len(self._queue)

    def snapshot(self) -> list[ServiceRequest]:
        return list(self._queue)
