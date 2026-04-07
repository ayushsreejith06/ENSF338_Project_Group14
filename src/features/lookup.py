"""Fast hash-table-style lookup service skeleton."""

from typing import Any


class LookupService:
    """Stores and retrieves values by string key."""

    def __init__(self) -> None:
        """Initialize lookup storage."""
        raise NotImplementedError

    def insert(self, key: str, value: Any) -> None:
        """Insert or replace a value by key."""
        raise NotImplementedError

    def lookup(self, key: str) -> Any | None:
        """Return the value for key, or None when the key is missing."""
        raise NotImplementedError

    def delete(self, key: str) -> bool:
        """Delete a key and return whether it was found."""
        raise NotImplementedError
