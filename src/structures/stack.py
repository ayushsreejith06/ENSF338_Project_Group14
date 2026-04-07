"""Internal stack skeleton for navigation undo history."""


class _NavigationHistory:
    """Internal LIFO stack of recently completed routes."""

    def __init__(self) -> None:
        """Initialize stack storage."""
        raise NotImplementedError

    def _push(self, route: tuple[list[str], int]) -> None:
        """Push a route result onto the history stack."""
        raise NotImplementedError

    def _pop(self) -> tuple[list[str], int] | None:
        """Pop the most recent route, if any."""
        raise NotImplementedError

    def _is_empty(self) -> bool:
        """Return whether the history stack is empty."""
        raise NotImplementedError
