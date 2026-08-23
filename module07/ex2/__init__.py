"""ex2 package: the Strategy pattern for the tournament.

Each strategy knows which Creatures it is suitable for (``is_valid``) and how
they should act during a fight (``act``).
"""
from .strategy import (
    AggressiveStrategy,
    BattleStrategy,
    DefensiveStrategy,
    InvalidStrategyError,
    NormalStrategy,
)

__all__ = [
    "BattleStrategy",
    "NormalStrategy",
    "AggressiveStrategy",
    "DefensiveStrategy",
    "InvalidStrategyError",
]
