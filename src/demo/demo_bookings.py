"""
Booking demo / test script
File: src/demo/demo_bookings.py
Author: B
"""

from datetime import datetime, date, timedelta

from src.models.campus import Campus, Booking
from src.features.booking_system import BookingSystem
from src.features.booking_system_b import get_next_event, get_events_for_day


def print_booking(booking: Booking) -> None:
    """Print one booking in a readable format."""
    print(f"Booking ID: {booking.booking_id}")
    print(f"Room: {booking.room_id}")
    print(f"Title: {booking.title}")
    print(f"Organizer: {booking.organizer}")
    print(
        f"Time: {booking.start_time.strftime('%Y-%m-%d %H:%M')} - "
        f"{booking.end_time.strftime('%Y-%m-%d %H:%M')}"
    )
    print("-" * 40)


def print_booking_list(title: str, bookings: list[Booking]) -> None:
    """Print a labeled list of bookings."""
    print(f"\n{title}")
    print("=" * len(title))

    if not bookings:
        print("No bookings found.")
        return

    for booking in bookings:
        print_booking(booking)


def create_sample_bookings() -> list[Booking]:
    """Create a readable small demo dataset."""
    return [
        Booking(
            booking_id="B101",
            room_id="ICT-121",
            title="Study Group",
            start_time=datetime(2026, 4, 15, 10, 0),
            end_time=datetime(2026, 4, 15, 11, 0),
            organizer="Ted"
        ),
        Booking(
            booking_id="B102",
            room_id="ICT-201",
            title="Project Meeting",
            start_time=datetime(2026, 4, 15, 12, 0),
            end_time=datetime(2026, 4, 15, 13, 30),
            organizer="Alex"
        ),
        Booking(
            booking_id="B103",
            room_id="ENG-103",
            title="Lab Review",
            start_time=datetime(2026, 4, 15, 15, 0),
            end_time=datetime(2026, 4, 15, 16, 0),
            organizer="Chris"
        ),
        Booking(
            booking_id="B104",
            room_id="ICT-121",
            title="Evening Workshop",
            start_time=datetime(2026, 4, 16, 18, 0),
            end_time=datetime(2026, 4, 16, 20, 0),
            organizer="Morgan"
        ),
    ]


def create_large_test_dataset() -> list[Booking]:
    """Create 100 bookings to satisfy project scale testing."""
    bookings: list[Booking] = []
    base_time = datetime(2026, 4, 20, 8, 0)

    room_ids = ["ICT-121", "ICT-201", "ENG-103", "SCI-301", "LIB-210"]

    for i in range(100):
        room_id = room_ids[i % len(room_ids)]
        day_offset = i // 10
        hour_offset = i % 10

        start_time = base_time + timedelta(days=day_offset, hours=hour_offset)
        end_time = start_time + timedelta(minutes=50)

        bookings.append(
            Booking(
                booking_id=f"T{i + 1:03d}",
                room_id=room_id,
                title=f"Test Event {i + 1}",
                start_time=start_time,
                end_time=end_time,
                organizer=f"Organizer {i + 1}"
            )
        )

    return bookings


def main() -> None:
    """Run booking system demo/test cases."""
    campus = Campus()
    booking_system = BookingSystem(campus)

    print("ADDING SAMPLE BOOKINGS")
    print("======================")
    for booking in create_sample_bookings():
        booking_system.add_booking(booking)
        print(f"Added booking {booking.booking_id}: {booking.title}")

    print_booking_list("ALL BOOKINGS", booking_system.get_all_bookings())

    start_range = datetime(2026, 4, 15, 10, 0)
    end_range = datetime(2026, 4, 15, 14, 0)
    bookings_in_range = booking_system.get_bookings_in_range(start_range, end_range)
    print_booking_list(
        "BOOKINGS BETWEEN 2026-04-15 10:00 AND 2026-04-15 14:00",
        bookings_in_range
    )

    next_event = get_next_event(booking_system)
    print("\nNEXT EVENT")
    print("==========")
    if next_event is None:
        print("No current or upcoming bookings.")
    else:
        print_booking(next_event)

    day_events = get_events_for_day(booking_system, date(2026, 4, 15))
    print_booking_list("EVENTS FOR 2026-04-15", day_events)

    removed = booking_system.remove_booking("B102")
    print("\nREMOVE BOOKING")
    print("==============")
    print(f"Removed B102: {removed}")

    print_booking_list("BOOKINGS AFTER REMOVAL", booking_system.get_all_bookings())

    large_campus = Campus()
    large_booking_system = BookingSystem(large_campus)

    for booking in create_large_test_dataset():
        large_booking_system.add_booking(booking)

    print("\nLARGE DATASET TEST")
    print("==================")
    print(f"Total bookings loaded: {len(large_booking_system.get_all_bookings())}")


if __name__ == "__main__":
    main()