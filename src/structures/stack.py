"""Internal stack implementation for navigation undo history."""


class _NavigationHistory:
    """Internal LIFO stack of recently completed routes."""

    def __init__(self) -> None:
        """Initialize stack storage."""
        self._routes: list[tuple[list[str], int]] = []

    def _push(self, route: tuple[list[str], int]) -> None:
        """Push a route result onto the history stack."""
        self._routes.append(route)

    def _pop(self) -> tuple[list[str], int] | None:
        """Pop the most recent route, if any."""
        if self._is_empty():
            return None
        return self._routes.pop()

    def _peek(self) -> tuple[list[str], int] | None:
        """Return the most recent route without removing it."""
        if self._is_empty():
            return None
        return self._routes[-1]

    def _is_empty(self) -> bool:
        """Return whether the history stack is empty."""
        return len(self._routes) == 0
