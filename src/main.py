from src.features.lookup_service import LookupService
from src.io.seed_data import load_buildings_seed


def run_lookup_demo() -> None:
    """Run a basic lookup demo using shared building seed data."""
    service = LookupService()
    service.load_items(load_buildings_seed())

    print("=== Lookup Demo ===")
    print("Total loaded buildings:", service.size())
    print()

    print("Lookup existing building: ICT")
    ict = service.lookup("ICT")
    print(ict)
    print()

    print("Lookup existing building: ENG")
    eng = service.lookup("ENG")
    print(eng)
    print()

    print("Lookup missing building: XYZ")
    missing = service.lookup("XYZ")
    print(missing)
    print()

    print("Delete existing building: GYM")
    print(service.delete("GYM"))
    print("Lookup GYM after delete:")
    print(service.lookup("GYM"))

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

    run_lookup_demo()
    print_integration_status()


if __name__ == "__main__":
    main()