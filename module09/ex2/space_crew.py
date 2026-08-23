"""Exercise 2: nested Pydantic models and complex relationships.

A SpaceMission owns a list of CrewMember models. A model validator enforces
crew safety and operational requirements before a mission can be approved.
"""
from datetime import datetime
from enum import Enum

from pydantic import BaseModel, Field, ValidationError, model_validator

SEPARATOR = "=" * 41


class Rank(str, Enum):
    CADET = "cadet"
    OFFICER = "officer"
    LIEUTENANT = "lieutenant"
    CAPTAIN = "captain"
    COMMANDER = "commander"


class CrewMember(BaseModel):
    """A single crew member aboard a mission."""

    member_id: str = Field(min_length=3, max_length=10)
    name: str = Field(min_length=2, max_length=50)
    rank: Rank
    age: int = Field(ge=18, le=80)
    specialization: str = Field(min_length=3, max_length=30)
    years_experience: int = Field(ge=0, le=50)
    is_active: bool = True


class SpaceMission(BaseModel):
    """A mission with its crew and safety requirements."""

    mission_id: str = Field(min_length=5, max_length=15)
    mission_name: str = Field(min_length=3, max_length=100)
    destination: str = Field(min_length=3, max_length=50)
    launch_date: datetime
    duration_days: int = Field(ge=1, le=3650)
    crew: list[CrewMember] = Field(min_length=1, max_length=12)
    mission_status: str = "planned"
    budget_millions: float = Field(ge=1.0, le=10000.0)

    @model_validator(mode="after")
    def check_safety_rules(self) -> "SpaceMission":
        if not self.mission_id.startswith("M"):
            raise ValueError("Mission ID must start with 'M'")

        leaders = {Rank.COMMANDER, Rank.CAPTAIN}
        if not any(member.rank in leaders for member in self.crew):
            raise ValueError(
                "Mission must have at least one Commander or Captain"
            )

        if self.duration_days > 365:
            experienced = sum(
                1 for member in self.crew if member.years_experience >= 5
            )
            if experienced * 2 < len(self.crew):
                raise ValueError(
                    "Long missions need at least 50% experienced crew "
                    "(5+ years)"
                )

        if not all(member.is_active for member in self.crew):
            raise ValueError("All crew members must be active")
        return self


def display_mission(mission: SpaceMission) -> None:
    print("Valid mission created:")
    print(f"Mission: {mission.mission_name}")
    print(f"ID: {mission.mission_id}")
    print(f"Destination: {mission.destination}")
    print(f"Duration: {mission.duration_days} days")
    print(f"Budget: ${mission.budget_millions}M")
    print(f"Crew size: {len(mission.crew)}")
    print("Crew members:")
    for member in mission.crew:
        print(f"- {member.name} ({member.rank.value}) - "
              f"{member.specialization}")


def build_valid_crew() -> list[CrewMember]:
    return [
        CrewMember(
            member_id="CM001",
            name="Sarah Connor",
            rank=Rank.COMMANDER,
            age=45,
            specialization="Mission Command",
            years_experience=20,
        ),
        CrewMember(
            member_id="CM002",
            name="John Smith",
            rank=Rank.LIEUTENANT,
            age=38,
            specialization="Navigation",
            years_experience=12,
        ),
        CrewMember(
            member_id="CM003",
            name="Alice Johnson",
            rank=Rank.OFFICER,
            age=31,
            specialization="Engineering",
            years_experience=7,
        ),
    ]


def main() -> None:
    print("Space Mission Crew Validation")
    print(SEPARATOR)

    mission = SpaceMission.model_validate({
        "mission_id": "M2024_MARS",
        "mission_name": "Mars Colony Establishment",
        "destination": "Mars",
        "launch_date": "2024-06-01T09:00:00",
        "duration_days": 900,
        "crew": build_valid_crew(),
        "mission_status": "approved",
        "budget_millions": 2500.0,
    })
    display_mission(mission)

    print()
    print(SEPARATOR)
    print("Expected validation error:")
    try:
        SpaceMission.model_validate({
            "mission_id": "M2024_MOON",
            "mission_name": "Lunar Survey",
            "destination": "Moon",
            "launch_date": "2024-09-01T09:00:00",
            "duration_days": 30,
            "crew": [
                CrewMember(
                    member_id="CM010",
                    name="Bob Miller",
                    rank=Rank.OFFICER,
                    age=29,
                    specialization="Science",
                    years_experience=4,
                ),
            ],  # invalid: no Commander or Captain aboard
            "budget_millions": 500.0,
        })
    except ValidationError as error:
        message = str(error.errors()[0]["msg"])
        prefix = "Value error, "
        if message.startswith(prefix):
            message = message[len(prefix):]
        print(message)


if __name__ == "__main__":
    main()
