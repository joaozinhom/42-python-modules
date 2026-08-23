from abc import ABC, abstractmethod


class Creature(ABC):
    """Abstract base class for every Creature card.

    Holds the shared ``name`` and ``type`` attributes, exposes the abstract
    ``attack`` method every concrete Creature must implement, and provides a
    concrete generic ``describe`` method.
    """

    def __init__(self, name: str, creature_type: str) -> None:
        self.name = name
        self.type = creature_type

    @abstractmethod
    def attack(self) -> str:
        ...

    def describe(self) -> str:
        return f"{self.name} is a {self.type} type Creature"


class CreatureFactory(ABC):
    """Abstract factory able to create a base and an evolved Creature.

    Concrete factories tie together a single Creature family (the base form
    and its evolved form).
    """

    @abstractmethod
    def create_base(self) -> Creature:
        ...

    @abstractmethod
    def create_evolved(self) -> Creature:
        ...
