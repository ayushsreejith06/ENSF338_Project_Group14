"""Optional AVL tree skeleton for the booking index bonus."""

from typing import Generic, TypeVar

K = TypeVar("K")
V = TypeVar("V")


class AVLTree(Generic[K, V]):
    """Optional balanced binary search tree for indexed lookup."""

    def __init__(self) -> None:
        """Initialize tree storage."""
        raise NotImplementedError

    def insert(self, key: K, value: V) -> None:
        """Insert or update a key-value pair."""
        raise NotImplementedError

    def delete(self, key: K) -> bool:
        """Delete a key and return whether it was found."""
        raise NotImplementedError

    def search(self, key: K) -> V | None:
        """Return a value by key, or None when missing."""
        raise NotImplementedError

    def in_order(self) -> list[tuple[K, V]]:
        """Return key-value pairs in sorted key order."""
        raise NotImplementedError
