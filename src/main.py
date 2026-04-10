from src.features.lookup_service import LookupService
from src.io.seed_data import load_buildings_seed


def run_lookup() -> None:
    """Run a basic lookup demo using shared building seed data."""
    service = LookupService()
    service.load_items(load_buildings_seed())

    print("=== Lookup Demo ===")
    print("Total loaded buildings:", service.size())
    print("ICT:", service.lookup("ICT"))
    print("ENG:", service.lookup("ENG"))
    print("XYZ:", service.lookup("XYZ"))
    print("Delete GYM:", service.delete("GYM"))
    print("GYM after delete:", service.lookup("GYM"))
    
def run_navigation() -> None:
    """Run the navigation feature."""
    print("\n=== Navigation ===")
    print("Navigation feature not integrated yet.")


def run_booking() -> None:
    """Run the booking feature."""
    print("\n=== Booking ===")
    print("Booking feature not integrated yet.")


def run_queue_system() -> None:
    """Run the queue/request processing feature."""
    print("\n=== Queue System ===")
    print("Queue system feature not integrated yet.")

def print_integration_status() -> None:
    """Print the current status of module integration."""
    print()
    print("Navigation module integration: pending")
    print("Booking system integration: pending")
    print("Queue system integration: pending")


def main() -> None:
    """Main entry point for the project."""
    print("=== ENSF 338 Campus Navigation and Event Management System ===")
    print()

    run_lookup()
    print_integration_status()


if __name__ == "__main__":
    try:
        main()
    except Exception as error:
        print("Application failed to start.")
        print(f"Error: {error}")