from src.features.lookup_service import LookupService
from src.io.seed_data import load_buildings_seed


def main() -> None:
    """Run the lookup system demo."""
    service = LookupService()
    service.load_items(load_buildings_seed())

    print("LOOKUP DEMO")
    print("===========")
    print(f"Total loaded buildings: {service.size()}")

    print("\nLOOKUP EXISTING KEYS")
    print("====================")
    print("ICT:", service.lookup("ICT"))
    print("ENG:", service.lookup("ENG"))

    print("\nLOOKUP MISSING KEY")
    print("==================")
    print("XYZ:", service.lookup("XYZ"))

    print("\nDELETE EXISTING KEY")
    print("===================")
    print("Delete GYM:", service.delete("GYM"))
    print("GYM after delete:", service.lookup("GYM"))


if __name__ == "__main__":
    main()