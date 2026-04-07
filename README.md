# Campus Navigation and Event Management System

Architecture freeze skeleton for the ENSF 338 group project.

## Current Scope

This repository currently freezes the public API and module boundaries only.
Feature logic is intentionally not implemented yet.

## Package Layout

- `src/models/`: shared dataclasses only.
- `src/interfaces.py`: frozen public contracts for feature teams.
- `src/structures/`: data structure skeletons.
- `src/features/`: feature service skeletons.
- `src/io/`: data loading and persistence boundary.
- `src/demo/`: demo and integration runner code.
- `src/utils/`: shared utilities, only when needed.
- `data/`: seed data location.
- `report/`: project report artifacts.

## Git Workflow

Use feature branches from `dev`, merge completed slices into `dev`, then open
one final pull request from `dev` into `main`.

Avoid renaming public methods in `src/interfaces.py` after this architecture
freeze unless the whole team agrees.
