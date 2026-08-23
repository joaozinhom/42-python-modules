"""ex1 package: extra capabilities layered on top of ex0.

Capabilities (``HealCapability``, ``TransformCapability``) are kept separate
from the ``Creature`` hierarchy. Only capabilities and factories are exposed;
concrete Creatures stay hidden behind their factories.
"""
from .capabilities import HealCapability, TransformCapability
from .factories import HealingCreatureFactory, TransformCreatureFactory

__all__ = [
    "HealCapability",
    "TransformCapability",
    "HealingCreatureFactory",
    "TransformCreatureFactory",
]
