# Shared API Contract

This document freezes the public interfaces for the Campus Navigation and Event Management System. Teammates must implement against these class names, method names, arguments, and return types.

This phase is only for API centralization. Algorithms and storage internals are intentionally left as skeletons.

## Central Import Surface

Use `src/interfaces.py` as the shared import surface when possible:

```python
from src.interfaces import Booking, BookingSystem, Graph, NavigationManager
```

The names exported by `src/interfaces.py` are public and must not be renamed without team agreement.

## Module Boundaries

- `src/models/`: shared data models only.
- `src/structures/`: data structure skeletons such as graph, priority queue, stack, FIFO queue, booking index, and optional AVL tree.
- `src/features/`: feature managers and services that coordinate structures.
- `src/io/`: data loading and persistence boundary.
- `src/demo/`: demo runner and integration wiring only.

Do not put feature logic in models. Do not put demo or UI code in feature modules. Do not create duplicate public APIs for the same concept.

## Data Models

### `Room`

Defined in `src/models/campus.py`.

```python
Room(room_id: str, capacity: int, room_type: str)
```

Public fields:

- `room_id: str`
- `capacity: int`
- `room_type: str`

### `Building`

Defined in `src/models/campus.py`.

```python
Building(building_id: str, name: str, location: tuple[float, float])
```

Public fields:

- `building_id: str`
- `name: str`
- `location: tuple[float, float]`
- `rooms: list[Room]`

`rooms` is optional at construction time and defaults to an empty list.

### `Booking`

Defined in `src/models/campus.py`.

```python
Booking(
    booking_id: str,
    room_id: str,
    title: str,
    start_time,
    end_time,
    organizer: str,
)
```

Public fields:

- `booking_id: str`
- `room_id: str`
- `title: str`
- `start_time: Any`
- `end_time: Any`
- `organizer: str`

`start_time` and `end_time` are typed as `Any` in the skeleton because the project has not yet frozen whether the team will use `datetime`, strings, or another comparable time representation. Implementations must treat them consistently and as comparable values.

### `Campus`

Defined in `src/models/campus.py`.

```python
Campus()
```

Public fields:

- `buildings: dict[str, Building]`
- `rooms: dict[str, Room]`
- `bookings: dict[str, Booking]`

These fields default to empty dictionaries.

## Data Structures

### `Graph`

Defined in `src/structures/graph.py`.

Graph representation: adjacency list.

Public methods:

```python
def add_node(self, building_id: str) -> None
def add_edge(self, src: str, dst: str, weight: int) -> None
def shortest_path(self, src: str, dst: str) -> tuple[list[str], int]
```

`shortest_path` must use Dijkstra when implemented. It returns a tuple of:

- `list[str]`: building IDs in route order
- `int`: total path weight

### `ServicePriorityQueue`

Defined in `src/structures/priority_queue.py`.

Public methods:

```python
def enqueue(self, request: Any) -> None
def dequeue(self) -> Any | None
def is_empty(self) -> bool
```

The request type is `Any` for now because the request model has not been frozen as part of this phase. Teams must not create a second service queue API with different method names.

### Optional `AVLTree`

Defined in `src/structures/avl_tree.py`.

Public methods:

```python
def insert(self, booking: Booking) -> None
def search_in_range(self, start_time: Any, end_time: Any) -> list[Booking]
```

This is the optional balanced booking index bonus. It must remain booking-focused and must not replace the public `BookingSystem` API.

## Feature Managers And Services

### `NavigationManager`

Defined in `src/features/navigation.py`.

Public methods:

```python
def navigate(self, src: str, dst: str) -> tuple[list[str], int]
def undo(self) -> str | None
```

`navigate` delegates shortest-path work to `Graph.shortest_path`. `undo` uses stack-style route history when implemented.

### `BookingSystem`

Defined in `src/features/booking.py`.

Public methods:

```python
def add_booking(self, booking: Booking) -> None
def remove_booking(self, booking_id: str) -> bool
def get_bookings_in_range(self, start_time: Any, end_time: Any) -> list[Booking]
def get_next_event(self) -> Booking | None
def get_events_for_day(self, day: Any) -> list[Booking]
```

The initial implementation should use a sorted booking structure. If the AVL bonus is implemented later, `BookingSystem` remains the public service API.

### `LookupService`

Defined in `src/features/lookup.py`.

Public methods:

```python
def insert(self, key: str, value: Any) -> None
def lookup(self, key: str) -> Any | None
def delete(self, key: str) -> bool
```

This service is the hash-table-style API for fast building and resource lookup. It is intentionally generic so buildings, rooms, resources, and other values can share the same interface without duplicate method names.

### `RequestPipeline`

Defined in `src/features/request_pipeline.py`.

Public methods:

```python
def enqueue(self, request: Any) -> None
def dequeue(self) -> Any | None
def process_next(self) -> Any | None
```

This is the FIFO incoming request processing pipeline. `process_next` should remove and process the oldest request when implemented.

## Locked Public Methods

These methods are public and must not be renamed:

- `Graph.add_node`
- `Graph.add_edge`
- `Graph.shortest_path`
- `NavigationManager.navigate`
- `NavigationManager.undo`
- `BookingSystem.add_booking`
- `BookingSystem.remove_booking`
- `BookingSystem.get_bookings_in_range`
- `BookingSystem.get_next_event`
- `BookingSystem.get_events_for_day`
- `ServicePriorityQueue.enqueue`
- `ServicePriorityQueue.dequeue`
- `ServicePriorityQueue.is_empty`
- `LookupService.insert`
- `LookupService.lookup`
- `LookupService.delete`
- `RequestPipeline.enqueue`
- `RequestPipeline.dequeue`
- `RequestPipeline.process_next`
- `AVLTree.insert`
- `AVLTree.search_in_range`

Private helper methods may be added with leading underscores, but they are not part of this contract.

## Minimal Signature Notes

Only one signature was slightly tightened from the prompt: methods without explicit return annotations in the prompt now return `Any | None` where they dequeue, lookup, or process unknown request/value objects. This satisfies the project requirement that public methods use Python type hints while keeping request and resource data flexible for parallel implementation.

## Integration Rules

- Import shared contracts from `src/interfaces.py` or from the defining module listed above.
- Do not rename locked public methods.
- Do not add duplicate public APIs for the same feature. Extend internals behind the existing service class instead.
- Keep algorithm implementations inside `src/structures/` or `src/features/`, not in data models.
- Keep demo wiring in `src/demo/`.
- Keep persistence and seed data loading in `src/io/`.
- Coordinate before changing dataclass fields because constructor signatures affect every teammate.

## Known Merge-Risk Files

These files are likely to be touched by multiple teammates and should be edited carefully:

- `docs/API_CONTRACT.md`
- `src/interfaces.py`
- `src/models/campus.py`
- `src/structures/graph.py`
- `src/features/navigation.py`
- `src/features/booking.py`
- `src/structures/priority_queue.py`
- `src/features/lookup.py`
- `src/features/request_pipeline.py`
- `src/structures/avl_tree.py`

To minimize conflicts, each teammate should mainly work in their assigned feature or structure file and avoid broad formatting-only edits to shared contract files.
