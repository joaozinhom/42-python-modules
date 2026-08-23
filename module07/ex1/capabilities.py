from abc import ABC, abstractmethod
from typing import Optional


class HealCapability(ABC):
    """Capability mixin granting a Creature the ability to heal.

    It intentionally does NOT inherit from ``Creature``: a capability is a
    separate concern that could one day be attached to other kinds of object.
    """

    @abstractmethod
    def heal(self, target: Optional[object] = None) -> str:
        ...


class TransformCapability(ABC):
    """Capability mixin granting a Creature a reversible transformation.

    The ``transformed`` attribute keeps the state persistent, which the
    concrete Creature uses to alter its ``attack`` output.
    """

    transformed: bool = False

    @abstractmethod
    def transform(self) -> str:
        ...

    @abstractmethod
    def revert(self) -> str:
        ...
