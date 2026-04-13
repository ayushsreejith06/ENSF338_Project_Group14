from __future__ import annotations

import heapq
from typing import List, Optional, Tuple

from src.models.service_request import ServiceRequest


class ServicePriorityQueue:
    """
    Min-heap based priority queue.

    Lower numeric priority rank means higher urgency:
    Emergency < Standard < Low

    Ties are broken by arrival_sequence so that equal-priority requests
    are still served in FIFO order.
    """

    def __init__(self) -> None:
        self._heap: List[Tuple[int, int, ServiceRequest]] = []
        self._sequence_counter = 0

    def enqueue(self, req: ServiceRequest) -> None:
        self._sequence_counter += 1
        req.arrival_sequence = self._sequence_counter
        entry = (req.priority_rank(), req.arrival_sequence, req)
        heapq.heappush(self._heap, entry)

    def dequeue(self) -> Optional[ServiceRequest]:
        if self.is_empty():
            return None
        _, _, req = heapq.heappop(self._heap)
        return req

    def peek(self) -> Optional[ServiceRequest]:
        if self.is_empty():
            return None
        return self._heap[0][2]

    def is_empty(self) -> bool:
        return len(self._heap) == 0

    def __len__(self) -> int:
        return len(self._heap)

    def snapshot(self) -> list[ServiceRequest]:
        return [entry[2] for entry in sorted(self._heap)]
