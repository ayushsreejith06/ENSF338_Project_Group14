# Campus Navigation and Event Management System

This project is focused on implementing core data structures and integrating them into a unified campus system.

---

## Overview

The system is designed to replicate a campus environment with multiple interacting components:

* **Navigation System** – finds the shortest path routing between buildings
* **Booking System** – scheduling and queries for rooms and events
* **Request Pipeline** – FIFO + priority-based request handling
* **Lookup Service** – accessing campus data quickly (buildings, rooms, etc.)

Each component is developed independently in their dedicated branches and later integrated into a single application.

---

## Project Structure

```
src/
│
├── models/         # Shared data models
├── structures/     # Data structures (graph, hash index, etc.)
├── features/       # Feature logic (lookup, navigation, booking, queue)
├── io/             # Data loading utilities
├── demo/           # Optional demo/testing scripts
├── utils/          # Shared helpers (if needed)
│
data/               # Seed data (JSON)
report/             # Report and documentation
```

---

## How to Run

From the project root:

```bash
python -m src.main
```

---

## Menu Options

When the program runs, you will see a menu:

```
1. Lookup
2. Navigation
3. Booking
4. Queue System
0. Exit
```

---

## System Design

The system is structured as a modular architecture where each component is implemented independently and integrated through a central application runner.

- **Lookup Service**
  - Provides fast key-based access to campus data
  - Supports insert, lookup, and delete operations
  - Uses a hash-based structure for efficient access

- **Navigation System**
  - Uses a graph-based representation of the campus
  - Computes shortest paths between buildings using Dijkstra’s algorithm
  - Maintains navigation history with undo functionality

- **Booking System**
  - Manages room and event scheduling
  - Supports insertion, deletion, and time-based queries
  - Maintains ordered access to upcoming events

- **Request Pipeline**
  - Processes incoming requests using FIFO and priority-based ordering
  - Ensures correct processing order across multiple request types

The system is designed so that each module interacts through clearly defined interfaces, allowing independent development and clean integration.

---

## Team

* Ayush – Lookup + Integration
* Rabi – Navigation + Undo
* Rolanted – Booking System
* Andrew – Request Pipeline
