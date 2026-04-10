# ENSF 338 Project – Phase Checklists

Each person should work through their phases in order and check things off as they go.  
Do NOT move to the next phase unless the current one is fully working.

---

## Rabi – Navigation + Undo + Map

### Phase 1 – Graph Setup
- [ ] Create graph structure (adjacency list)
- [ ] Add nodes (buildings)
- [ ] Add weighted edges (pathways)
- [ ] Hardcode a small test graph first
- [ ] Print graph to verify structure

### Phase 2 – Shortest Path
- [ ] Implement Dijkstra’s algorithm
- [ ] Return correct path + total cost
- [ ] Test with multiple source/destination pairs
- [ ] Verify correctness manually

### Phase 3 – Map Loading
- [ ] Load graph from file (edges + weights)
- [ ] Ensure at least 15 nodes + 25 edges
- [ ] Validate input parsing works

### Phase 4 – Navigation Manager
- [ ] Wrap shortest path into `navigate()`
- [ ] Format output clearly (path + time)
- [ ] Handle invalid inputs

### Phase 5 – Undo System
- [ ] Implement stack
- [ ] Store navigation history
- [ ] Implement undo (return previous state)
- [ ] Support multiple undo levels

### Phase 6 – Demo
- [ ] Create demo script
- [ ] Show at least 2 route queries
- [ ] Show undo working
- [ ] Output is clean and readable

---

## Rolanted – Booking System

### Phase 1 – Booking Model
- [ ] Create Booking class
- [ ] Include id, room, time range, etc.
- [ ] Create sample bookings

### Phase 2 – Storage
- [ ] Store bookings in a structured way (list or sorted list)
- [ ] Ensure insert works correctly

### Phase 3 – Core Operations
- [ ] Add booking
- [ ] Remove booking
- [ ] Retrieve bookings

### Phase 4 – Time Range Queries
- [ ] Query bookings within a time range
- [ ] Return correct subset
- [ ] Test edge cases

### Phase 5 – Ordered Access
- [ ] Get next upcoming event
- [ ] Get events for a specific day
- [ ] Ensure ordering is correct

### Phase 6 – Scale + Demo
- [ ] Test with 100+ bookings
- [ ] Create demo script
- [ ] Show range query output
- [ ] Show next-event retrieval

### Phase 7 – (Optional Bonus)
- [ ] Implement AVL tree
- [ ] Maintain balance after insert
- [ ] Show structure before/after inserts

---

## Andrew – Priority Queue + Request Pipeline

### Phase 1 – Priority Queue
- [ ] Create priority queue structure
- [ ] Support at least 3 priority levels
- [ ] Insert requests

### Phase 2 – Priority Processing
- [ ] Always dequeue highest priority first
- [ ] Verify correct ordering

### Phase 3 – FIFO Queue
- [ ] Implement basic queue
- [ ] Enqueue/dequeue works correctly

### Phase 4 – Request Pipeline
- [ ] Combine queue into processing system
- [ ] Process requests in arrival order
- [ ] Handle multiple requests

### Phase 5 – Simulation
- [ ] Simulate at least 20 requests
- [ ] Print processing order
- [ ] Verify FIFO behavior

### Phase 6 – Demo
- [ ] Show priority queue behavior
- [ ] Show FIFO pipeline behavior
- [ ] Output clearly shows ordering

---

## Ayush – Lookup + Integration

### Phase 1 – Lookup Service
- [x] Implement insert
- [x] Implement lookup
- [x] Implement delete
- [x] Test existing + missing keys

### Phase 2 – Data Setup
- [x] Create shared test data (buildings, etc.)
- [x] Ensure consistent formats

### Phase 3 – Integration Layer
- [x] Create main runner
- [ ] Connect navigation, booking, queues, lookup
- [ ] Ensure imports work cleanly

### Phase 4 – Demo Runner
- [x] Create menu or run-all script
- [ ] Trigger all features from one place
- [ ] Ensure everything runs without crashing

### Phase 5 – Testing + PR Review
- [ ] Test each feature after merging into dev
- [ ] Catch integration bugs early
- [ ] Ensure consistent outputs

### Phase 6 – Final Prep
- [ ] Clean README (how to run project)
- [ ] Ensure demo scenarios are reproducible
- [ ] Help collect screenshots
- [ ] Final check before dev → main merge

---

## Final Group Checklist

### Core System
- [ ] All features implemented
- [ ] No crashes / broken imports
- [ ] Code runs end-to-end

### Demo Requirements
- [ ] Shortest path queries (2+ examples)
- [ ] Undo navigation
- [ ] Booking range query
- [ ] Priority queue demo
- [ ] Fast lookup demo (existing + missing key)
- [ ] Request pipeline demo

### Report
- [ ] Design decisions explained
- [ ] Complexity analysis included
- [ ] Challenges + lessons written
- [ ] Contributions table completed

### Submission
- [ ] GitHub repo clean and complete
- [ ] README included
- [ ] `/src` folder complete
- [ ] `/report` PDF included
- [ ] Final zip prepared