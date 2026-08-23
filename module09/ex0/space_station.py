"""Exercise 0: basic Pydantic model creation with BaseModel and Field.

A SpaceStation model validates the vital statistics every station across the
galaxy reports to the Cosmic Data Observatory.
"""
from datetime import datetime
from typing import Optional

from pydantic import BaseModel, Field, ValidationError

SEPARATOR = "=" * 40


class SpaceStation(BaseModel):
    """Validated data for a single space station."""

    station_id: str = Field(min_length=3, max_length=10)
    name: str = Field(min_length=1, max_length=50)
    crew_size: int = Field(ge=1, le=20)
    power_level: float = Field(ge=0.0, le=100.0)
    oxygen_level: float = Field(ge=0.0, le=100.0)
    last_maintenance: datetime
    is_operational: bool = True
    notes: Optional[str] = Field(default=None, max_length=200)


def display_station(station: SpaceStation) -> None:
    status = "Operational" if station.is_operational else "Offline"
    print("Valid station created:")
    print(f"ID: {station.station_id}")
    print(f"Name: {station.name}")
    print(f"Crew: {station.crew_size} people")
    print(f"Power: {station.power_level}%")
    print(f"Oxygen: {station.oxygen_level}%")
    print(f"Status: {status}")


def main() -> None:
    print("Space Station Data Validation")
    print(SEPARATOR)

    # Pydantic converts the ISO string below into a real datetime object.
    station = SpaceStation.model_validate({
        "station_id": "ISS001",
        "name": "International Space Station",
        "crew_size": 6,
        "power_level": 85.5,
        "oxygen_level": 92.3,
        "last_maintenance": "2024-01-15T10:30:00",
    })
    display_station(station)

    print()
    print(SEPARATOR)
    print("Expected validation error:")
    try:
        SpaceStation.model_validate({
            "station_id": "BAD001",
            "name": "Overcrowded Station",
            "crew_size": 30,  # invalid: above the maximum of 20
            "power_level": 50.0,
            "oxygen_level": 50.0,
            "last_maintenance": "2024-01-15T10:30:00",
        })
    except ValidationError as error:
        print(error.errors()[0]["msg"])


if __name__ == "__main__":
    main()
