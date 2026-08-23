from abc import ABC, abstractmethod

from ex0 import Creature
from ex1 import HealCapability, TransformCapability


class InvalidStrategyError(Exception):
    """Raised when a strategy is applied to an unsuitable Creature."""


class BattleStrategy(ABC):
    """Abstract strategy describing how a Creature behaves in a fight."""

    name: str = "generic"

    @abstractmethod
    def is_valid(self, creature: Creature) -> bool:
        ...

    @abstractmethod
    def act(self, creature: Creature) -> list[str]:
        ...

    def _guard(self, creature: Creature) -> None:
        if not self.is_valid(creature):
            raise InvalidStrategyError(
                f"Invalid Creature '{creature.name}' for this "
                f"{self.name} strategy"
            )


class NormalStrategy(BattleStrategy):
    name = "normal"

    def is_valid(self, creature: Creature) -> bool:
        return True

    def act(self, creature: Creature) -> list[str]:
        self._guard(creature)
        return [creature.attack()]


class AggressiveStrategy(BattleStrategy):
    name = "aggressive"

    def is_valid(self, creature: Creature) -> bool:
        return isinstance(creature, TransformCapability)

    def act(self, creature: Creature) -> list[str]:
        self._guard(creature)
        assert isinstance(creature, TransformCapability)
        return [creature.transform(), creature.attack(), creature.revert()]


class DefensiveStrategy(BattleStrategy):
    name = "defensive"

    def is_valid(self, creature: Creature) -> bool:
        return isinstance(creature, HealCapability)

    def act(self, creature: Creature) -> list[str]:
        self._guard(creature)
        assert isinstance(creature, HealCapability)
        return [creature.attack(), creature.heal()]
