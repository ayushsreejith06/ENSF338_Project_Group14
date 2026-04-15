from src.demo.demo_bookings import main as run_booking_demo
from src.demo.demo_queues import main as run_queue_demo
from src.demo.demo_navigation import run_demo as run_navigation_demo
from src.demo.demo_lookup import main as run_lookup_demo
from src.io.seed_data import load_buildings_seed
import os

def run_lookup() -> None:
    """Run a basic lookup demo using shared building seed data."""
    print("\n=== Lookup ===")
    try:
        run_lookup_demo()
    except Exception as e:
        print(f"Lookup error: {e}")
       
    
def run_navigation() -> None:
    """Run the navigation feature."""
    print("\n=== Navigation ===")
    try:
        run_navigation_demo()
    except Exception as e:
        print(f"Navigation error: {e}")

def run_booking() -> None:
    """Run the booking feature."""
    print("\n=== Booking ===")
    try:
        run_booking_demo()
    except Exception as e:
        print(f"Booking error: {e}")


def run_queue_system() -> None:
    """Run the queue/request processing feature."""
    print("\n=== Queue System ===")
    try:
        run_queue_demo()
    except Exception as e:
        print(f"Queue system error: {e}")

def print_menu() -> None:
    """Print the main menu options."""
    print("\n=== ENSF 338 Campus Navigation and Event Management System ===")
    print("1. Lookup")
    print("2. Navigation")
    print("3. Booking")
    print("4. Queue System")
    print("0. Exit")

def clear_screen() -> None:
    """Clear the terminal screen."""
    os.system("cls" if os.name == "nt" else "clear")

def pause() -> None:
    """Pause until the user is ready to continue then clear screen."""
    input("\nPress Enter to continue...")
    clear_screen()


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