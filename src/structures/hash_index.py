from typing import Any


class HashIndex:
    """Simple dictionary-backed index for fast key-based lookup."""

    def __init__(self) -> None:
        self._store: dict[str, Any] = {}

    def insert(self, key: str, value: Any) -> None:
        """Insert or update a value by key."""
        self._store[key] = value

    def lookup(self, key: str) -> Any | None:
        """Return the value for a key, or None if it does not exist."""
        return self._store.get(key)

    def delete(self, key: str) -> bool:
        """Delete a key if it exists. Return True if removed, else False."""
        if key in self._store:
            del self._store[key]
            return True
        return False

    def contains(self, key: str) -> bool:
        """Return True if the key exists in the index."""
        return key in self._store

    def size(self) -> int:
        """Return the number of stored key/value pairs."""
        return len(self._store)