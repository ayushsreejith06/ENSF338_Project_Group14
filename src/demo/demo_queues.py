from __future__ import annotations

from src.models.service_request import ServiceRequest
from src.structures.request_pipeline import RequestPipeline
from src.structures.service_priority_queue import ServicePriorityQueue


def build_demo_requests() -> list[ServiceRequest]:
    """
    Creates 20 requests to satisfy the project requirement to simulate
    at least 20 sequential incoming requests.
    """
    raw_requests = [
        ("navigation", "Route from ICT to Science A", "Standard", "student-01"),
        ("service", "Printer jam in Library", "Low", "library-desk"),
        ("service", "Server room temperature alert", "Emergency", "it-monitor"),
        ("navigation", "Route from ENG Block to Gym", "Standard", "student-02"),
        ("service", "Projector failure in ICT-121", "Emergency", "instructor-01"),
        ("service", "Replace whiteboard markers", "Low", "staff-02"),
        ("navigation", "Route from Residence to ICT", "Standard", "visitor-01"),
        ("service", "Wi-Fi outage in Student Union", "Emergency", "network-monitor"),
        ("navigation", "Route from Parkade to Library", "Standard", "student-03"),
        ("service", "Desk key request", "Low", "admin-01"),
        ("service", "Room booking conflict support", "Standard", "booking-system"),
        ("navigation", "Route from MFH to Library", "Standard", "student-04"),
        ("service", "Lab PC will not boot", "Emergency", "lab-tech"),
        ("navigation", "Route from Gym to ICT", "Standard", "student-05"),
        ("service", "Chair replacement request", "Low", "facilities"),
        ("navigation", "Route from Science A to Parkade", "Standard", "student-06"),
        ("service", "Door access card failure", "Standard", "security-desk"),
        ("service", "Flood warning near ENG Block", "Emergency", "sensor-node"),
        ("navigation", "Route from Student Union to Residence", "Standard", "student-07"),
        ("service", "Routine cable cleanup", "Low", "maintenance-01"),
    ]
    return [
        ServiceRequest(
            request_type=req_type,
            description=description,
            priority=priority,
            source=source,
        )
        for req_type, description, priority, source in raw_requests
    ]


def demo_request_pipeline(requests: list[ServiceRequest]) -> None:
    print("=" * 72)
    print("FIFO REQUEST PIPELINE DEMO")
    print("=" * 72)

    pipeline = RequestPipeline()

    print("\nEnqueueing 20 incoming requests in arrival order:\n")
    for req in requests:
        pipeline.enqueue(req)
        print(f"ENQUEUE -> {req}")

    print("\nProcessing requests in FIFO order:\n")
    processed_count = 0
    while not pipeline.is_empty():
        current = pipeline.process_next()
        processed_count += 1
        print(f"PROCESS {processed_count:02d} -> {current}")

    print(f"\nTotal requests processed in FIFO order: {processed_count}")


def demo_priority_queue(requests: list[ServiceRequest]) -> None:
    print("\n" + "=" * 72)
    print("PRIORITY QUEUE DEMO")
    print("=" * 72)

    pq = ServicePriorityQueue()

    print("\nInserting requests with mixed priorities:\n")
    for req in requests:
        pq.enqueue(req)
        print(
            f"ENQUEUE -> id={req.request_id:02d}, "
            f"priority={req.priority:<9} description={req.description}"
        )

    print("\nDequeuing in urgency order (Emergency -> Standard -> Low):\n")
    served_count = 0
    while not pq.is_empty():
        current = pq.dequeue()
        served_count += 1
        print(
            f"SERVE   -> #{served_count:02d} "
            f"id={current.request_id:02d}, "
            f"priority={current.priority:<9} description={current.description}"
        )

    print(f"\nTotal requests served by priority: {served_count}")


def main() -> None:
    requests = build_demo_requests()
    demo_request_pipeline(requests)
    demo_priority_queue(build_demo_requests())


if __name__ == "__main__":
    main()
