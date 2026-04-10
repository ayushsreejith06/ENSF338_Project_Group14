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

def print_menu() -> None:
    """Print the main menu options."""
    print("\n=== ENSF 338 Campus Navigation and Event Management System ===")
    print("1. Lookup")
    print("2. Navigation")
    print("3. Booking")
    print("4. Queue System")
    print("0. Exit")


def pause() -> None:
    """Pause until the user is ready to continue."""
    input("\nPress Enter to continue...")


def main() -> None:
    """Main entry point for the project."""
while True:
        print_menu()
        choice = input("Enter choice: ").strip()

        if choice == "1":
            run_lookup()
            pause()
        elif choice == "2":
            run_navigation()
            pause()
        elif choice == "3":
            run_booking()
            pause()
        elif choice == "4":
            run_queue_system()
            pause()
        elif choice == "0":
            print("Exiting program.")
            break
        else:
            print("Invalid choice. Try again.")
            pause()


if __name__ == "__main__":
    try:
        main()
    except Exception as error:
        print("Application failed to start.")
        print(f"Error: {error}")