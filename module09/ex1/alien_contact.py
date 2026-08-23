"""Exercise 1: custom validation with @model_validator (Pydantic v2).

An AlienContact model enforces business rules that go beyond simple field
constraints, using a model-level validator that runs after field validation.
"""
from datetime import datetime
from enum import Enum
from typing import Optional

from pydantic import BaseModel, Field, ValidationError, model_validator

SEPARATOR = "=" * 40


class ContactType(str, Enum):
    RADIO = "radio"
    VISUAL = "visual"
    PHYSICAL = "physical"
    TELEPATHIC = "telepathic"


class AlienContact(BaseModel):
    """Validated alien contact report."""

    contact_id: str = Field(min_length=5, max_length=15)
    timestamp: datetime
    location: str = Field(min_length=3, max_length=100)
    contact_type: ContactType
    signal_strength: float = Field(ge=0.0, le=10.0)
    duration_minutes: int = Field(ge=1, le=1440)
    witness_count: int = Field(ge=1, le=100)
    message_received: Optional[str] = Field(default=None, max_length=500)
    is_verified: bool = False

    @model_validator(mode="after")
    def check_business_rules(self) -> "AlienContact":
        if not self.contact_id.startswith("AC"):
            raise ValueError("Contact ID must start with 'AC' (Alien Contact)")
        if self.contact_type is ContactType.PHYSICAL and not self.is_verified:
            raise ValueError("Physical contact reports must be verified")
        if self.contact_type is ContactType.TELEPATHIC and (
            self.witness_count < 3
        ):
            raise ValueError(
                "Telepathic contact requires at least 3 witnesses"
            )
        if self.signal_strength > 7.0 and not self.message_received:
            raise ValueError(
                "Strong signals should include received messages"
            )
        return self


def clean_error(error: ValidationError) -> str:
    """Return the first error message without Pydantic's 'Value error, '."""
    message = str(error.errors()[0]["msg"])
    prefix = "Value error, "
    return message[len(prefix):] if message.startswith(prefix) else message


def display_contact(contact: AlienContact) -> None:
    print("Valid contact report:")
    print(f"ID: {contact.contact_id}")
    print(f"Type: {contact.contact_type.value}")
    print(f"Location: {contact.location}")
    print(f"Signal: {contact.signal_strength}/10")
    print(f"Duration: {contact.duration_minutes} minutes")
    print(f"Witnesses: {contact.witness_count}")
    if contact.message_received is not None:
        print(f"Message: '{contact.message_received}'")


def main() -> None:
    print("Alien Contact Log Validation")
    print(SEPARATOR)

    contact = AlienContact.model_validate({
        "contact_id": "AC_2024_001",
        "timestamp": "2024-07-14T22:15:00",
        "location": "Area 51, Nevada",
        "contact_type": ContactType.RADIO,
        "signal_strength": 8.5,
        "duration_minutes": 45,
        "witness_count": 5,
        "message_received": "Greetings from Zeta Reticuli",
    })
    display_contact(contact)

    print()
    print(SEPARATOR)
    print("Expected validation error:")
    try:
        AlienContact.model_validate({
            "contact_id": "AC_2024_002",
            "timestamp": "2024-07-15T03:00:00",
            "location": "Roswell, New Mexico",
            "contact_type": ContactType.TELEPATHIC,
            "signal_strength": 5.0,
            "duration_minutes": 10,
            "witness_count": 1,  # invalid: telepathic needs at least 3
        })
    except ValidationError as error:
        print(clean_error(error))


if __name__ == "__main__":
    main()
