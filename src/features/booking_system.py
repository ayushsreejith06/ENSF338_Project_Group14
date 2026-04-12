"""
Booking System (src/features/booking_system.py)
Author: Leo
"""

from datetime import datetime
from typing import Optional, List
from pathlib import Path
import bisect

from ..models.campus import Booking, Campus


class BookingSystem:
    """Manages all room bookings and events on campus"""
    
    def __init__(self, campus: Campus, storage_file: Optional[str] = None):
        """
        Initialize booking system with campus data
        """
        self.campus = campus
        self.storage_file = storage_file
        
        self._sorted_bookings: List[Booking] = []
        self._rebuild_sorted_list()
        
        if storage_file and Path(storage_file).exists():
            self.load_from_file(storage_file)
    
    def _rebuild_sorted_list(self) -> None:
        """Rebuild the sorted bookings list from campus data"""
        self._sorted_bookings = sorted(
            self.campus.bookings.values(),
            key=lambda b: b.start_time
        )
    
    def _find_conflicts(self, booking: Booking) -> List[Booking]:
        """Find bookings that conflict with the proposed booking."""
        conflicts = []
        
        for existing_booking in self.campus.bookings.values():
            if existing_booking.room_id == booking.room_id and booking.overlaps_with(existing_booking):
                conflicts.append(existing_booking)
        
        return conflicts
    
    def get_conflicts(self, booking: Booking) -> List[Booking]:
        """Public method to check for conflicts."""
        return self._find_conflicts(booking)
    
    def add_booking(self, booking: Booking) -> str:
        """
        Add a new booking
        """
        conflicts = self._find_conflicts(booking)
        if conflicts:
            conflict_info = ", ".join([f"Booking {b.booking_id} ({b.title})" 
                                     for b in conflicts[:3]])
            if len(conflicts) > 3:
                conflict_info += f"... and {len(conflicts) - 3} more"
            raise ValueError(f"Booking conflicts with: {conflict_info}")
        
        self.campus.bookings[booking.booking_id] = booking
        
        insertion_point = bisect.bisect_left(
            [b.start_time for b in self._sorted_bookings],
            booking.start_time
        )
        self._sorted_bookings.insert(insertion_point, booking)
        
        if self.storage_file:
            self.save_to_file(self.storage_file)
        
        return booking.booking_id
    
    def remove_booking(self, booking_id: str) -> bool:
        """
        Remove a booking by ID
        """
        if booking_id not in self.campus.bookings:
            return False
        
        del self.campus.bookings[booking_id]
        
        for i, booking in enumerate(self._sorted_bookings):
            if booking.booking_id == booking_id:
                del self._sorted_bookings[i]
                break
        
        if self.storage_file:
            self.save_to_file(self.storage_file)
        
        return True
    
    def get_booking(self, booking_id: str) -> Optional[Booking]:
        """Retrieve booking by ID"""
        return self.campus.bookings.get(booking_id)
    
    def get_all_bookings(self) -> List[Booking]:
        """Get all bookings in chronological order"""
        return self._sorted_bookings.copy()
    
    def get_bookings_in_range(self, start_time: datetime, end_time: datetime) -> List[Booking]:
        """
        Get all bookings that occur within a specified time range.
        """
        if start_time >= end_time:  # Invaild time range.
            return []
        
        start_idx = bisect.bisect_left(
            [b.start_time for b in self._sorted_bookings],
            start_time
        )
        
        result = []
        for i in range(start_idx, len(self._sorted_bookings)):
            booking = self._sorted_bookings[i]
            if booking.start_time >= end_time:
                break
            if booking.is_in_time_range(start_time, end_time):
                result.append(booking)
        
        return result
    
    def get_bookings_for_room(self, room_id: str) -> List[Booking]:
        """
        Get bookings for a specific room
        """
        return [
            booking for booking in self._sorted_bookings
            if booking.room_id == room_id
        ]