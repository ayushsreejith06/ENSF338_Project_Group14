from typing import Any

from src.structures.hash_index import HashIndex


class LookupService:
    """Feature-level service for fast key-based lookup of project resources."""

    def __init__(self) -> None:
        self._index = HashIndex()

    def insert(self, key: str, value: Any) -> None:
        """Insert or update a value by key."""
        self._index.insert(key, value)

    def lookup(self, key: str) -> Any | None:
        """Return the value for a key, or None if not found."""
        return self._index.lookup(key)

    def delete(self, key: str) -> bool:
        """Delete a key if it exists. Return True if removed, else False."""
        return self._index.delete(key)

    def contains(self, key: str) -> bool:
        """Return True if the key exists."""
        return self._index.contains(key)

    def size(self) -> int:
        """Return the number of stored items."""
        return self._index.size()