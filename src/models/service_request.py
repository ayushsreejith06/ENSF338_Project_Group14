from __future__ import annotations

from dataclasses import dataclass, field
from itertools import count
from typing import Literal

PriorityLevel = Literal["Emergency", "Standard", "Low"]

_priority_order = {
    "Emergency": 0,
    "Standard": 1,
    "Low": 2,
}

_request_counter = count(1)


@dataclass(slots=True)
class ServiceRequest:
    """
    Represents a request that can move through the incoming request pipeline
    and/or the service priority queue.
    """
    request_type: str
    description: str
    priority: PriorityLevel = "Standard"
    source: str = "system"
    request_id: int = field(default_factory=lambda: next(_request_counter))
    arrival_sequence: int = field(default=0)

    def priority_rank(self) -> int:
        return _priority_order[self.priority]

    def __str__(self) -> str:
        return (
            f"Request(id={self.request_id}, type={self.request_type}, "
            f"priority={self.priority}, source={self.source}, "
            f"description={self.description})"
        )
