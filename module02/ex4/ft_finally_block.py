class GardenError(Exception):
    def __init__(self, message: str = "Unknown garden error") -> None:
        super().__init__(message)


class PlantError(GardenError):
    def __init__(self, message: str = "Unknown plant error") -> None:
        super().__init__(message)


def water_plant(plant_name: str) -> None:
    if (plant_name != plant_name.capitalize()):
        raise PlantError(f"Invalid plant name to water: '{plant_name}'")
    print(f"Watering {plant_name}: [OK]")
    return (None)


def test_watering_system(plants: list) -> None:
    print("Opening watering system")
    try:
        for plant in plants:
            water_plant(plant)
    except PlantError as e:
        print(f"Caught PlantError: {e}")
        print(".. ending tests and returning to main")
    finally:
        print("Closing watering system")
    return (None)


print("=== Garden Watering System ===\n")
print("Testing valid plants...")
test_watering_system(["Tomato", "Lettuce", "Carrots"])
print("\nTesting invalid plants...")
test_watering_system(["Tomato", "lettuce", "Carrots"])
print("\nCleanup always happens, even with errors!")
