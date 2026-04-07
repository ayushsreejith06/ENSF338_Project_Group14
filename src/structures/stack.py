"""Stack skeleton for navigation undo history."""

from src.models.campus import PathResult


class NavigationHistory:
    """LIFO stack of recently completed routes."""

    def __init__(self) -> None:
        """Initialize stack storage."""
        raise NotImplementedError

    def push(self, route: PathResult) -> None:
        """Push a route onto the history stack."""
        raise NotImplementedError

    def pop(self) -> PathResult | None:
        """Pop the most recent route, if any."""
        raise NotImplementedError

    def peek(self) -> PathResult | None:
        """Return the most recent route without removing it."""
        raise NotImplementedError

    def is_empty(self) -> bool:
        """Return whether the history stack is empty."""
        raise NotImplementedError
