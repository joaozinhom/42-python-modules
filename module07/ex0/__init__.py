"""ex0 package: the Abstract Factory pattern for Creature cards.

Only the abstract building blocks (``Creature``, ``CreatureFactory``) and the
concrete factories are exposed. Concrete Creatures are intentionally NOT
exported: they can only be obtained through a factory.
"""
from .creature import Creature, CreatureFactory
from .factories import AquaFactory, FlameFactory

__all__ = ["Creature", "CreatureFactory", "FlameFactory", "AquaFactory"]
